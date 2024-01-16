    import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import time

class ChronometerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("QuizShow")
        self.master.configure(bg='#2E2E2E')

        self.master.geometry("800x600")

        # Görseli yükle
        image = Image.open("alis.png")  
        image = image.resize((150, 150))  
        self.photo = ImageTk.PhotoImage(image)

        # Görsel
        self.image_label = tk.Label(master, image=self.photo, bg='#2E2E2E')
        self.image_label.place(x=40, y=40) 
        
        self.amal_label = tk.Label(master, text="AMAL Yazılım Geliştirme Ekibi", font=("Arial", 12), bg='#2E2E2E', fg='#30D5C8')
        self.amal_label.place(x=20, y=200)  # Konum

        self.amal_label = tk.Label(master, text="QUIZ SHOW", font=("Impact", 25), bg='#2E2E2E', fg='white')
        self.amal_label.place(x=20, y=250)

        self.label_time = tk.Label(master, text="Süre girin:", bg='#2E2E2E', fg='white')
        self.label_time.pack()

        # Timer girişi
        self.entry_time = tk.Entry(master, bg='#2E2E2E', fg='white')
        self.entry_time.pack()

        # Geri sayım
        self.countdown_frame = tk.Frame(master, bg='#404040')
        self.countdown_frame.pack(side=tk.TOP, pady=(10, 0))
        self.countdown_var = tk.StringVar()
        self.countdown_label = tk.Label(self.countdown_frame, textvariable=self.countdown_var, font=("Arial", 24), bg='#2E2E2E', fg='white')
        self.countdown_label.pack()

        # Başlat
        self.start_button = tk.Button(master, text="Kronometreyi Başlat", command=self.start_chronometer, bg='#404040', fg='white', height=3, width=30)
        self.start_button.pack(side=tk.LEFT, padx=(10, 0), pady=(0, 10))

        # Sıfırla
        self.reset_button = tk.Button(master, text="Sıfırla", command=self.reset_chronometer, bg='red', fg='white', height=3, width=15)
        self.reset_button.pack(side=tk.LEFT, padx=(0, 10), pady=(0, 10))
        self.reset_button.config(state=tk.DISABLED)

        self.label_teams = tk.Label(master, text="Puanlar", bg='#2E2E2E', fg='white')
        self.label_teams.pack()
        
        self.label_point_change = tk.Label(master, text="Puan Değişim Miktarı:", bg='#2E2E2E', fg='white')
        self.label_point_change.pack()

        self.entry_point_change = tk.Entry(master, bg='#2E2E2E', fg='white')
        self.entry_point_change.pack()

        self.team_scores = [0, 0, 0, 0, 0]

        self.team_labels = []
        self.team_buttons_plus = []
        self.team_buttons_minus = []

        for i in range(5):
            frame = tk.Frame(master, bg='#2E2E2E')
            frame.pack(pady=10)  

            label = tk.Label(frame, text=f"Takım {i + 1}", bg='#2E2E2E', fg='white')
            label.pack(side=tk.LEFT)

            button_minus = tk.Button(frame, text="-", command=lambda idx=i: self.update_score(idx, -self.get_point_change()), bg='#404040', fg='white', height=2, width=5)
            button_minus.pack(side=tk.LEFT)
            
            score_label = tk.Label(frame, text=str(self.team_scores[i]), bg='#2E2E2E', fg='white')
            score_label.pack(side=tk.LEFT)

            button_plus = tk.Button(frame, text="+", command=lambda idx=i: self.update_score(idx, self.get_point_change()), bg='#404040', fg='white', height=2, width=5)
            button_plus.pack(side=tk.LEFT)

            self.team_labels.append(score_label)
            self.team_buttons_plus.append(button_plus)
            self.team_buttons_minus.append(button_minus)

        self.running = False

    def start_chronometer(self):
        if not self.running:
            try:
                target_time = float(self.entry_time.get())
            except ValueError:
                messagebox.showerror("Hata", "Lütfen geçerli bir süre girin.")
                return

            self.label_time.config(text="Kronometre çalışıyor...")
            self.start_button.config(state=tk.DISABLED)
            self.reset_button.config(state=tk.NORMAL)

            start_time = time.time()
            self.running = True  

            while self.running:
                elapsed_time = time.time() - start_time
                remaining_time = max(0, target_time - elapsed_time)

                if remaining_time == 0:
                    messagebox.showinfo("Süre doldu", "Süre doldu.")
                    self.running = False  
                    break

                self.countdown_var.set(f"Kalan süre: {remaining_time:.2f} saniye")
                self.master.update()

                time.sleep(0.01)

            self.label_time.config(text="Süre girin:")
            self.start_button.config(state=tk.NORMAL)
            self.reset_button.config(state=tk.DISABLED)
            self.countdown_var.set("")  

    def reset_chronometer(self):
        self.entry_time.delete(0, tk.END)
        self.label_time.config(text="Süre girin:")
        self.start_button.config(state=tk.NORMAL)
        self.reset_button.config(state=tk.DISABLED)
        self.running = False  
        self.countdown_var.set("") 

    def update_score(self, team_index, delta):
        self.team_scores[team_index] += delta
        self.team_labels[team_index].config(text=str(self.team_scores[team_index]))

    def get_point_change(self):
        try:
            return int(self.entry_point_change.get())
        except ValueError:
            return 10


if __name__ == "__main__":
    root = tk.Tk(screenName=None,baseName=None, className="QuizShow", useTk=1)
    app = ChronometerApp(root)
    root.mainloop()
