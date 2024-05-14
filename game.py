class State:
    def __init__(self):
        self.allNodesValues = {}

    def bestMove(self, s):
        if self.player(s) == 'X':
            best_val = self.maxValue(s)
        elif self.player(s) == 'O':
            best_val = self.minValue(s)
        best_moveStr = None
        best_move = None
        if not self.action(s):
            return s
        else:
            for item in self.action(s):
                child = self.result(s, item)
                childStr = ' '.join(str(e) for e in child)
                for elem in self.allNodesValues:
                    if elem == childStr and self.allNodesValues[elem] == best_val:
                        best_moveStr = elem
                        best_move = list(best_moveStr.split(' '))

                        break
            for i in range(9):
                best_move[i] = None if best_move[i] == 'None' else best_move[i]
            return best_move

    def player(self, s):
        total_X = s.count('X')
        total_O = s.count("O")
        if total_X > total_O:
            return 'O'
        else:
            return 'X'

    def action(self, s):
        a = []
        for i in range(9):
            if s[i] == None:
                a.append(i)
        return a

    def result(self, s, a):
        r = s[:]
        if self.player(s) == 'X':
            r[a] = 'X'
        else:
            r[a] = 'O'
        return r

    def terminal(self, s):
        if ((s[0] == s[1] == s[2] != None) or (s[3] == s[4] == s[5] != None) or (s[6] == s[7] == s[8] != None) or (s[0] == s[3] == s[6] != None) or (s[1] == s[4] == s[7] != None) or (s[2] == s[5] == s[8] != None) or (s[0] == s[4] == s[8] != None) or (s[2] == s[4] == s[6] != None)):
            return True
        else:
            return False

    def utility(self, s):
        if self.player(s) == 'O' and self.terminal(s) == True:
            return 1
        elif self.player(s) == 'X' and self.terminal(s) == True:
            return -1
        elif not self.action(s):
            return 0

    def maxValue(self, s):
        self.allNodesValues
        if self.terminal(s) or not self.action(s):
            self.allNodesValues.update({' '.join(str(e)
                                                 for e in s): self.utility(s)})
            return self.utility(s)
        v = -99
        for act in self.action(s):
            v = max(v, self.minValue(self.result(s, act)))
        self.allNodesValues.update({' '.join(str(e) for e in s): v})
        return v

    def minValue(self, s):
        self.allNodesValues
        if self.terminal(s) or not self.action(s):
            self.allNodesValues.update({' '.join(str(e)
                                                 for e in s): self.utility(s)})
            return self.utility(s)
        v = 99
        for act in self.action(s):
            v = min(v, self.maxValue(self.result(s, act)))
        self.allNodesValues.update({' '.join(str(e) for e in s): v})
        return v


def printCurrentBoard(l):
    a = [l[i:i+3] for i in range(0, len(l), 3)]
    for i in range(3):
        for j in range(3):
            if a[i][j] == None:
                print(" ", end=" ")
            else:
                print(a[i][j], end=" ")
        print()


state_1 = State()
gameBoard = [None, None, None, None, None, None, None, None, None]
while not state_1.terminal(gameBoard) and state_1.action(gameBoard):
    position = int(input("Enter the position you want to play [1 - 9]: "))
    if position < 1 or position > 9:
        print("ERROR!! Position not on the board")
    elif gameBoard[position - 1] == None:
        gameBoard[position -
                  1] = 'X' if state_1.player(gameBoard) == 'X' else 'O'
        gameBoard = state_1.bestMove(gameBoard)
        printCurrentBoard(gameBoard)
    else:
        print("WARNING!! Position already played")
        continue
if state_1.utility(gameBoard) == 1:
    print("!! X Won !!")
elif state_1.utility(gameBoard) == -1:
    print("!! O Won !!")
else:
    print("!! Draw !!")
