import tkinter as tk
from tkinter import messagebox
import random

englishKelimeler = [
    'apple', 'banana', 'grape', 'orange', 'strawberry',
    'pear', 'peach', 'plum', 'cherry', 'apricot',
    'melon', 'watermelon', 'kiwi', 'mango', 'pineapple',
    'blueberry', 'raspberry', 'blackberry', 'lime', 'lemon',
    'coconut', 'pomegranate', 'fig', 'date', 'guava'
]

turkishKelimeler = [
    'elma', 'muz', 'üzüm', 'portakal', 'çilek',
    'armut', 'şeftali', 'erik', 'kiraz', 'kayısı',
    'kavun', 'karpuz', 'kivi', 'mango', 'ananas',
    'yaban mersini', 'ahududu', 'böğürtlen', 'lime', 'limon',
    'hindistancevizi', 'nar', 'incir', 'hurma', 'guava'
]

indis = random.sample(range(len(englishKelimeler)), 5)
rasgeleİngiliceKelimeler = [englishKelimeler[i] for i in indis]
rasgeleTürkceKelimeler = [turkishKelimeler[i] for i in indis]

sayac = 0
YanlisCevaplar = []

class KelimeBulmaca(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Kelime Tahmin Oyunu")
        self.geometry("800x600")
        self.configure(bg="lightblue")

        self.current_question = 0

        self.label = tk.Label(self, text=f"{self.current_question + 1}. İngilizce Kelime: {rasgeleİngiliceKelimeler[self.current_question]}", font=("Helvetica", 18), bg="lightblue")
        self.label.pack(pady=20)

        self.entry = tk.Entry(self, font=("Helvetica", 16))
        self.entry.pack(pady=10)

        self.button = tk.Button(self, text="Cevabı Kontrol Et", font=("Helvetica", 16), bg="white", command=self.CevapKontrol)
        self.button.pack(pady=20)

        self.start_button = tk.Button(self, text="Başlat", font=("Helvetica", 16), bg="white", command=self.Baslat)
        self.start_button.pack(pady=50)

    def Baslat(self):
        self.start_button.pack_forget()
        self.label.pack(pady=20)
        self.entry.pack(pady=10)
        self.button.pack(pady=20)

    def CevapKontrol(self):
        global sayac, YanlisCevaplar

        KullanıcıCevap = self.entry.get().strip().lower()
        DogruCevap = rasgeleTürkceKelimeler[self.current_question]

        if KullanıcıCevap == DogruCevap:
            sayac += 1
        else:
            YanlisCevaplar.append((rasgeleİngiliceKelimeler[self.current_question], DogruCevap))

        self.current_question += 1

        if self.current_question < len(rasgeleİngiliceKelimeler):
            self.label.config(text=f"{self.current_question + 1}. İngilizce Kelime: {rasgeleİngiliceKelimeler[self.current_question]}")
            self.entry.delete(0, tk.END)
        else:
            wrong_answers_str = "\n".join([f"{eng} - {tr}" for eng, tr in YanlisCevaplar])
            messagebox.showinfo("Oyun Bitti", f"Oyun bitti! Doğru cevap sayınız: {sayac}\n\nYanlış cevaplar:\n{wrong_answers_str}")
            self.destroy()

if __name__ == "__main__":
    app = KelimeBulmaca()
    app.mainloop()
