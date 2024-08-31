import tkinter as tk
from PIL import Image, ImageTk
import tkinter.messagebox as MessageBox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.x_score = 0
        self.o_score = 0
        self.board = [None] * 9  # Initialize the board
        self.turn = 'X'  # Initialize the turn
        self.intro_screen()

    def intro_screen(self):
        self.clear_screen()
        canvas = tk.Canvas(self.root, width=600, height=650)
        canvas.pack()

        img = Image.open(r"C:\Users\hanin\Desktop\Python Project Folder\Image Folder\NICE.png")  # Update with your image path
        img = img.resize((600, 650), Image.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)
        canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
        canvas.img_tk = img_tk

        start_button = tk.Button(self.root, text="START", font=('MS Serif', 17), bg="#384031", fg="#39FF14", command=self.select_points_screen)
        canvas.create_window(300, 600, window=start_button)

    def select_points_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        canvas = tk.Canvas(self.root, width=1080, height=650)
        canvas.pack()

        img = Image.open(r"C:\Users\hanin\Desktop\Python Project Folder\Image Folder\MAP.webp")  # Updated path to the second image
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

        self.points_frame = tk.Frame(self.root)
        self.points_frame.grid(row=0, column=0, padx=20, pady=20)
        
    def set_points(self, points):
        self.points_to_win = points
        self.points_frame.destroy()
        self.start_game()

    def start_game(self):
        self.clear_screen()
        self.board = [None] * 9
        self.turn = 'X'

        self.buttons = []
        self.game_frame = tk.Frame(self.root)
        self.game_frame.grid(row=0, column=0, padx=20, pady=20)

        for i in range(9):
            button = tk.Button(self.game_frame, text='', font=('normal', 40), width=5, height=2, command=lambda i=i: self.make_move(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

        self.update_status()

    def make_move(self, index):
        if self.board[index] is None:
            self.board[index] = self.turn
            self.buttons[index].config(text=self.turn)
            if self.check_winner():
                MessageBox.showinfo("Game Over", f"Player {self.turn} wins!")
                if self.turn == 'X':
                    self.x_score += 1
                else:
                    self.o_score += 1
                self.update_status()
                self.start_game()
            elif None not in self.board:
                MessageBox.showinfo("Game Over", "It's a tie!")
                self.update_status()
                self.start_game()
            else:
                self.turn = 'O' if self.turn == 'X' else 'X'
                self.update_status()

    def check_winner(self):
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)              # Diagonals
        ]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] and self.board[condition[0]] is not None:
                return True
        return False

    def update_status(self):
        status = f"Player X: {self.x_score} - Player O: {self.o_score}\nCurrent Turn: {self.turn}"
        if hasattr(self, 'status_label'):
            self.status_label.config(text=status)
        else:
            self.status_label = tk.Label(self.root, text=status, font=('normal', 16))
            self.status_label.grid(row=1, column=0, pady=10)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
