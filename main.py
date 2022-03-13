import sys
from PyQt5.QtWidgets import QApplication, QWidget,  QLabel
from PyQt5.QtWidgets import QInputDialog
from PyQt5 import QtGui
import game


TEAMS = {"A": 1, 'B': 2, 'C': 3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8}
COLOR = {
    'A': 'rgb(85, 255, 0)',
    'B': 'rgb(170, 255, 127)',
    'C': 'rgb(0, 255, 0)',
    'D': 'rgb(255, 0, 0)',
    'E': 'rgb(255, 255, 0)',
    'G': 'rgb(0, 0, 255)',
    'H': 'rgb(50, 50, 50)'
}


class Table(QWidget):

    def __init__(self):
        super().__init__()
        self.game = game.Game("ans.txt")
        self.game.board[0][2] = 'A'
        self.game.board[0][6] = 'B'
        self.game.board[2][0] = 'H'
        self.game.board[6][0] = 'G'
        self.game.board[8][2] = 'F'
        self.game.board[8][6] = 'E'
        self.game.board[2][8] = 'C'
        self.game.board[6][8] = 'D'
        self.initUI()


    def initUI(self):
        size = 80
        self.setGeometry(100, 100, 9 * (size+1)+1, 9 * (size+1)+1)
        self.setWindowTitle('Захватчики')
        self.cell=[]
        for j in range(9):
            x = []
            for i in range(9):
                if self.game.board[i][j] != 0:
                    s = self.game.board[i][j]
                else:
                    s = '0'
                a = QLabel(s, self)
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