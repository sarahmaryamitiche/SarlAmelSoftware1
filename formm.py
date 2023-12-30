# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formm.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class MyLineEdit(QtWidgets.QLineEdit):

    def __init__(self, parent):
        super(MyLineEdit, self).__init__(parent)
        #super(CustomQLineEidt, self).__init__()

    def mousePressEvent(self, e):
        self.mouseseleted()

    def mouseseleted(self):
        self.clear()
        self.setStyleSheet("color: rgb(0,0,0);\n"
"border: 1.3px solid rgb(150,150,150);\n"
"font-size: 14px;")

class Ui_Form_2(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(516, 512)
        self.formLayout = QtWidgets.QFormLayout(Form)
        self.formLayout.setObjectName("formLayout")
        self.frame_29 = QtWidgets.QFrame(Form)
        self.frame_29.setMinimumSize(QtCore.QSize(500, 500))
        self.frame_29.setMaximumSize(QtCore.QSize(500, 500))
        self.frame_29.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_29.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.verticalLayout_40 = QtWidgets.QVBoxLayout(self.frame_29)
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_40.setSpacing(15)
        self.verticalLayout_40.setObjectName("verticalLayout_40")
        self.label_125 = QtWidgets.QLabel(self.frame_29)
        self.label_125.setStyleSheet("font-size: 40px;")
        self.label_125.setObjectName("label_125")
        self.verticalLayout_40.addWidget(self.label_125, 0, QtCore.Qt.AlignHCenter)
        self.label_126 = QtWidgets.QLabel(self.frame_29)
        self.label_126.setMinimumSize(QtCore.QSize(0, 50))
        self.label_126.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_126.setStyleSheet("font-size: 16px;\n"
"color: #353946;")
        self.label_126.setObjectName("label_126")
        self.verticalLayout_40.addWidget(self.label_126, 0, QtCore.Qt.AlignHCenter)
        self.frame = QtWidgets.QFrame(self.frame_29)
        self.frame.setMinimumSize(QtCore.QSize(320, 160))
        self.frame.setMaximumSize(QtCore.QSize(320, 160))
        self.frame.setStyleSheet("border:none;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tel_8 = MyLineEdit(self.frame)
        self.tel_8.setMinimumSize(QtCore.QSize(300, 25))
        self.tel_8.setMaximumSize(QtCore.QSize(300, 28))
        self.tel_8.setStyleSheet("color: rgb(206, 206, 206);\n"
"border: 1.3px solid rgb(238, 238, 238);\n"
"font-size: 14px;")
        self.tel_8.setAlignment(QtCore.Qt.AlignCenter)
        self.tel_8.setObjectName("tel_8")
        self.verticalLayout.addWidget(self.tel_8)
        self.lineEdit = MyLineEdit(self.frame)
        self.lineEdit.setMinimumSize(QtCore.QSize(300, 30))
        self.lineEdit.setMaximumSize(QtCore.QSize(300, 30))
        self.lineEdit.setStyleSheet("color: rgb(206, 206, 206);\n"
"border: 1.3px solid rgb(238, 238, 238);\n"
"font-size: 14px;")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.mdp_4 = MyLineEdit(self.frame)
        self.mdp_4.setMinimumSize(QtCore.QSize(300, 30))
        self.mdp_4.setMaximumSize(QtCore.QSize(300, 30))
        self.mdp_4.setStyleSheet("border: 1.3px solid rgb(238, 238, 238);\n"
"color: rgb(206, 206, 206);\n"
"font-size: 14px;")
        self.mdp_4.setAlignment(QtCore.Qt.AlignCenter)
        self.mdp_4.setObjectName("mdp_4")
        self.verticalLayout.addWidget(self.mdp_4)
        self.lineEdit_2 =MyLineEdit(self.frame)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(300, 30))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(300, 30))
        self.lineEdit_2.setStyleSheet("border: 1.3px solid rgb(238, 238, 238);\n"
"color: rgb(206, 206, 206);\n"
"font-size: 14px;")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.verticalLayout_40.addWidget(self.frame, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.connecter_4 = QtWidgets.QPushButton(self.frame_29)
        self.connecter_4.setMinimumSize(QtCore.QSize(200, 35))
        self.connecter_4.setMaximumSize(QtCore.QSize(200, 35))
        self.connecter_4.setStyleSheet("font-size: 18px;\n"
"border: none;\n"
"background-color: rgb(57, 195, 221);\n"
"padding: 10px 0px 10px 0px;\n"
"color: white;\n"
"")
        self.connecter_4.setObjectName("connecter_4")
        self.verticalLayout_40.addWidget(self.connecter_4, 0, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(25, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_40.addItem(spacerItem)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.frame_29)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_125.setText(_translate("Form", "PortGest"))
        self.label_126.setText(_translate("Form", "Veuillez introduire les informations de votre base de données"))
        self.tel_8.setText(_translate("Form", "Nom de base de données"))
        self.lineEdit.setText(_translate("Form", "Utilisateur"))
        self.mdp_4.setText(_translate("Form", "Mot de passe"))
        self.lineEdit_2.setText(_translate("Form", "Host"))
        self.connecter_4.setText(_translate("Form", "Valider"))