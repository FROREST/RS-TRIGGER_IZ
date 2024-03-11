import tkinter as tk
from tkinter import messagebox
from tkinter import Entry, Label, Button, Canvas
from PIL import Image, ImageTk

class RSFlipFlopGUI:
    def __init__(self, master):
        self.master = master
        master.title("RS-триггер")

        self.rs_flip_flop = RSFlipFlop()

        self.label_s = Label(master, text="Введите значение входа S (0 или 1):")
        self.label_s.grid(row=1, column=0, padx=10, pady=10)

        self.entry_s = Entry(master)
        self.entry_s.grid(row=0, column=1, padx=10, pady=10)

        self.label_r = Label(master, text="Введите значение входа R (0 или 1):")
        self.label_r.grid(row=0, column=0, padx=10, pady=10)

        self.entry_r = Entry(master)
        self.entry_r.grid(row=1, column=1, padx=10, pady=10)

        self.button = Button(master, text="Установить триггер", command=self.set_flip_flop)
        self.button.grid(row=2, column=0, columnspan=2, pady=10)

        self.canvas = Canvas(master, width=200, height=200)
        self.canvas.grid(row=0, column=2, rowspan=3, padx=10, pady=10)

        self.result_label_q = Label(master, text="Выход Q:")
        self.result_label_q.grid(row=0, column=3, padx=10, pady=10)

        self.result_label_not_q = Label(master, text="Инвертированный выход Q:")
        self.result_label_not_q.grid(row=1, column=3, padx=10, pady=10)

        # Загрузить изображение при инициализации
        self.show_image("//123.png")

    def set_flip_flop(self):
        try:
            s_input = int(self.entry_s.get())
            r_input = int(self.entry_r.get())
        except ValueError:
            self.show_error("Ошибка", "Введите числовые значения (0 или 1) для входов S и R.")
            return

        if not (0 <= s_input <= 1 and 0 <= r_input <= 1):
            self.show_error("Ошибка", "Недопустимые значения входов (S={}, R={})".format(s_input, r_input))
            return

        self.rs_flip_flop.set_input(s_input, r_input)


        self.canvas.delete("all")

        # Обновляем результаты
        result_q, result_not_q = self.rs_flip_flop.get_output()
        self.result_label_q.config(text="Выход Q: {}".format(result_q))
        self.result_label_not_q.config(text="Инвертированный выход Q: {}".format(result_not_q))


        self.show_image("//123.png")

    def show_image(self, path):
        image = Image.open(path)
        image = image.resize((200, 200), Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.BICUBIC)
        photo = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canvas.image = photo

    def show_error(self, title, message):
        messagebox.showerror(title, message)

class RSFlipFlop:
    def __init__(self):
        self.q = 0  # Исходное значение выхода Q
        self.not_q = 1  # Исходное значение инвертированного выхода Q

    def set_input(self, s, r):
        if s == 1 and r == 0:
            self.q = 1
            self.not_q = 0
        elif s == 0 and r == 1:
            self.q = 0
            self.not_q = 1
        elif s == 1 and r == 1:
            self.q = 0
            self.not_q = 0
        elif s == 0 and r == 0:
            pass


    def get_output(self):
        return self.q, self.not_q

root = tk.Tk()
app = RSFlipFlopGUI(root)
root.mainloop()
