# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\WS\Python\Lessons\Code\06-上位机开发-PyQt5\ui\my_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MyWidget(object):
    def setupUi(self, MyWidget):
        MyWidget.setObjectName("MyWidget")
        MyWidget.resize(356, 357)
        self.verticalLayout = QtWidgets.QVBoxLayout(MyWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(MyWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(MyWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(MyWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(MyWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton = QtWidgets.QRadioButton(MyWidget)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(MyWidget)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(MyWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(MyWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(MyWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 4, 1, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(MyWidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 5, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox = QtWidgets.QCheckBox(MyWidget)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_2.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(MyWidget)
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_2.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(MyWidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout_2.addWidget(self.checkBox_3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(MyWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(MyWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.btn_submit = QtWidgets.QPushButton(MyWidget)
        self.btn_submit.setObjectName("btn_submit")
        self.gridLayout.addWidget(self.btn_submit, 6, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(MyWidget)
        QtCore.QMetaObject.connectSlotsByName(MyWidget)

    def retranslateUi(self, MyWidget):
        _translate = QtCore.QCoreApplication.translate
        MyWidget.setWindowTitle(_translate("MyWidget", "Form"))
        self.label_3.setText(_translate("MyWidget", "性别："))
        self.label_4.setText(_translate("MyWidget", "爱好："))
        self.label_6.setText(_translate("MyWidget", "择偶要求："))
        self.radioButton.setText(_translate("MyWidget", "男"))
        self.radioButton_2.setText(_translate("MyWidget", "女"))
        self.label_5.setText(_translate("MyWidget", "个性签名："))
        self.checkBox.setText(_translate("MyWidget", "抽烟"))
        self.checkBox_2.setText(_translate("MyWidget", "喝酒"))
        self.checkBox_3.setText(_translate("MyWidget", "烫头"))
        self.label.setText(_translate("MyWidget", "用户名："))
        self.label_2.setText(_translate("MyWidget", "密码："))
        self.btn_submit.setText(_translate("MyWidget", "确认注册"))
