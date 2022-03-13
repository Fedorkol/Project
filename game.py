class Game:
    def __init__(self, name):
        with open(name, "r") as f:
            self.answer = []
            for line in f:
                self.answer.append(list(line.split()))
        self.width = 9
        self.height = 9
        self.board = [[0] * self.width for _ in range(self.height)]
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
        if int(self.answer[task-1][-1]) == int(ans):
            if int(self.answer[task-1][1]) >= self.price[cell[0]][cell[1]]:
                if self.scam[team-1][task-1] == 0:
                    self.count[team-1] += self.price[cell[0]][cell[1]]
                    self.scam[team-1][task-1] = 1
                    self.board[cell[0]-1][cell[1]-1] = team
                else:
                    print('Вы уже сдавади эту задачу!')
            else:
                print('Клетка, на которую вы претендуете, стоит дороже награды за данную задачу.')

if __name__ == "__main__":
    t = Game("ans.txt")
    print(t.answer)
    print(t.price)
    while True:
        r = input('Введите запрос')
        if r == '':
            break
        t.question(*map(int, r.split()))
        t.print_board()
        t.print_count()