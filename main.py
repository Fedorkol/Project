import sys
from PyQt5.QtWidgets import QApplication, QWidget,  QLabel
from PyQt5.QtWidgets import QInputDialog
from PyQt5 import QtGui
TEAMS = {"A": 1, 'B': 2, 'C': 3}
COLOR = {
    'A': 'rgb(85, 255, 0)',
    'B': 'rgb(170, 255, 127)'


}
class Table(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        size = 80
        self.setGeometry(100, 100, 9 * (size+1)+1, 9 * (size+1)+1)
        self.setWindowTitle('Захватчики')
        self.cell=[]
        for i in range(9):
            x = []
            for j in range(9):
                a = QLabel('текст', self)
                a.setFont(QtGui.QFont('SansSerif', 12))
                a.setStyleSheet(f'background-color: {COLOR["B"]};')
                a.move(size * i + 10,size * j + 1)
                a.resize(80, 80)
                x.append(a)
            self.cell.append(x)
        self.show()


    def new_task(self):
        st, ok_pressed = QInputDialog.getText(self, "Обработка запроса", "Введите запрос команды:")
        if ok_pressed:
            st = st.split()
            self.on_change(*map(int,st[-2:]))

    def on_change(self, *cell):
        self.cell[cell[0]][cell[1]].setText('A 1 3\nB 1\nC 1')
        self.cell[cell[0]][cell[1]].setStyleSheet(f'background-color: {COLOR["A"]};')








if __name__ == '__main__':
    app = QApplication(sys.argv)
    application = Table()
    application.show()
    while True:
        application.new_task()
    application.on_change(3, 4)
    sys.exit(app.exec())