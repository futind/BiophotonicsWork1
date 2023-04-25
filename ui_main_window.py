# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpinBox, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

from mplwidget import mplwidget
import main_window_resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(878, 525)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(260, 10, 611, 471))
        self.distribution_graphpane_tab = QWidget()
        self.distribution_graphpane_tab.setObjectName(u"distribution_graphpane_tab")
        self.distribution_graph = mplwidget(self.distribution_graphpane_tab)
        self.distribution_graph.setObjectName(u"distribution_graph")
        self.distribution_graph.setGeometry(QRect(9, 9, 591, 421))
        self.tabWidget.addTab(self.distribution_graphpane_tab, "")
        self.density_histogram_tab = QWidget()
        self.density_histogram_tab.setObjectName(u"density_histogram_tab")
        self.density_graph = mplwidget(self.density_histogram_tab)
        self.density_graph.setObjectName(u"density_graph")
        self.density_graph.setGeometry(QRect(9, 9, 591, 421))
        self.tabWidget.addTab(self.density_histogram_tab, "")
        self.perform_pushButton = QPushButton(self.centralwidget)
        self.perform_pushButton.setObjectName(u"perform_pushButton")
        self.perform_pushButton.setGeometry(QRect(10, 230, 241, 31))
        self.pix_label = QLabel(self.centralwidget)
        self.pix_label.setObjectName(u"pix_label")
        self.pix_label.setGeometry(QRect(10, 10, 241, 141))
        self.pix_label.setPixmap(QPixmap(u":/task_prefix/task.png"))
        self.pix_label.setScaledContents(True)
        self.reset_pushButton = QPushButton(self.centralwidget)
        self.reset_pushButton.setObjectName(u"reset_pushButton")
        self.reset_pushButton.setGeometry(QRect(10, 270, 241, 31))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 160, 243, 62))
        self.input_data_layout = QHBoxLayout(self.widget)
        self.input_data_layout.setObjectName(u"input_data_layout")
        self.input_data_layout.setContentsMargins(0, 0, 0, 0)
        self.label_layout = QVBoxLayout()
        self.label_layout.setObjectName(u"label_layout")
        self.photons_quantity_label = QLabel(self.widget)
        self.photons_quantity_label.setObjectName(u"photons_quantity_label")

        self.label_layout.addWidget(self.photons_quantity_label)

        self.beam_radius_label = QLabel(self.widget)
        self.beam_radius_label.setObjectName(u"beam_radius_label")

        self.label_layout.addWidget(self.beam_radius_label)


        self.input_data_layout.addLayout(self.label_layout)

        self.spinBox_layout = QVBoxLayout()
        self.spinBox_layout.setObjectName(u"spinBox_layout")
        self.photons_quantity_spinBox = QSpinBox(self.widget)
        self.photons_quantity_spinBox.setObjectName(u"photons_quantity_spinBox")
        self.photons_quantity_spinBox.setMaximum(100000000)
        self.photons_quantity_spinBox.setValue(1000000)

        self.spinBox_layout.addWidget(self.photons_quantity_spinBox)

        self.beam_radius_doubleSpinBox = QDoubleSpinBox(self.widget)
        self.beam_radius_doubleSpinBox.setObjectName(u"beam_radius_doubleSpinBox")
        self.beam_radius_doubleSpinBox.setMaximum(999999.000000000000000)

        self.spinBox_layout.addWidget(self.beam_radius_doubleSpinBox)


        self.input_data_layout.addLayout(self.spinBox_layout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 878, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.distribution_graphpane_tab), QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0435 \u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0439 \u0444\u043e\u0442\u043e\u043d\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.density_histogram_tab), QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0435\u0432\u043e\u0435 \u0441\u0435\u0447\u0435\u043d\u0438\u0435 \u043f\u043b\u043e\u0442\u043d\u043e\u0441\u0442\u0438 \u0440\u0430\u0441\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u044f", None))
        self.perform_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0441\u0442\u0438 \u0438\u0441\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.pix_label.setText("")
        self.reset_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441", None))
        self.photons_quantity_label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0444\u043e\u0442\u043e\u043d\u043e\u0432 (N)", None))
        self.beam_radius_label.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0434\u0438\u0443\u0441 \u043f\u0443\u0447\u043a\u0430 (a)", None))
    # retranslateUi

