class Game(object):
    cells = [0,1,2,3,4,5,6,7,8]
    def put(self, where, what):
        self.cells[where] = what
    def show(self):
        for y in range(3):
            print(self.cells[3*y], self.cells[3*y+1], self.cells[3*y+2], sep=" | ")
            if(y < 2):
                print("-"*9)
    def ask(self, which):
        user_n = input(f'{which}-player, choose a cell for your move and write its number\n')
        try:
           n = int(user_n) 
        except ValueError:
            print("Please, write an integer number")
            return self.ask(which)
        if(n < 0 or n > 8):
            print("Your number should be between 0 and 8")
            return self.ask(which)
        if self.cells[n] == "O" or self.cells[n] == "X":
            print("This cell has already taken. Try another one")
            return self.ask(which)
        self.put(n,which)

    def result(self):

        if self.cells[0] == self.cells[1] == self.cells[2]:
            return f"{self.cells[0]}-player wins"
        if self.cells[3] == self.cells[4] == self.cells[5]:
            return f"{self.cells[3]}-player wins"
        if self.cells[6] == self.cells[7] == self.cells[8]:
            return f"{self.cells[6]}-player wins"

        if self.cells[0] == self.cells[3] == self.cells[6]:
            return f"{self.cells[0]}-player wins"
        if self.cells[1] == self.cells[4] == self.cells[7]:
            return f"{self.cells[1]}-player wins"
        if self.cells[2] == self.cells[5] == self.cells[8]:
            return f"{self.cells[2]}-player wins"

        if self.cells[0] == self.cells[4] == self.cells[8]:
            return f"{self.cells[0]}-player wins"
        if self.cells[2] == self.cells[4] == self.cells[6]:
            return (f'{self.cells[2]}-player wins')

        if any(map(lambda x : isinstance(x, int), self.cells)):
            return "not end"
        return "Draw"

    def play(self):
        whose_turn = "X"
        while self.result() == "not end":
            self.show()
            self.ask(whose_turn)
            if whose_turn == "X":
                whose_turn = "O"
            else:
                whose_turn = "X"
        self.show()
        print(self.result())

# first_game = Game()
# first_game.play()


