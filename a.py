import tkinter as tk
from tkinter import messagebox
import time


class ChronometerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Kronometre")
        self.master.configure(bg='#2E2E2E')

        self.label_time = tk.Label(master, text="Süre girin:", bg='#2E2E2E', fg='white')
        self.label_time.pack()

        self.entry_time = tk.Entry(master, bg='#2E2E2E', fg='white')
        self.entry_time.pack()

        self.start_button = tk.Button(master, text="Kronometreyi Başlat", command=self.start_chronometer,bg='#404040', fg='white')
        self.start_button.pack()

        self.label_teams = tk.Label(master, text="Puanlar", bg='#2E2E2E', fg='white')
        self.label_teams.pack()

        self.team_scores = [0, 0, 0, 0, 0]

        self.team_labels = []
        self.team_buttons_plus = []
        self.team_buttons_minus = []

        for i in range(5):
            frame = tk.Frame(master, bg='#2E2E2E')
            frame.pack()

            label = tk.Label(frame, text=f"Takım {i + 1}", bg='#2E2E2E', fg='white')
            label.pack(side=tk.LEFT)

            button_minus = tk.Button(frame, text="-", command=lambda idx=i: self.update_score(idx, -10), bg='#404040', fg='white')
            button_minus.pack(side=tk.LEFT)

            score_label = tk.Label(frame, text=str(self.team_scores[i]), bg='#2E2E2E', fg='white')
            score_label.pack(side=tk.LEFT)

            button_plus = tk.Button(frame, text="+", command=lambda idx=i: self.update_score(idx, 10), bg='#404040', fg='white')
            button_plus.pack(side=tk.LEFT)
            self.team_labels.append(score_label)
            self.team_buttons_plus.append(button_plus)
            self.team_buttons_minus.append(button_minus)

    def start_chronometer(self):
        try:
            target_time = float(self.entry_time.get())
        except ValueError:
            messagebox.showerror("Hata", "Lütfen geçerli bir süre girin.")
            return

        self.label_time.config(text="Kronometre çalışıyor...")
        self.start_button.config(state=tk.DISABLED)

        start_time = time.time()

        while True:
            elapsed_time = time.time() - start_time


            if elapsed_time >= target_time:
                messagebox.showinfo("Süre doldu", "Süre doldu.")
                break


            self.label_time.config(text=f"Geçen zaman: {elapsed_time:.2f} saniye")


            self.master.update()


            time.sleep(0.01)


        self.label_time.config(text="Süre girin:")
        self.start_button.config(state=tk.NORMAL)

    def update_score(self, team_index, delta):
        self.team_scores[team_index] += delta
        self.team_labels[team_index].config(text=str(self.team_scores[team_index]))

if __name__ == "__main__":
    root = tk.Tk()
    app = ChronometerApp(root)
    root.mainloop()
