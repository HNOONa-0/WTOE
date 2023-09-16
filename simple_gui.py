import sys
import random
from PySide2 import QtCore, QtWidgets, QtGui
from program import get_result

WIDTH=200;
WINDOW_WIDTH=800;
WINDOW_HEIGHT=600;
class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.text = QtWidgets.QLabel("Type a word",alignment=QtCore.Qt.AlignCenter)

        self.text_line=QtWidgets.QLineEdit()
        self.text_line.setAlignment(QtCore.Qt.AlignCenter);
        self.text_line.setFixedWidth(WIDTH);
        self.text_line.returnPressed.connect(self.show_result);

        self.button = QtWidgets.QPushButton("Click me!")
        self.button.setFixedWidth(WIDTH);

        self.result_label= QtWidgets.QLabel("😀 😀 😀 😀 😀",alignment=QtCore.Qt.AlignCenter)
        self.result_font=QtGui.QFont("Helvetica [Cronyx]", 24);
        self.result_label.setFont(self.result_font);


        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setAlignment(QtCore.Qt.AlignCenter);

        self.layout.addWidget(self.text)
        self.layout.addWidget(self.text_line, alignment=QtCore.Qt.AlignCenter)
        # self.layout.addWidget(self.button, alignment=QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.result_label)
        self.setLayout(self.layout)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))
    def show_result(self):
        if len(self.text_line.text() )==0 or len(self.text_line.text().split() )>1:
            self.result_label.setText('please write only a single word');
            return;
        res=get_result(self.text_line.text() );
        if len(res)==0:
            self.result_label.setText('No emojis found');
        else:
            self.result_label.setText(res);
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(WINDOW_WIDTH, WINDOW_HEIGHT)
    widget.show()

    sys.exit(app.exec_())