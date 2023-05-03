from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*

app = QApplication([])
my_win = QWidget()
my_win.setWindowTitle('Wow iPhone')
line = QVBoxLayout()
line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()

button1 = QPushButton('1')
button2 = QPushButton('1')
button3 = QPushButton('1')
button4 = QPushButton('1')
button5 = QPushButton('1')
button6 = QPushButton('1')
line1.addWidget(button1, alignment=Qt.AlignLeft)
line1.addWidget(button2, alignment=Qt.AlignRight)
line2.addWidget(button3, alignment=Qt.AlignLeft)
line2.addWidget(button4, alignment=Qt.AlignRight)
line3.addWidget(button5, alignment=Qt.AlignLeft)
line3.addWidget(button6, alignment=Qt.AlignRight)

line.addLayout(line1)
line.addLayout(line2)
line.addLayout(line3)
my_win.setLayout(line)

my_win.resize(700,500)
my_win.show()
app.exec_()

