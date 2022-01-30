# Form implementation generated from reading ui file '.\ui\main.ui'
#
# Created by: PyQt6 UI code generator 6.2.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 827)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 790))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1200, 790))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(1200, 790))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_connect_to_db = QtWidgets.QLabel(self.tab_3)
        self.label_connect_to_db.setMinimumSize(QtCore.QSize(0, 30))
        self.label_connect_to_db.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_connect_to_db.setFont(font)
        self.label_connect_to_db.setObjectName("label_connect_to_db")
        self.verticalLayout.addWidget(self.label_connect_to_db)
        self.lineEdit_ip = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_ip.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_ip.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_ip.setFont(font)
        self.lineEdit_ip.setFrame(True)
        self.lineEdit_ip.setObjectName("lineEdit_ip")
        self.verticalLayout.addWidget(self.lineEdit_ip)
        self.lineEdit_port = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_port.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_port.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_port.setFont(font)
        self.lineEdit_port.setFrame(True)
        self.lineEdit_port.setObjectName("lineEdit_port")
        self.verticalLayout.addWidget(self.lineEdit_port)
        self.lineEdit_login = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_login.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_login.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_login.setFont(font)
        self.lineEdit_login.setFrame(True)
        self.lineEdit_login.setObjectName("lineEdit_login")
        self.verticalLayout.addWidget(self.lineEdit_login)
        self.lineEdit_pass = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_pass.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_pass.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_pass.setFont(font)
        self.lineEdit_pass.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhHiddenText|QtCore.Qt.InputMethodHint.ImhNoAutoUppercase|QtCore.Qt.InputMethodHint.ImhNoPredictiveText|QtCore.Qt.InputMethodHint.ImhSensitiveData)
        self.lineEdit_pass.setFrame(True)
        self.lineEdit_pass.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_pass.setObjectName("lineEdit_pass")
        self.verticalLayout.addWidget(self.lineEdit_pass)
        self.lineEdit_name_of_db = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_name_of_db.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_name_of_db.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_name_of_db.setFont(font)
        self.lineEdit_name_of_db.setFrame(True)
        self.lineEdit_name_of_db.setObjectName("lineEdit_name_of_db")
        self.verticalLayout.addWidget(self.lineEdit_name_of_db)
        self.pushButton_connect = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_connect.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_connect.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_connect.setFont(font)
        self.pushButton_connect.setObjectName("pushButton_connect")
        self.verticalLayout.addWidget(self.pushButton_connect)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_result_connect_to_db = QtWidgets.QLabel(self.tab_3)
        self.label_result_connect_to_db.setMinimumSize(QtCore.QSize(0, 150))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_result_connect_to_db.setFont(font)
        self.label_result_connect_to_db.setText("")
        self.label_result_connect_to_db.setObjectName("label_result_connect_to_db")
        self.verticalLayout.addWidget(self.label_result_connect_to_db)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_subject_level_1_ds_info = QtWidgets.QLabel(self.tab)
        self.label_subject_level_1_ds_info.setMinimumSize(QtCore.QSize(0, 30))
        self.label_subject_level_1_ds_info.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(12)
        self.label_subject_level_1_ds_info.setFont(font)
        self.label_subject_level_1_ds_info.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_subject_level_1_ds_info.setObjectName("label_subject_level_1_ds_info")
        self.verticalLayout_2.addWidget(self.label_subject_level_1_ds_info)
        self.comboBox_subject_level_1_add_to_ds = QtWidgets.QComboBox(self.tab)
        self.comboBox_subject_level_1_add_to_ds.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_subject_level_1_add_to_ds.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(12)
        self.comboBox_subject_level_1_add_to_ds.setFont(font)
        self.comboBox_subject_level_1_add_to_ds.setObjectName("comboBox_subject_level_1_add_to_ds")
        self.verticalLayout_2.addWidget(self.comboBox_subject_level_1_add_to_ds)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_subject_level_1_ds_info = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_subject_level_1_ds_info.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_subject_level_1_ds_info.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(14)
        self.lineEdit_subject_level_1_ds_info.setFont(font)
        self.lineEdit_subject_level_1_ds_info.setObjectName("lineEdit_subject_level_1_ds_info")
        self.horizontalLayout.addWidget(self.lineEdit_subject_level_1_ds_info)
        self.checkBox_subject_level_1_add_ds_info = QtWidgets.QCheckBox(self.tab)
        self.checkBox_subject_level_1_add_ds_info.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(12)
        self.checkBox_subject_level_1_add_ds_info.setFont(font)
        self.checkBox_subject_level_1_add_ds_info.setChecked(False)
        self.checkBox_subject_level_1_add_ds_info.setObjectName("checkBox_subject_level_1_add_ds_info")
        self.horizontalLayout.addWidget(self.checkBox_subject_level_1_add_ds_info)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.label_subject_level_2_ds_info = QtWidgets.QLabel(self.tab)
        self.label_subject_level_2_ds_info.setMinimumSize(QtCore.QSize(0, 30))
        self.label_subject_level_2_ds_info.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(12)
        self.label_subject_level_2_ds_info.setFont(font)
        self.label_subject_level_2_ds_info.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_subject_level_2_ds_info.setAutoFillBackground(False)
        self.label_subject_level_2_ds_info.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_subject_level_2_ds_info.setObjectName("label_subject_level_2_ds_info")
        self.verticalLayout_2.addWidget(self.label_subject_level_2_ds_info)
        self.comboBox_subject_level_2_add_to_ds = QtWidgets.QComboBox(self.tab)
        self.comboBox_subject_level_2_add_to_ds.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_subject_level_2_add_to_ds.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(12)
        self.comboBox_subject_level_2_add_to_ds.setFont(font)
        self.comboBox_subject_level_2_add_to_ds.setObjectName("comboBox_subject_level_2_add_to_ds")
        self.verticalLayout_2.addWidget(self.comboBox_subject_level_2_add_to_ds)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_subject_level_2_ds_info = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_subject_level_2_ds_info.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_subject_level_2_ds_info.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(14)
        self.lineEdit_subject_level_2_ds_info.setFont(font)
        self.lineEdit_subject_level_2_ds_info.setObjectName("lineEdit_subject_level_2_ds_info")
        self.horizontalLayout_2.addWidget(self.lineEdit_subject_level_2_ds_info)
        self.checkBox_subject_level_2_add_ds_info = QtWidgets.QCheckBox(self.tab)
        self.checkBox_subject_level_2_add_ds_info.setMinimumSize(QtCore.QSize(0, 30))
        self.checkBox_subject_level_2_add_ds_info.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(12)
        self.checkBox_subject_level_2_add_ds_info.setFont(font)
        self.checkBox_subject_level_2_add_ds_info.setChecked(False)
        self.checkBox_subject_level_2_add_ds_info.setObjectName("checkBox_subject_level_2_add_ds_info")
        self.horizontalLayout_2.addWidget(self.checkBox_subject_level_2_add_ds_info)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.label_subject_level_3_ds_info = QtWidgets.QLabel(self.tab)
        self.label_subject_level_3_ds_info.setMinimumSize(QtCore.QSize(0, 30))
        self.label_subject_level_3_ds_info.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(12)
        self.label_subject_level_3_ds_info.setFont(font)
        self.label_subject_level_3_ds_info.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_subject_level_3_ds_info.setObjectName("label_subject_level_3_ds_info")
        self.verticalLayout_2.addWidget(self.label_subject_level_3_ds_info)
        self.lineEdit_subject_level_3_ds_info = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_subject_level_3_ds_info.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_subject_level_3_ds_info.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(14)
        self.lineEdit_subject_level_3_ds_info.setFont(font)
        self.lineEdit_subject_level_3_ds_info.setObjectName("lineEdit_subject_level_3_ds_info")
        self.verticalLayout_2.addWidget(self.lineEdit_subject_level_3_ds_info)
        self.label_add_source_ds_info = QtWidgets.QLabel(self.tab)
        self.label_add_source_ds_info.setMinimumSize(QtCore.QSize(0, 30))
        self.label_add_source_ds_info.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(12)
        self.label_add_source_ds_info.setFont(font)
        self.label_add_source_ds_info.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_add_source_ds_info.setObjectName("label_add_source_ds_info")
        self.verticalLayout_2.addWidget(self.label_add_source_ds_info)
        self.lineEdit_source_ds_info = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_source_ds_info.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_source_ds_info.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(14)
        self.lineEdit_source_ds_info.setFont(font)
        self.lineEdit_source_ds_info.setObjectName("lineEdit_source_ds_info")
        self.verticalLayout_2.addWidget(self.lineEdit_source_ds_info)
        self.label_add_notes_ds_info = QtWidgets.QLabel(self.tab)
        self.label_add_notes_ds_info.setMinimumSize(QtCore.QSize(0, 30))
        self.label_add_notes_ds_info.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(12)
        self.label_add_notes_ds_info.setFont(font)
        self.label_add_notes_ds_info.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_add_notes_ds_info.setObjectName("label_add_notes_ds_info")
        self.verticalLayout_2.addWidget(self.label_add_notes_ds_info)
        self.lineEdit_notes_ds_info = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_notes_ds_info.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_notes_ds_info.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(14)
        self.lineEdit_notes_ds_info.setFont(font)
        self.lineEdit_notes_ds_info.setObjectName("lineEdit_notes_ds_info")
        self.verticalLayout_2.addWidget(self.lineEdit_notes_ds_info)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkBox_good_for_question_add_to_ds_info = QtWidgets.QCheckBox(self.tab)
        self.checkBox_good_for_question_add_to_ds_info.setMinimumSize(QtCore.QSize(0, 40))
        self.checkBox_good_for_question_add_to_ds_info.setMaximumSize(QtCore.QSize(16777215, 40))
        self.checkBox_good_for_question_add_to_ds_info.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_good_for_question_add_to_ds_info.setFont(font)
        self.checkBox_good_for_question_add_to_ds_info.setObjectName("checkBox_good_for_question_add_to_ds_info")
        self.horizontalLayout_3.addWidget(self.checkBox_good_for_question_add_to_ds_info)
        self.pushButton_add_to_db_ds_info = QtWidgets.QPushButton(self.tab)
        self.pushButton_add_to_db_ds_info.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_add_to_db_ds_info.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_add_to_db_ds_info.setFont(font)
        self.pushButton_add_to_db_ds_info.setAutoDefault(False)
        self.pushButton_add_to_db_ds_info.setFlat(False)
        self.pushButton_add_to_db_ds_info.setObjectName("pushButton_add_to_db_ds_info")
        self.horizontalLayout_3.addWidget(self.pushButton_add_to_db_ds_info)
        self.pushButton_clear_add_to_ds_info = QtWidgets.QPushButton(self.tab)
        self.pushButton_clear_add_to_ds_info.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_clear_add_to_ds_info.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_clear_add_to_ds_info.setFont(font)
        self.pushButton_clear_add_to_ds_info.setObjectName("pushButton_clear_add_to_ds_info")
        self.horizontalLayout_3.addWidget(self.pushButton_clear_add_to_ds_info)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_2.addItem(spacerItem2)
        self.label_result_add_to_ds_info = QtWidgets.QLabel(self.tab)
        self.label_result_add_to_ds_info.setMinimumSize(QtCore.QSize(0, 150))
        self.label_result_add_to_ds_info.setText("")
        self.label_result_add_to_ds_info.setObjectName("label_result_add_to_ds_info")
        self.verticalLayout_2.addWidget(self.label_result_add_to_ds_info)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_2.addItem(spacerItem3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_connect_to_db.setText(_translate("MainWindow", "Connect to DB"))
        self.lineEdit_ip.setPlaceholderText(_translate("MainWindow", "IP"))
        self.lineEdit_port.setPlaceholderText(_translate("MainWindow", "Port"))
        self.lineEdit_login.setPlaceholderText(_translate("MainWindow", "login"))
        self.lineEdit_pass.setPlaceholderText(_translate("MainWindow", "Password"))
        self.lineEdit_name_of_db.setPlaceholderText(_translate("MainWindow", "DataBase"))
        self.pushButton_connect.setText(_translate("MainWindow", "Connect"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Connect to DB"))
        self.label_subject_level_1_ds_info.setText(_translate("MainWindow", "Subject Level 1"))
        self.lineEdit_subject_level_1_ds_info.setPlaceholderText(_translate("MainWindow", "New Subject Level 1"))
        self.checkBox_subject_level_1_add_ds_info.setText(_translate("MainWindow", "Add to DB"))
        self.label_subject_level_2_ds_info.setText(_translate("MainWindow", "Subject Level 2"))
        self.lineEdit_subject_level_2_ds_info.setPlaceholderText(_translate("MainWindow", "New Subject Level 2"))
        self.checkBox_subject_level_2_add_ds_info.setText(_translate("MainWindow", "Add to DB"))
        self.label_subject_level_3_ds_info.setText(_translate("MainWindow", "Subject Level 3"))
        self.lineEdit_subject_level_3_ds_info.setPlaceholderText(_translate("MainWindow", "New Subject Level 3"))
        self.label_add_source_ds_info.setText(_translate("MainWindow", "Source"))
        self.lineEdit_source_ds_info.setPlaceholderText(_translate("MainWindow", "Source"))
        self.label_add_notes_ds_info.setText(_translate("MainWindow", "Notes"))
        self.lineEdit_notes_ds_info.setPlaceholderText(_translate("MainWindow", "Notes"))
        self.checkBox_good_for_question_add_to_ds_info.setText(_translate("MainWindow", "GOOD FOR QUESTION"))
        self.pushButton_add_to_db_ds_info.setText(_translate("MainWindow", "ADD into DB"))
        self.pushButton_clear_add_to_ds_info.setText(_translate("MainWindow", "Clear"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Add to DS info"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Select from DS info"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "DS_QA"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
