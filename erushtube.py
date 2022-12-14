# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'erushtube.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from pytube import YouTube
from pytube.exceptions import RegexMatchError
import datetime
from PyQt5.QtGui import QImage, QPixmap
import requests
from threading import Thread
import time

size=0
class Ui_MainWindow(object):
    global size
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(277, 779)
        MainWindow.setStyleSheet("")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(10, 10, 256, 710))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(25)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_url = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(17)
        self.label_url.setFont(font)
        self.label_url.setObjectName("label_url")
        self.lineEdit_url = QtWidgets.QLineEdit(self.splitter)
        self.lineEdit_url.setObjectName("lineEdit_url")
        self.line = QtWidgets.QFrame(self.splitter)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_songname = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_songname.setFont(font)
        self.label_songname.setObjectName("label_songname")
        self.verticalLayout_2.addWidget(self.label_songname)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_length = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_length.setFont(font)
        self.label_length.setObjectName("label_length")
        self.verticalLayout_2.addWidget(self.label_length)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_views = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_views.setFont(font)
        self.label_views.setObjectName("label_views")
        self.verticalLayout_2.addWidget(self.label_views)
        self.graphicsView = QtWidgets.QLabel(self.splitter)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_720p = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_720p.setFont(font)
        self.radioButton_720p.setObjectName("radioButton_720p")
        self.verticalLayout.addWidget(self.radioButton_720p)
        self.radioButton_480p = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_480p.setFont(font)
        self.radioButton_480p.setObjectName("radioButton_480p")
        self.verticalLayout.addWidget(self.radioButton_480p)
        self.radioButton_360p = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_360p.setFont(font)
        self.radioButton_360p.setObjectName("radioButton_360p")
        self.verticalLayout.addWidget(self.radioButton_360p)
        self.radioButton_mp3 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_mp3.setFont(font)
        self.radioButton_mp3.setObjectName("radioButton_mp3")
        self.verticalLayout.addWidget(self.radioButton_mp3)
        self.pushButton = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_error = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_error.setFont(font)
        self.label_error.setObjectName("label_error")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 277, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.lineEdit_url.returnPressed.connect(self.get_info)
        self.pushButton.clicked.connect(self.set_stream_object)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ErushTube"))
        self.label.setText(_translate("MainWindow", "ErushTube"))
        self.label_url.setText(_translate("MainWindow", "Youtube Url:"))
        self.label_2.setText(_translate("MainWindow", "Song name:"))
        self.label_songname.setText(_translate("MainWindow", ""))
        self.label_3.setText(_translate("MainWindow", "Length:"))
        self.label_length.setText(_translate("MainWindow", ""))
        self.label_4.setText(_translate("MainWindow", "Views:"))
        self.label_views.setText(_translate("MainWindow", ""))
        self.radioButton_720p.setText(_translate("MainWindow", "720p"))
        self.radioButton_480p.setText(_translate("MainWindow", "480p"))
        self.radioButton_360p.setText(_translate("MainWindow", "360p"))
        self.radioButton_mp3.setText(_translate("MainWindow", "Mp3-Audio only"))
        self.pushButton.setText(_translate("MainWindow", "Download"))
        self.label_error.setText(_translate("MainWindow", ""))
        self.image = QImage()
        self.size = 0

    def get_info(self):
        try:
            url = self.lineEdit_url.text()
            yt = YouTube(url)
            name = yt.title
            length = str(datetime.timedelta(seconds=yt.length))
            views = str(yt.views)
            thumbnail = yt.thumbnail_url
            self.image.loadFromData(requests.get(thumbnail).content)
            self.graphicsView.setPixmap(QPixmap(self.image).scaled(self.graphicsView.width(),self.graphicsView.height(),aspectRatioMode=2))
            self.label_songname.setText(name)
            self.label_length.setText(length)
            self.label_views.setText(views)

            return yt
            #self.graphicsView.
        except RegexMatchError:
            self.label_error.setText(f"Error:Couldn't find video.")
            self.lineEdit_url.clear()


    def set_stream_object(self):
        yt = self.get_info()
        res = ""
        audio=False
        if self.radioButton_720p.isChecked():
            res = '720p'

        elif self.radioButton_480p.isChecked():
            res='480p'

        elif self.radioButton_360p.isChecked():
            res = '360p'

        elif self.radioButton_mp3.isChecked():
            audio=True

        else:
            self.label_error.setText('Error:Choose a resolution.')

        if audio:
            stream=yt.streams.get_audio_only()
            filesize=stream.filesize/(1024*1024)
            self.label_error.setText(f"Filesize:{filesize:.2f} MB")
            folder = str(QtWidgets.QFileDialog.getExistingDirectory(None, "Select Directory"))
            stream.download(filename=f"{yt.title}.mp3", output_path=folder)
            self.label_error.setText("Download Completed")
        else:
            if res !="":
                stream=yt.streams.get_by_resolution(res)
                if stream == None:
                    self.label.setText("Could not find video")
                else:
                    self.label_error.setText(f"Filesize:{stream.filesize / (1024 * 1024):.2f} MB")
                    folder = str(QtWidgets.QFileDialog.getExistingDirectory(None, "Select Directory"))
                    stream.download(output_path=folder)
                    self.label_error.setText("Download Completed")
            else:
                self.label_error.setText('Error:Choose a resolution.')


    # def start_thread(self):
    #     thread_stream = Thread(target=self.set_stream_object)
    #     thread_stream.start()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_MainWindow()
    w = QtWidgets.QMainWindow()
    ex.setupUi(w)
    w.show()
    sys.exit(app.exec_())
