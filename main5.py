# Here is an updated version of the code that includes a score reset button:

# ```python
import tkinter as tk

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.player_turn = "X"
        self.score = {"X": 0, "O": 0}
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_widgets()
        self.window.mainloop()

    def create_widgets(self):
        self.label = tk.Label(self.window, text="Player X's turn", font=("Arial", 24))
        self.label.grid(row=0, column=0, columnspan=3)

        for i in range(3):
            for j in range(3):
                # self.buttons[i][j] = tk.Button(self.window, text="", font=("Arial", 24), width=5, height=2,
                #                                command=lambda row=i, col=j: self.button_click(row, col))
                self.buttons[i][j] = tk.Button(self.window, text="", font=("Arial", 40), width=6, height=2,
                               command=lambda row=i, col=j: self.button_click(row, col), padx=0, pady=0)
                self.buttons[i][j].grid(row=i+1, column=j)

        self.score_label = tk.Label(self.window, text="Score: X - 0 | O - 0", font=("Arial", 24))
        self.score_label.grid(row=4, column=0, columnspan=3)

        self.replay_button = tk.Button(self.window, text="Replay",  bg='#24f254',font=("Arial", 24), command=self.replay)
        self.replay_button.grid(row=5, column=0)

        self.reset_button = tk.Button(self.window, text="Reset Score",bg='#ba2409' ,font=("Arial", 24), command=self.reset_score)
        self.reset_button.grid(row=5, column=2)

    def button_click(self, row, col):
        if not self.buttons[row][col]["text"]:
            self.buttons[row][col]["text"] = self.player_turn
            if self.player_turn == "X":
                self.buttons[row][col]["fg"] = "red"
            else:
                self.buttons[row][col]["fg"] = "blue"
            if self.check_winner():
                for i in range(3):
                    for j in range(3):
                        self.buttons[i][j]["state"] = "disabled"
                self.label["text"] = f"Player {self.player_turn} wins!"
                self.score[self.player_turn] += 1
                self.update_score()
            elif not any([self.buttons[i][j]["text"] == "" for i in range(3) for j in range(3)]):
                self.label["text"] = "It's a tie!"
            else:
                self.player_turn = "O" if self.player_turn == "X" else "X"
                self.label["text"] = f"Player {self.player_turn}'s turn"

    def check_winner(self):
        for i in range(3):
            if all([self.buttons[i][j]["text"] == self.player_turn for j in range(3)]):
                return True
            if all([self.buttons[j][i]["text"] == self.player_turn for j in range(3)]):
                return True
        if all([self.buttons[i][i]["text"] == self.player_turn for i in range(3)]):
            return True
        if all([self.buttons[i][2-i]["text"] == self.player_turn for i in range(3)]):
            return True
        return False

    def update_score(self):
        self.score_label["text"] = f"Score: X - {self.score['X']} | O - {self.score['O']}"

    def replay(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = ""
                self.buttons[i][j]["state"] = "normal"
                self.buttons[i][j]["fg"] = "black"
        self.player_turn = "X"
        self.label["text"] = f"Player {self.player_turn}'s turn"

    def reset_score(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = ""
                self.buttons[i][j]["state"] = "normal"
                self.buttons[i][j]["fg"] = "black"
        self.score["X"] = 0
        self.score["O"] = 0
        self.update_score()
        self.player_turn = "X"
        self.label["text"] = f"Player {self.player_turn}'s turn"

if __name__ == "__main__":
    TicTacToe()
# ```
# This code creates a Tic Tac Toe game