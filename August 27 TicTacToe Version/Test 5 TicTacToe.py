import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.x_score = 0
        self.o_score = 0
        self.points_to_win = 0  # Points required to win
        self.turn = 'X'  # Initialize the turn
        self.board = [""] * 9  # Initialize the board with empty strings for moves
        self.buttons = [None] * 9  # Keep track of the button references
        self.move_history = []  # Track move history
        self.intro_screen()  # Start with the introduction screen

    def intro_screen(self):
        # Create introduction screen
        canvas = tk.Canvas(self.root, width=600, height=650)
        canvas.pack()

        img = Image.open(r"C:\Users\hanin\Desktop\Python Project Folder\Image Folder\NICE.png")
        img = img.resize((600, 650), Image.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)
        canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
        canvas.img_tk = img_tk

        start_button = tk.Button(self.root, text="START", font=('MS Serif', 17), bg="#384031", fg="#39FF14", command=self.select_points_screen)
        canvas.create_window(300, 600, window=start_button)

    def select_points_screen(self):
        # Clear screen and show point selection
        for widget in self.root.winfo_children():
            widget.destroy()

        canvas = tk.Canvas(self.root, width=1080, height=650)
        canvas.pack()

        img = Image.open(r"C:\Users\hanin\Desktop\Python Project Folder\Image Folder\MAP.webp")
        img = img.resize((1080, 650), Image.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)
        canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
        canvas.img_tk = img_tk
        
        canvas.create_text(540, 100, text="MATCH SERIES", font=("Times New Roman", 80, "bold"), fill="#69983a")
        canvas.create_text(540, 150, text="AEGIS of Champions", font=("Great Vibes", 40, "bold"), fill="white")

        race_to_3_button = tk.Button(canvas, text="BEST OF 5", font=('MS Serif', 20), bg="#384031", fg="#39FF14", command=lambda: self.set_points(3))
        canvas.create_window(540, 300, window=race_to_3_button)

        race_to_5_button = tk.Button(canvas, text="BEST OF 9", font=('MS Serif', 20), bg="#384031", fg="#39FF14", command=lambda: self.set_points(5))
        canvas.create_window(540, 400, window=race_to_5_button)

        race_to_7_button = tk.Button(canvas, text="BEST OF 13", font=('MS Serif', 20), bg="#384031", fg="#39FF14", command=lambda: self.set_points(7))
        canvas.create_window(540, 500, window=race_to_7_button)

    def set_points(self, points):
        # Set points to win and create the game board
        self.points_to_win = points
        self.x_score = 0
        self.o_score = 0
        self.create_board()

    def create_board(self):
        # Clear screen and initialize the Tic Tac Toe board
        for widget in self.root.winfo_children():
            widget.destroy()

        self.board = [""] * 9
        self.move_history = []
        self.turn = 'X'
        self.buttons = []

        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text="", font=('Courier New', 20, 'bold'), width=5, height=2, bg="#1a1a1a", fg="#00FF00", activebackground="#333333", activeforeground="#00FF00", command=lambda idx=i*3+j: self.on_button_click(idx))
                button.grid(row=i, column=j, padx=5, pady=5)
                button.bind("<Enter>", lambda event, b=button: b.config(bg="#00FF00"))
                button.bind("<Leave>", lambda event, b=button: b.config(bg="#1a1a1a"))
                self.buttons.append(button)

        self.update_score()

    def on_button_click(self, index):
        if self.board[index] == "":
            self.board[index] = self.turn
            self.buttons[index].config(text="❌" if self.turn == 'X' else "⭕")

            self.move_history.append((index, self.turn))

            if len([m for i, m in self.move_history if m == self.turn]) > 3:
                self.remove_oldest_move(self.turn)

            if self.check_winner():
                self.update_scoreboard()
                if self.check_match_winner():
                    return
                else:
                    self.reset_board()
            else:
                self.switch_turn()

    def remove_oldest_move(self, turn):
        for i, (index, player) in enumerate(self.move_history):
            if player == turn:
                self.move_history.pop(i)
                self.board[index] = ""
                self.buttons[index].config(text="")
                break

    def switch_turn(self):
        self.turn = 'O' if self.turn == 'X' else 'X'

    def check_winner(self):
        # Check for a winner
        lines = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
            [0, 4, 8], [2, 4, 6]              # Diagonal
        ]
        for line in lines:
            if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] != "":
                return True
        return False

    def update_scoreboard(self):
        # Update scores based on the winner
        if self.turn == 'X':
            self.x_score += 1
        else:
            self.o_score += 1
        self.update_score()

    def update_score(self):
        # Display scores
        score_label = tk.Label(self.root, text=f"X: {self.x_score} - O: {self.o_score}", font=('MS Serif', 15), fg="#00FF00", bg="#1a1a1a")
        score_label.grid(row=3, column=0, columnspan=3)

    def reset_board(self):
        # Reset the board for a new round
        self.board = [""] * 9
        self.move_history = []
        for button in self.buttons:
            button.config(text="")

    def check_match_winner(self):   
        # Check if someone won the match series
        if self.x_score == self.points_to_win:
            messagebox.showinfo("Congratulations", "Player X wins the match!")
            self.select_points_screen()
            return True
        elif self.o_score == self.points_to_win:
            messagebox.showinfo("Congratulations", "Player O wins the match!")
            self.select_points_screen()
            return True
        return False

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
