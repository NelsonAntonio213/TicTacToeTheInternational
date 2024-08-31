import tkinter as tk
from PIL import Image, ImageTk

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.x_score = 0
        self.o_score = 0
        self.board = [None] * 9  # Initialize the board here
        self.turn = 'X'  # Initialize the turn here
        self.load_images()  # Load X and O images
        self.intro_screen()

    def load_images(self):
        # Load and resize X image
        x_image = Image.open(r"C:\Users\hanin\Desktop\Python Project Folder\Image Folder\RC.png")  # Path to X image
        x_image = x_image.resize((160, 160), Image.LANCZOS)
        self.x_image_tk = ImageTk.PhotoImage(x_image)

        # Load and resize O image
        o_image = Image.open(r"C:\Users\hanin\Desktop\Python Project Folder\Image Folder\DC.jpg")  # Path to O image
        o_image = o_image.resize((160, 160), Image.LANCZOS)
        self.o_image_tk = ImageTk.PhotoImage(o_image)

    def intro_screen(self):
        canvas = tk.Canvas(self.root, width=500, height=500)
        canvas.pack()

        img = Image.open(r"C:\Users\hanin\Desktop\Python Project Folder\Image Folder\NICE.png")  # Use the uploaded image path
        img = img.resize((500, 500), Image.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)
        canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
        canvas.img_tk = img_tk
        
        start_button = tk.Button(self.root, text="START", font=('MS Serif', 17), bg="#384031", fg="#39FF14", command=self.select_points_screen)
        canvas.create_window(250, 450, window=start_button)

    def select_points_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        canvas = tk.Canvas(self.root, width=500, height=500)
        canvas.pack()

        img = Image.open(r"C:\Users\hanin\Desktop\Python Project Folder\Image Folder\INTRO.png")  # Updated path to the second image
        img = img.resize((500, 500), Image.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)
        canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
        canvas.img_tk = img_tk

        canvas.create_text(250, 50, text="MATCH SERIES", font=("Times New Roman", 45, "bold"), fill="#39FF14")
        canvas.create_text(250, 82, text="AEGIS of Champions", font=("Great Vibes", 25, "bold"), fill="#FFFF33")

        race_to_3_button = tk.Button(canvas, text="BEST OF 5", font=('MS Serif', 15), bg="#384031", fg="#39FF14", command=lambda: self.set_points(3))
        canvas.create_window(250, 175, window=race_to_3_button)

        race_to_5_button = tk.Button(canvas, text="BEST OF 9", font=('MS Serif', 15), bg="#384031", fg="#39FF14", command=lambda: self.set_points(5))
        canvas.create_window(250, 250, window=race_to_5_button)

        race_to_7_button = tk.Button(canvas, text="BEST OF 13", font=('MS Serif', 15), bg="#384031", fg="#39FF14", command=lambda: self.set_points(7))
        canvas.create_window(250, 325, window=race_to_7_button)

    def set_points(self, points):
        self.points_to_win = points
        self.start_game()

    def start_game(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        # Background image
        background_frame = tk.Frame(self.root)
        background_frame.pack(fill="both", expand=True)

        canvas = tk.Canvas(background_frame, width=1080, height=605)
        canvas.pack(fill="both", expand=True)

        img = Image.open(r"C:\Users\hanin\Desktop\Python Project Folder\Image Folder\MAP.webp")  # Use the uploaded image path
        img = img.resize((1080, 605), Image.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)
        canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
        canvas.img_tk = img_tk

        # Scoreboard
        score_frame = tk.Frame(canvas)
        canvas.create_window(540, 30, window=score_frame)

        self.x_score_label = tk.Label(score_frame, text=f"X Points: {self.x_score}", font=('Times New Roman', 24, 'bold'), bg="#384031", fg="cyan", relief="ridge", bd=5, padx=5, pady=5)
        self.x_score_label.grid(row=0, column=1)
        
        self.o_score_label = tk.Label(score_frame, text=f"O Points: {self.o_score}", font=('Times New Roman', 24, 'bold'), bg="#384031", fg="red", relief="ridge", bd=5, padx=5, pady=5)
        self.o_score_label.grid(row=0, column=3)

        # Initialize the board and moves
        self.board = [None] * 9
        self.turn = 'X'  # Reset the turn at the start of each game
        self.x_moves = []  # Initialize the x_moves list
        self.o_moves = []  # Initialize the o_moves list
        self.grid_frame = tk.Frame(canvas, bg="#384031", relief="ridge", bd=5, padx=5, pady=5)
        canvas.create_window(540, 330, window=self.grid_frame)

        # Configure grid rows and columns
        for i in range(3):
            self.grid_frame.grid_columnconfigure(i, weight=0, minsize=176)
            self.grid_frame.grid_rowconfigure(i, weight=0, minsize=176)

        self.buttons = []
        for i in range(9):
            button = tk.Button(
                self.grid_frame,
                text="",
                image=None,  # Start with no image
                width=20,  # Set button width to fixed size in pixels
                height=11,  # Set button height to fixed size in pixels
                bd=0,  # Set border width to 0 to remove grid lines
                highlightthickness=0,  # Remove highlight/border when the button is focused
                command=lambda i=i: self.make_move(i)
            )
            button.grid(row=i // 3, column=i % 3, sticky="nsew", padx=2, pady=2)  # Added padx and pady for gaps
            self.buttons.append(button)

    def make_move(self, index):
        if self.board[index] is None:
            self.board[index] = self.turn
            if self.turn == 'X':
                self.buttons[index].config(image=self.x_image_tk, bg='cyan')  # Set X image
                self.x_moves.append(index)
                if len(self.x_moves) > 3:
                    oldest_move = self.x_moves.pop(0)
                    self.board[oldest_move] = None
                    self.buttons[oldest_move].config(image='', bg="SystemButtonFace")  # Clear image
            else:
                self.buttons[index].config(image=self.o_image_tk, bg='red')  # Set O image
                self.o_moves.append(index)
                if len(self.o_moves) > 3:
                    oldest_move = self.o_moves.pop(0)
                    self.board[oldest_move] = None
                    self.buttons[oldest_move].config(image='', bg="SystemButtonFace")  # Clear image

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
            [0, 1, 2], [3, 4, 5], [6, 7, 8], 
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  
            [0, 4, 8], [2, 4, 6]  
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] and self.board[combo[0]] is not None:
                for i in combo:
                    self.buttons[i].config(bg="#39FF14", width=20, height=11)
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
        return self.x_score >= self.points_to_win or self.o_score >= self.points_to_win

    def reset_board(self):
        for i in range(9):
            self.board[i] = None
            self.buttons[i].config(image='', bg="SystemButtonFace")
        self.turn = 'X'
        self.x_moves.clear()
        self.o_moves.clear()

    def end_game(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        # Create the end_frame and canvas first
        end_frame = tk.Frame(self.root)
        end_frame.pack(fill="both", expand=True)

        canvas = tk.Canvas(end_frame, width=500, height=500)
        canvas.pack(fill="both", expand=True)

        # Load and display the TI8-themed image as the background
        img = Image.open(r"C:\Users\hanin\Desktop\Python Project Folder\Image Folder\ENDS.png")  # Replace with your image path
        img = img.resize((500, 500), Image.LANCZOS)  # Adjust the size according to your window
        img_tk = ImageTk.PhotoImage(img)
        canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
        canvas.img_tk = img_tk  # Keep a reference to prevent garbage collection

        winner = 'X' if self.x_score >= self.points_to_win else 'O'

        # Use a large, bold font with colors reflecting the TI8 theme and center-align the text
        canvas.create_text(255, 380, text = f"{winner}", 
                            font=("Times New Roman", 100, "bold"), 
                            fill="gold")
                           
        # Themed button to restart the game
        restart_button = tk.Button(canvas, text="REINCARNATE", font=('MS Serif', 15, 'bold'), 
                                bg="#384031", fg="#39FF14", command=lambda: self.restart_game(end_frame))
        canvas.create_window(255, 477, window=restart_button)  # Adjust position as needed

    def restart_game(self, end_frame):
        end_frame.destroy()
        self.x_score = 0
        self.o_score = 0
        self.select_points_screen()

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
