# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\WS\Python\Lessons\Code\06-上位机开发-PyQt5\ui\my_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(268, 187)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.username = QtWidgets.QLabel(Dialog)
        self.username.setObjectName("username")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.username)
        self.username_edit = QtWidgets.QLineEdit(Dialog)
        self.username_edit.setObjectName("username_edit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.username_edit)
        self.Label = QtWidgets.QLabel(Dialog)
        self.Label.setObjectName("Label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Label)
        self.email_edit = QtWidgets.QLineEdit(Dialog)
        self.email_edit.setObjectName("email_edit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.email_edit)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "请输入个人信息："))
        self.username.setText(_translate("Dialog", "用户名："))
        self.Label.setText(_translate("Dialog", "邮箱"))
