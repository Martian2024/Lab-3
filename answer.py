# вариант лабы - 4
from tkinter import Tk, Frame, Label, Button, Entry, END
from PIL import Image, ImageTk, ImageSequence
from random import randint
from pygame import mixer


class MainClass(Tk):
    def __init__(self):
        super().__init__()

        self.WIDTH = 800
        self.HEIGHT = 600
        self.NUMBER_OF_CHUNKS = 4
        self.SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        self.INTERVAL_BORDERS = (20, len(self.SYMBOLS))

        self.title('Skyrim keys')
        self.geometry(f'{self.WIDTH}x{self.HEIGHT}')
        self.resizable(False, False)

        self.background_image_pil = Image.open(
            'whiterun_in_the_doghouseadjusted.jpg').resize((self.WIDTH, self.HEIGHT))
        self.background_image = ImageTk.PhotoImage(self.background_image_pil)
        self.gif = Image.open('gc_skyrim_header.gif')
        self.gif_frames = []
        for frame in ImageSequence.Iterator(self.gif):
            obj = ImageTk.PhotoImage(frame.resize((200, 100)))
            self.gif_frames.append(obj)

        self.frame = Frame(self, width=self.WIDTH, height=self.HEIGHT, bg='blue')
        self.frame.place(x=0, y=0)
        self.image_label = Label(self.frame, image=self.background_image)
        self.image_label.place(x=-2, y=0)
        self.gif_label = Label(self.frame)
        self.gif_label.place(relx=0.5, rely=0.3, anchor="center")
        self.key_value = Entry(self.frame, text='XXXX-XXXX-XXXX')
        self.key_value.place(relx=0.5, rely=0.5, anchor="center")
        self.generate_button = Button(
            self.frame, text='Generate key!', command=self.generate_key)
        self.generate_button.place(relx=0.5, rely=0.6, anchor="center")
        self.play_button = Button(
            self.frame, text='Generate key!', command=self.generate_key)
        self.play_button.place(relx=0.5, rely=0.6, anchor="center")
        self.stop_button = Button(
            self.frame, text='Generate key!', command=self.generate_key)
        self.stop_button.place(relx=0.5, rely=0.6, anchor="center")

        self.after(50, self.update)
        mixer.init()
        mixer.music.load('01 - Dragonborn.mp3')
        mixer.music.play(loops=-1)

    def set_text(self, text):
        self.key_value.delete(0, END)
        self.key_value.insert(0, text)

    def update(self, frame=30):
        self.gif_label.configure(image=self.gif_frames[frame])
        loop = self.after(50, self.update, frame + 1 if frame + 1 < self.gif.n_frames else 0)

    def generate_key(self):
        chunks = []
        for _ in range(self.NUMBER_OF_CHUNKS):
            current_sum = 0
            chunk = ''
            for _ in range(4):
                index = randint(
                    self.INTERVAL_BORDERS[0] - current_sum, self.INTERVAL_BORDERS[1] - current_sum - 1)
                chunk += self.SYMBOLS[index]
                current_sum += index
            chunks.append(chunk)
            if current_sum < self.INTERVAL_BORDERS[0] or current_sum > self.INTERVAL_BORDERS[1]:
                print('AAAAAAAAAAA')
        self.set_text('-'.join(chunks))


if __name__ == '__main__':
    root = MainClass()
    root.mainloop()
