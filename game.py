class Game:
    def __init__(self, name):
        with open(name, "r") as f:
            self.answer = []
            for line in f:
                self.answer.append(list(line.split()))
        self.width = 9
        self.height = 9
        self.board = [[0] * self.width for _ in range(self.height)]
        self.board[0][2] = 1
        self.board[0][6] = 2
        self.board[2][0] = 8
        self.board[6][0] = 7
        self.board[8][2] = 6
        self.board[8][6] = 5
        self.board[2][8] = 3
        self.board[6][8] = 4
        self.count = [0] * 9
        self.price = [[5, 3, 0, 3, 5, 3, 0, 3, 5], [3, 5, 3, 3, 5, 3, 3, 5, 3], [0, 3, 5, 3, 5, 3, 5, 3, 0], [3, 3, 3, 8, 11, 8, 3, 3, 3], [5, 5, 5, 11, 15, 11, 5, 5, 5], [3, 3, 3, 8, 11, 8, 3, 3, 3], [0, 3, 5, 3, 5, 3, 5, 3, 0],  [3, 5, 3, 3, 5, 3, 3, 5, 3], [5, 3, 0, 3, 5, 3, 0, 3, 5]]
        self.scam = [[0]*30]*8


    def print_count(self):
        for i in range(8):
            print('Team', i + 1, self.count[i])


    def print_board(self):
        for i in range(9):
            print(*self.board[i])


    def question(self, team, task,  ans, *cell):
        q = False
        if int(self.answer[task-1][-1]) == int(ans):
            if int(self.answer[task-1][1]) >= self.price[cell[0]][cell[1]]:
                if self.scam[team-1][task-1] == 0:
                    if cell != (0, 2) and cell != (0, 6) and cell != (2, 0) and cell != (6, 0):
                        if cell != (8, 2) and cell != (8, 6) and cell != (2, 8) and cell != (6, 8):
                            if cell == (0, 0) and (self.board[0][1] == team or self.board[1][0] == team):
                                #print(1)
                                q = True
                            elif cell == (0, 8) and (self.board[0][7] == team or self.board[1][8] == team):
                                #print(2)
                                q = True
                            elif cell == (8, 0) and (self.board[7][0] == team or self.board[8][1] == team):
                                #print(3)
                                q = True
                            elif cell == (8, 8) and (self.board[8][7] == team or self.board[7][8] == team):
                                #print(4)
                                q = True
                            elif cell[0] == 0 and (self.board[0][cell[1]-1] == team or self.board[0][cell[1]+1] == team or self.board[1][cell[1]] == team):
                                #print(5)
                                q = True
                            elif cell[0] == 8 and (self.board[8][cell[1]-1] == team or self.board[8][cell[1]+1] == team or self.board[7][cell[1]] == team):
                                #print(6)
                                q = True
                            elif cell[1] == 0 and (self.board[cell[0]+1][0] == team or self.board[cell[0]-1][0] == team or self.board[cell[0]][1] == team):
                                #print(7)
                                q = True
                            elif cell[1] == 8 and (self.board[cell[0]+1][8] == team or self.board[cell[0]-1][8] == team or self.board[cell[0]][7] == team):
                                #print(8)
                                q = True
                            elif cell[0] != 0 and cell[0] != 8 and cell[1] != 0 and cell[1] != 8:
                                if self.board[cell[0]+1][cell[1]+1] == team or self.board[cell[0]+1][cell[1]] == team or self.board[cell[0]][cell[1]+1] == team or self.board[cell[0]][cell[1]] == team:
                                    #print(9)
                                    q = True
                                else:
                                    print('Данная клетка не граничит с уже имеющимися у вас клетками и её нельзя захватить.')
                            else:
                                print('Данная клетка не граничит с уже имеющимися у вас клетками и её нельзя захватить.')
                            if q:
                                self.count[team-1] += self.price[cell[0]][cell[1]]
                                self.scam[team-1][task-1] = 1
                                self.board[cell[0]][cell[1]] = team
                        else:
                            print('Данная клетка является базой команды и её нельзя захватить.')
                    else:
                        print('Данная клетка является базой команды и её нельзя захватить.')
                else:
                    print('Вы уже сдавали эту задачу!')
            else:
                print('Клетка, на которую вы претендуете, стоит дороже награды за данную задачу и её нельзя захватить.')
        else:
            print('Ваш ответ неправильный.')


if __name__ == "__main__":
    t = Game("ans.txt")
    while True:
        r = input('Введите запрос (номер команды, номер задания, ваш ответ, координаты клетки):')
        if r == '':
            break
        r = list(map(int, r.split()))
        r[-2] -= 1
        r[-1] -= 1
        t.question(*r)
        t.print_board()
        t.print_count()