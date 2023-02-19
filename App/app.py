import sys
from 

app = QApplication(sys.argv)

janela = QWidget()
janela.resize(500, 500)
janela.setWindowTitle('App One')
janela.show()

btn = QPushButton('Botao', janela)
btn.setGeometry(300, 300, 150, 150)
btn.setStyleSheet('background-color:red;color:white')

label = QLabel('texto 1', janela)
label.move(500, 200)
label.setStyleSheet('background-color:black;color')

app.exec()