import sys
from PyQt5.QtWidgets import QApplication, QWidget,  QLabel, QPushButton
from PyQt5.QtWidgets import QInputDialog
from PyQt5 import QtGui, QtCore
import game


TEAMS = {"A": 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
COLOR = {
    'A': 'rgb(85, 255, 0)',
    'B': 'rgb(170, 255, 127)',
    'C': 'rgb(0, 255, 0)',
    'D': 'rgb(255, 0, 0)',
    'E': 'rgb(255, 255, 0)',
    'F': 'rgb(0, 0, 255)',
    'G': 'rgb(50, 50, 50)',
    'H': 'rgb(150, 50, 50)'
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
        self.setGeometry(100, 100, 960, 760)
        self.setWindowTitle('Захватчики')
        self.cell=[]
        V = []
        H = []
        for i in range(9):
            x = []
            #Создаем вертикальные подписи
            lb = QLabel(str(i + 1), self)
            lb.setAlignment(QtCore.Qt.AlignVCenter)
            lb.setFont(QtGui.QFont('SansSerif', 12))
            lb.setStyleSheet(f'background-color: rgb(255, 255, 255);border-color:rgb(0,0,0); border-width:1px; border-style:solid;')
            lb.move(5, size * i + 5 + 20)
            lb.resize(20, size)
            V.append(lb)
            #Создаем горизонтальные подписи
            lb = QLabel(str(i + 1), self)
            lb.setAlignment(QtCore.Qt.AlignCenter)
            lb.setFont(QtGui.QFont('SansSerif', 12))
            lb.setStyleSheet(f'background-color: rgb(255, 255, 255);border-color:rgb(0,0,0); border-width:1px; border-style:solid;')
            lb.move(size * i + 20+5,5)
            lb.resize(size, 20)
            H.append(lb)

            for j in range(9):
                if self.game.board[i][j] != 0:
                    s = self.game.board[i][j]
                    style = f'background-color: {COLOR[s]};border-color:rgb(0,0,0); border-width:1px; border-style:solid;'
                else:
                    s = ''
                    style = f'background-color: rgb(255, 255, 255);border-color:rgb(0,0,0); border-width:1px; border-style:solid;'
                a = QLabel(s, self)
                a.setAlignment(QtCore.Qt.AlignTop)
                a.setFont(QtGui.QFont('SansSerif', 12))
                a.setStyleSheet(style)
                a.move(size * j + 20+5,size * i  + 20+5)
                a.resize(size, size)
                x.append(a)
            self.cell.append(x)
        self.btn = QPushButton('Сдать задачу', self)
        self.btn.setGeometry(770, 700, 100, 40)
        self.btn.clicked.connect(self.new_task)
        self.show()


    def new_task(self):
        st, ok_pressed = QInputDialog.getText(self, "Обработка запроса", "Введите запрос команды:")
        if ok_pressed:
            st = st.split()
            team = st[0].upper()
            task = int(st[1])
            ans = st[2]
            cell = st[-2:]
            self.game.question(team,task, ans, cell)
            self.on_change(*map(int,st[-2:]))

    def on_change(self, *cell):
        if self.game.board[cell[0]][cell[1]] != 0:
            s = self.game.board[cell[0]][cell[1]]
            for i in range(len(s)):
                pass
            #self.cell[cell[0]][cell[1]].setText(s)
            #self.cell[cell[0]][cell[1]].setStyleSheet(f'background-color: {COLOR["A"]};border-color:rgb(0,0,0); border-width:1px; border-style:solid;')








if __name__ == '__main__':
    app = QApplication(sys.argv)
    application = Table()
    application.show()

    application.on_change(3, 4)
    sys.exit(app.exec())