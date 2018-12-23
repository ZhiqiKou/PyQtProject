import sys
import Hello
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Hello.Ui_Hello()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())