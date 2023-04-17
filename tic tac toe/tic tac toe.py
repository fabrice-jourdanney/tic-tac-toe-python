import tkinter as tk

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]
        self.buttons = []
        self.create_board()

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.master, text="", width=10, height=5, command=lambda i=i, j=j: self.clicked_button(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def clicked_button(self, i, j):
        if self.board[i][j] == "":
            self.board[i][j] = self.current_player
            self.buttons[i][j].config(text=self.current_player)
            if self.check_win():
                self.show_win_message()
                self.reset_board()
            elif self.check_tie():
                self.show_tie_message()
                self.reset_board()
            else:
                self.switch_player()

    def check_win(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            elif self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def show_win_message(self):
        tk.messagebox.showinfo("Winner", f"{self.current_player} has won the game!")

    def check_tie(self):
        for row in self.board:
            if "" in row:
                return False
        return True

    def show_tie_message(self):
        tk.messagebox.showinfo("Tie Game", "The game has ended in a tie!")

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ""
                self.buttons[i][j].config(text="")
        self.current_player = "X"

    def switch_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
