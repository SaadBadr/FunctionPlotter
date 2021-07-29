# ------------------ PySide2 - Qt Designer - Matplotlib ------------------
from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile

from matplotlib.backends.backend_qt5agg import (
    FigureCanvas, NavigationToolbar2QT as NavigationToolbar)

from matplotlib.figure import Figure

from mathParse import MathExpression
import matplotlib.pyplot as plt
import numpy as np


# ------------------ MplWidget ------------------


class MplWidget(QWidget):

    def __init__(self, parent=None):

        QWidget.__init__(self, parent)

        self.canvas = FigureCanvas(Figure())

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        vertical_layout.addWidget(NavigationToolbar(self.canvas, self))

        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)

# ------------------ MainWidget ------------------


class MainWidget(QWidget):

    def __init__(self):

        QWidget.__init__(self)

        designer_file = QFile("t.ui")
        designer_file.open(QFile.ReadOnly)

        loader = QUiLoader()
        loader.registerCustomWidget(MplWidget)
        self.ui = loader.load(designer_file, self)

        designer_file.close()

        self.ui.pushButton_plot.clicked.connect(
            self.update_graph)

        self.setWindowTitle("Funtion Plotter v1")

        grid_layout = QGridLayout()
        grid_layout.addWidget(self.ui)
        self.setLayout(grid_layout)

    def update_graph(self):
        exp_text = self.ui.lineEdit_function.text()

        min = self.ui.spinBox_min.value()
        max = self.ui.spinBox_max.value()

        x = np.linspace(min, max, 300)
        exp = MathExpression(exp_text, x)

        self.ui.MplWidget.canvas.axes.clear()
        self.ui.MplWidget.canvas.axes.plot(x, exp.y)
        self.ui.MplWidget.canvas.draw()


app = QApplication([])
window = MainWidget()
window.show()
app.exec_()
