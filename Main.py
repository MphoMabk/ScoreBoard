import tkinter as tk

# HomeInput=input(" enter home team")


class Scoreboard(tk.Frame):
    def __init__(self, master=None):
        
        super().__init__(master)
        
        self.home_score = 0
        self.away_score = 0
        root.title("Team A vs Team B") 
        

        self.home_label = tk.Label(self, text="Home-Team", font=("DS-Digital", 24))
        self.home_label.grid(row=0, column=0)
        self.home_score_label = tk.Label(self, text="0", font=("Digital-7", 24))
        self.home_score_label.grid(row=1, column=0)
        self.home_button = tk.Button(self, text="Add Point", command=self.add_home_point)
        self.home_button.grid(row=2, column=0)
        
        self.away_label = tk.Label(self, text="Away", font=("Arial", 24))
        self.away_label.grid(row=0, column=2)
        self.away_score_label = tk.Label(self, text="0", font=("Arial", 24))
        self.away_score_label.grid(row=1, column=2)
        inputn = input("what must i do")
        if inputn == "add":
            self.add_away_point
        self.away_button = tk.Button(self, text="Add Point", command=self.add_away_point)
        self.away_button.grid(row=2, column=2)
        
        self.quit_button = tk.Button(self, text="Quit", command=self.quit)
        self.quit_button.grid(row=3, column=1)
        
        self.pack()
        
    def add_home_point(self):
        self.home_score += 1
        self.home_score_label.config(text=str(self.home_score))
        
    def add_away_point(self):
        self.away_score += 1
        self.away_score_label.config(text=str(self.away_score))
        
root = tk.Tk()
scoreboard = Scoreboard(root)
root.mainloop()
