import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import logging
logging.basicConfig( level=logging.INFO, format='%(levelname)s:%(message)s')

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://ecosia.org'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        navigation = QToolBar()
        self.addToolBar(navigation)

        backbtn = QAction('Back', self)
        backbtn.triggered.connect(self.browser.back)
        navigation.addAction(backbtn)

        forwardbtn = QAction('Forward', self)
        forwardbtn.triggered.connect(self.browser.forward)
        navigation.addAction(forwardbtn)

        reloadbtn = QAction('Reload', self)
        reloadbtn.triggered.connect(self.browser.reload)
        navigation.addAction(reloadbtn)

        homebtn = QAction('Home', self)
        homebtn.triggered.connect(self.navigate_home)
        navigation.addAction(homebtn)



        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navigation.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://ecosia.org'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('browser')
window = MainWindow()
app.exec_()