from entities.notification import Notification
from entities.task import Task
from entities.user import User
from database_con import get_db_connection


class TaskRepository:

    def __init__(self, conn) -> None:
        self.conn = conn
        self._cursor = self.conn.cursor()

    def fetch_tasks(self, user_id, admin):
        if not admin:
            self._cursor.execute("""SELECT T.title, T.description, T.id, T.done,
                U_by.name, U_By.username, U_By.id, U_To.name, U_To.username, U_To.id
                FROM Tasks T LEFT JOIN Users U_To ON T.assigned_to = U_To.id LEFT JOIN Users U_By ON T.assigned_by = U_By.id 
                WHERE T.assigned_to = %s ORDER BY T.id;""", (user_id, ))
        else:
            self._cursor.execute("""SELECT T.title, T.description, T.id, T.done,
                U_by.name, U_By.username, U_By.id, U_To.name, U_To.username, U_To.id
                FROM Tasks T LEFT JOIN Users U_To ON T.assigned_to = U_To.id LEFT JOIN Users U_By ON T.assigned_by = U_By.id 
                WHERE T.assigned_by = %s ORDER BY T.id;""", (user_id, ))

        results = self._cursor.fetchall()
        task_list = []
        for result in results:
            assigned_by_user = User(result[4], result[5], "", result[6])
            assigned_to_user = User(result[7], result[8], "", result[9])
            task_list.append(Task(
                result[0], result[1], assigned_by_user, assigned_to_user, result[2], result[3]))

        return task_list

    def mark_as_done(self, task_id):
        self._cursor.execute(
            "UPDATE Tasks SET done=TRUE WHERE id=%s;", (task_id, ))
        self.conn.commit()

    def assign_task(self, task: Task, org_id):
        self._cursor.execute("""INSERT INTO Tasks
                                (title, description, assigned_by, assigned_to, org, done)
                                VALUES (%s, %s, %s, %s, %s, FALSE);""",
                             (task.title, task.desc, task.assigned_by.id,
                              task.assigned_to.id, org_id))
        self.conn.commit()

    def check_notifications(self, user_id):
        self._cursor.execute(
            "SELECT message, type FROM Notifications WHERE user_id=%s;", (user_id, ))

        notifications = []

        for result in self._cursor.fetchall():
            notifications.append(Notification(result[0], result[1]))

        self._cursor.execute(
            "DELETE FROM Notifications WHERE user_id=%s;", (user_id, ))
        self.conn.commit()

        return notifications

    def send_notification(self, user_id, message, notification_type):
        self._cursor.execute(
            "INSERT INTO Notifications VALUES (%s, %s, %s);", (user_id, message, notification_type))
        self.conn.commit()

    def delete_users_tasks(self, user_id):
        self._cursor.execute(
            "DELETE FROM Tasks WHERE assigned_to=%s;", (user_id, )
        )
        self.conn.commit()


task_repository = TaskRepository(get_db_connection())