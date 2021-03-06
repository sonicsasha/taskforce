# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_files/new_task_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewFormDialog(object):
    def setupUi(self, NewFormDialog):
        NewFormDialog.setObjectName("NewFormDialog")
        NewFormDialog.resize(541, 292)
        self.verticalLayout = QtWidgets.QVBoxLayout(NewFormDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formTitle = QtWidgets.QLabel(NewFormDialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.formTitle.sizePolicy().hasHeightForWidth())
        self.formTitle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.formTitle.setFont(font)
        self.formTitle.setAlignment(
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.formTitle.setObjectName("formTitle")
        self.verticalLayout.addWidget(self.formTitle)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.taskLabel = QtWidgets.QLabel(NewFormDialog)
        self.taskLabel.setObjectName("taskLabel")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.taskLabel)
        self.taskFill = QtWidgets.QLineEdit(NewFormDialog)
        self.taskFill.setObjectName("taskFill")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.taskFill)
        self.descLabel = QtWidgets.QLabel(NewFormDialog)
        self.descLabel.setObjectName("descLabel")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.descLabel)
        self.descFill = QtWidgets.QTextEdit(NewFormDialog)
        self.descFill.setObjectName("descFill")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.descFill)
        self.assignLabel = QtWidgets.QLabel(NewFormDialog)
        self.assignLabel.setObjectName("assignLabel")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.assignLabel)
        self.assignComboBox = QtWidgets.QComboBox(NewFormDialog)
        self.assignComboBox.setObjectName("assignComboBox")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.assignComboBox)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(NewFormDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(NewFormDialog)
        self.buttonBox.rejected.connect(NewFormDialog.reject)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(NewFormDialog)

    def retranslateUi(self, NewFormDialog):
        _translate = QtCore.QCoreApplication.translate
        NewFormDialog.setWindowTitle(_translate("NewFormDialog", "Dialog"))
        self.formTitle.setText(_translate(
            "NewFormDialog", "Assign a new task"))
        self.taskLabel.setText(_translate("NewFormDialog", "Task:"))
        self.descLabel.setText(_translate("NewFormDialog", "Description:"))
        self.assignLabel.setText(_translate("NewFormDialog", "Assign to:"))
