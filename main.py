import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication

from circle_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_ui()
        self._should_draw = False

    def init_ui(self) -> None:
        self.create_button.clicked.connect(self._create)

    def _create(self) -> None:
        self._should_draw = True
        self.update()

    def paintEvent(self, event) -> None:
        if not self._should_draw:
            return
        qp = QPainter()
        qp.begin(self)
        self.draw_circle(qp)
        qp.end()

    def draw_circle(self, qp):
        qp.setBrush(QColor('yellow'))
        diameter = randint(70, 200)
        start = 60
        qp.drawEllipse(start, start, start + diameter, start + diameter)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
