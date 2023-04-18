from PyQt5.QtWidgets import QApplication, QMainWindow
from Email import Ui_MainWindow
import sys
from check_email import email
class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        self.uic.pushButton_Enter.clicked.connect(self.app)

    def app(self):
        data= self.uic.textEdit_mail.toPlainText()
        result = email(data)
        self.uic.label_email.setText(result)

    def show(self):
        # command to run
        self.main_win.show()

if __name__ == "__main__":
    check_email = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(check_email.exec())