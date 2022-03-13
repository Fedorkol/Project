import sys
from PyQt5.QtWidgets import QApplication, QWidget,  QLabel, QPushButton
from PyQt5.QtWidgets import QInputDialog
from PyQt5 import QtGui, QtCore
import game


TEAMS = list('ABCDEFGH')
COLOR = {
    'A': 'rgb(220,20,60)',
    'B': 'rgb(255,140,0)',
    'C': 'rgb(255,215,0)',
    'D': 'rgb(0,250,154)',
    'E': 'rgb(135,206,250)',
    'F': 'rgb(70,130,180)',
    'G': 'rgb(128,0,128)',
    'H': 'rgb(255,105,180)'
}



class Table(QWidget):

    def __init__(self):
        super().__init__()

        self.game = game.Game("ans.txt")
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
                    s = TEAMS[self.game.board[i][j] - 1]
                    style = f'background-color: {COLOR[s]};border-color:rgb(0,0,0); border-width:1px; border-style:solid;'
                else:
                    s = ' ' * 8 + str(self.game.price[i][j])
                    lev = 255 - self.game.price[i][j] * 10
                    style = f'background-color: rgb({lev}, {lev}, {lev});border-color:rgb(0,0,0); border-width:1px; border-style:solid;'
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
                if type(s) == list:
                    _s = []
                    for el in s:
                        _s.append(TEAMS[int(el[0] - 1)] +' '+ str(el[1]))
                    _s[0] = _s[0] + ' ' * 4 + str(self.game.price[cell[0]][cell[1]])
            self.cell[cell[0]][cell[1]].setText('\n'.join(_s))
            self.cell[cell[0]][cell[1]].setStyleSheet(f'background-color: {COLOR[TEAMS[s[0][0] - 1]]};border-color:rgb(0,0,0); border-width:1px; border-style:solid;')








if __name__ == '__main__':
    app = QApplication(sys.argv)
    application = Table()
    application.show()
    application.game.board[0][1]=[(1, 1)]
    application.on_change(0,1)
    application.game.board[3][2] = [(4, 1), (8,1), (7,1)]
    application.on_change(3, 2)
    application.game.board[4][4] = [(1, 2), (6,2)]
    application.on_change(4, 4)
    sys.exit(app.exec())