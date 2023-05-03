from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*

app = QApplication([])
my_win = QWidget()
my_win.setWindowTitle('Wow iPhone')
line = QVBoxLayout()
button = QPushButton('Кнопка с айфон')
line.addWidget(button, alignment=Qt.AlignCenter)
my_win.setLayout(line)
def show_fun():
    fun_=QLabel('1000-7')
    line.addWidget(fun_, alignment=Qt.AlignCenter)
    my_win.setLayout(line)

button.clicked.connect(show_fun)
my_win.resize(700,500)
my_win.show()
app.exec_()

