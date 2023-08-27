'''from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindows

# Only needed for access to command line arguments
import sys

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = QMainWindows()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()'''

'''import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)

window = QMainWindow()
window.show()

# Start the event loop.
app.exec()


# Your application won't reach here until you exit and the event
# loop has stopped.'''

'''import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")

        # Set the central widget of the Window.
        self.setCentralWidget(button)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()'''

from senha import APIKEY
import requests
import json

headers = {'Authorization': f'Bearer {APIKEY}', 'content-type': 'application/json'}
link = 'https://api.openai.com/v1/chat/completions'
id_modelo = 'gpt-3.5-turbo'

body_mensagem = {
    'model' = [id_modelo,
               'messages']: [{'role': 'user', 'content': 'escreva um Email'}]
}
body_mensagem = json.dump(body_mensagem)

requisição = requests.post(link, headers=headers, date=body_mensagem)
print(requisição)
print(requisição.text)
