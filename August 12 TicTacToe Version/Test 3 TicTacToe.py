import tkinter as tk

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.x_score = 0
        self.o_score = 0
        self.intro_screen()  # Start with the intro screen

    def intro_screen(self):
        # Create the intro screen with a "Start" button
        self.intro_frame = tk.Frame(self.root)
        self.intro_frame.grid(row=0, column=1)

        intro_label = tk.Label(self.intro_frame, text="Press Start to Play", font=('normal', 24))
        intro_label.grid(row=0, column=0, pady=20)

        start_button = tk.Button(self.intro_frame, text="Start", font=('normal', 20), command=self.select_points_screen)
        start_button.grid(row=1, column=0, pady=20)

    def select_points_screen(self):
        # Ensure any previous frames are destroyed
        for widget in self.root.winfo_children():
            widget.destroy()

        # Create the points selection screen
        self.points_frame = tk.Frame(self.root)
        self.points_frame.grid(row=0, column=1)

        points_label = tk.Label(self.points_frame, text="Select Points Needed to Win", font=('normal', 24))
        points_label.grid(row=0, column=0, pady=20)

        race_to_3_button = tk.Button(self.points_frame, text="Race to 3", font=('normal', 20), command=lambda: self.set_points(3))
        race_to_3_button.grid(row=1, column=0, pady=10)

        race_to_5_button = tk.Button(self.points_frame, text="Race to 5", font=('normal', 20), command=lambda: self.set_points(5))
        race_to_5_button.grid(row=2, column=0, pady=10)

        race_to_7_button = tk.Button(self.points_frame, text="Race to 7", font=('normal', 20), command=lambda: self.set_points(7))
        race_to_7_button.grid(row=3, column=0, pady=10)

    def set_points(self, points):
        # Set the points needed to win and start the game
        self.points_to_win = points
        self.points_frame.destroy()
        self.start_game()

    def start_game(self):
        # Initialize the game board and reset scores
        self.board = [None] * 9
        self.turn = 'X'
        self.x_moves = []
        self.o_moves = []
        self.buttons = []

        # Create left and right frames for points display
        self.left_frame = tk.Frame(self.root)
        self.left_frame.grid(row=1, column=0, padx=20)

        self.right_frame = tk.Frame(self.root)
        self.right_frame.grid(row=1, column=2, padx=20)

        # Display points on the left side
        self.x_score_label = tk.Label(self.left_frame, text=f"X Points: {self.x_score}", font=('normal', 20))
        self.x_score_label.pack(pady=20)

        # Display points on the right side
        self.o_score_label = tk.Label(self.right_frame, text=f"O Points: {self.o_score}", font=('normal', 20))
        self.o_score_label.pack(pady=20)

        # Create the board in the center
        self.board_frame = tk.Frame(self.root)
        self.board_frame.grid(row=1, column=1)

        self.create_board()

    def create_board(self):
        for i in range(9):
            button = tk.Button(self.board_frame, text="", font=('normal', 40), width=5, height=2,
                               command=lambda i=i: self.make_move(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def make_move(self, index):
        if self.board[index] is None:
            self.board[index] = self.turn
            self.buttons[index].config(text=self.turn)

            if self.turn == 'X':
                self.x_moves.append(index)
                if len(self.x_moves) > 3:
                    oldest_move = self.x_moves.pop(0)
                    self.board[oldest_move] = None
                    self.buttons[oldest_move].config(text="")
            else:
                self.o_moves.append(index)
                if len(self.o_moves) > 3:
                    oldest_move = self.o_moves.pop(0)
                    self.board[oldest_move] = None
                    self.buttons[oldest_move].config(text="")

            if self.check_winner():
                self.update_score()
                if self.check_game_over():
                    self.root.after(1000, self.end_game)
                else:
                    self.root.after(1000, self.reset_board)
            else:
                self.switch_turn()

    def switch_turn(self):
        self.turn = 'O' if self.turn == 'X' else 'X'

    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]  # diagonals
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] and self.board[combo[0]] is not None:
                for i in combo:
                    self.buttons[i].config(bg="green")
                return True
        return False

    def update_score(self):
        if self.turn == 'X':
            self.x_score += 1
        else:
            self.o_score += 1
        self.x_score_label.config(text=f"X Points: {self.x_score}")
        self.o_score_label.config(text=f"O Points: {self.o_score}")

    def check_game_over(self):
        # Check if any player has reached the points needed to win
        return self.x_score >= self.points_to_win or self.o_score >= self.points_to_win

    def reset_board(self):
        for i in range(9):
            self.board[i] = None
            self.buttons[i].config(text="", bg="SystemButtonFace")
        self.turn = 'X'
        self.x_moves.clear()
        self.o_moves.clear()

    def end_game(self):
        # Destroy the game board and score display
        for widget in self.root.winfo_children():
            widget.destroy()

        # Display only the winner's message and play again button
        winner = 'X' if self.x_score >= self.points_to_win else 'O'
        end_frame = tk.Frame(self.root)
        end_frame.grid(row=0, column=0, pady=20)

        end_label = tk.Label(end_frame, text=f"{winner} Wins!", font=('normal', 24))
        end_label.grid(row=0, column=0, pady=20)

        restart_button = tk.Button(end_frame, text="Play Again", font=('normal', 20), command=lambda: self.restart_game(end_frame))
        restart_button.grid(row=1, column=0, pady=20)

    def restart_game(self, end_frame):
        # Destroy everything and return to the points selection screen
        end_frame.destroy()
        self.x_score = 0
        self.o_score = 0
        self.select_points_screen()

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
