# Form implementation generated from reading ui file 'F:\ericworks\newDrawings\drawingEdit.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(327, 470)
        Dialog.setMinimumSize(QtCore.QSize(327, 334))
        Dialog.setMaximumSize(QtCore.QSize(327, 470))
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 420, 311, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.label_8 = QtWidgets.QLabel(parent=Dialog)
        self.label_8.setGeometry(QtCore.QRect(10, 450, 301, 21))
        self.label_8.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_8.setObjectName("label_8")
        self.layoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 311, 411))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(32767)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.lineEdit_2.setMaxLength(11)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 4, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(parent=self.layoutWidget)
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 4, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 5, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 5, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 6, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(parent=self.layoutWidget)
        self.comboBox_2.setEditable(True)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout.addWidget(self.comboBox_2, 6, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 7, 0, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.lineEdit_8.setInputMask("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 7, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 8, 0, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout.addWidget(self.lineEdit_9, 8, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 9, 0, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.lineEdit_10.setText("")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout.addWidget(self.lineEdit_10, 9, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 10, 0, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout.addWidget(self.lineEdit_11, 10, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 11, 0, 1, 1)
        self.lineEdit_12 = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.lineEdit_12.setAcceptDrops(True)
        self.lineEdit_12.setInputMask("")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout.addWidget(self.lineEdit_12, 11, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 12, 0, 1, 1)
        self.lineEdit_13 = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.lineEdit_13.setAcceptDrops(True)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.gridLayout.addWidget(self.lineEdit_13, 12, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 13, 0, 1, 1)
        self.lineEdit_14 = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.gridLayout.addWidget(self.lineEdit_14, 13, 1, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEdit, self.lineEdit_2)
        Dialog.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        Dialog.setTabOrder(self.lineEdit_3, self.lineEdit_4)
        Dialog.setTabOrder(self.lineEdit_4, self.comboBox)
        Dialog.setTabOrder(self.comboBox, self.lineEdit_6)
        Dialog.setTabOrder(self.lineEdit_6, self.comboBox_2)
        Dialog.setTabOrder(self.comboBox_2, self.lineEdit_8)
        Dialog.setTabOrder(self.lineEdit_8, self.lineEdit_9)
        Dialog.setTabOrder(self.lineEdit_9, self.lineEdit_10)
        Dialog.setTabOrder(self.lineEdit_10, self.lineEdit_11)
        Dialog.setTabOrder(self.lineEdit_11, self.lineEdit_12)
        Dialog.setTabOrder(self.lineEdit_12, self.lineEdit_13)
        Dialog.setTabOrder(self.lineEdit_13, self.lineEdit_14)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "图号编辑"))
        self.label_8.setText(_translate("Dialog", "ID为系统数据库自动增加字段，无需手动添加或修改"))
        self.label.setText(_translate("Dialog", "ID："))
        self.label_2.setText(_translate("Dialog", "料号："))
        self.lineEdit_2.setInputMask(_translate("Dialog", "####-######"))
        self.label_3.setText(_translate("Dialog", "品名："))
        self.label_4.setText(_translate("Dialog", "规格："))
        self.label_12.setText(_translate("Dialog", "温度等级："))
        self.comboBox.setItemText(0, _translate("Dialog", "950"))
        self.comboBox.setItemText(1, _translate("Dialog", "850"))
        self.comboBox.setItemText(2, _translate("Dialog", "1050"))
        self.comboBox.setItemText(3, _translate("Dialog", "1150"))
        self.comboBox.setItemText(4, _translate("Dialog", "常温"))
        self.comboBox.setItemText(5, _translate("Dialog", "无"))
        self.label_13.setText(_translate("Dialog", "密度："))
        self.label_14.setText(_translate("Dialog", "包装方式："))
        self.label_5.setText(_translate("Dialog", "内部图号："))
        self.label_6.setText(_translate("Dialog", "客户图号："))
        self.label_15.setText(_translate("Dialog", "物料描述："))
        self.label_11.setText(_translate("Dialog", "产品图纸："))
        self.label_9.setText(_translate("Dialog", "生产图纸："))
        self.label_10.setText(_translate("Dialog", "客户图纸："))
        self.label_7.setText(_translate("Dialog", "备注："))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
