import random

def wisielec(word):
    wrong = 0
    stages = [' _______     ',
              '|       |    ',
              '|       |    ',
              '|       o    ',
              '|       |    ',
              '|      /|\   ',
              '|       |    ',
              '|      / \   ',
              '|            ']
    letters = list(word)
    board = ['_'] * len(word)
    win = False
    print((" ").join(board))

    while wrong < len(stages):
        guess = (input("Zgadnij litere > ")).lower()
        if guess in letters:
            indices = letters.count(guess)
            for i in range(indices):
                indeks = letters.index(guess)
                board[indeks] = letters[indeks]
                letters[indeks] = '$'
            print("Corect!")
        else:
            wrong += 1
            print("Wrong!")
        print()
        print("\n".join(stages[0:(wrong)]))
        print()
        print(" ".join(board))
        if '_' not in board:
            win = True
            print("Wygrales!")
            break

words = ['kotek','krowa','mucha','zul','smietnik','zuledwa','smietniki']
word = words[random.randint(0,len(words)-1)]


# Running the game
wisielec(word)
