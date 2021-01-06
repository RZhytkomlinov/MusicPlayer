import tkinter as tk
from tkinter import filedialog as fd
from pygame import mixer


# from tkinter import font as tkfont


class MusicPlayer(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Main, Spotify, Device):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row='0', column='0', sticky='snew')

        self.show_frame("Main")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def load(self):
        self.music_file = fd.askopenfile()

    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state = True
        else:
            mixer.music.unpause()
            self.playing_state = False

    def stop(self):
        mixer.music.stop()



class Main(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        canvas = tk.Canvas(self, height=200, width=380, bg='black')
        canvas1 = tk.Canvas(self, height=200, width=380, bg='black')
        canvas.place(relx='0.5', rely='0.3', anchor='center')
        canvas1.place(relx='0.5', rely='0.7', anchor='center')
        butt = tk.Button(self, text='Spotify', bg='gray', width='10',
                         command=lambda: controller.show_frame('Spotify'))
        butt1 = tk.Button(self, text='This device', bg='gray', width='10',
                          command=lambda: controller.show_frame('Device'))
        # label.grid(row = '1', column ='0', padx=150,pady=100,)
        # label1.grid(row = '2', column ='0',padx=150, pady=100,)
        butt.place(relx='0.5', rely='0.3', anchor='center')
        butt1.place(relx='0.5', rely='0.7', anchor='center')


class Device(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        canvas = tk.Canvas(self, height=75, width=380, bg='black')
        canvas1 = tk.Canvas(self, height=75, width=380, bg='black')
        canvas2 = tk.Canvas(self, height=75, width=380, bg='black')
        canvas3 = tk.Canvas(self, height=75, width=380, bg='black')
        canvas4 = tk.Canvas(self, height=75, width=380, bg='black')
        canvas.place(relx='0.5', rely='0.1', anchor='center')
        canvas1.place(relx='0.5', rely='0.3', anchor='center')
        canvas2.place(relx='0.5', rely='0.5', anchor='center')
        canvas3.place(relx='0.5', rely='0.7', anchor='center')
        canvas4.place(relx='0.5', rely='0.9', anchor='center')

        play = tk.Button(self, text='Play', bg='gray', width='10',
                         command=lambda: controller.play())
        load = tk.Button(self, text='Load', bg='gray', width='10',
                         command=lambda: controller.load())
        pause = tk.Button(self, text='Pause', bg='gray', width='10',
                          command=lambda: controller.pause())
        stop = tk.Button(self, text='Stop', bg='gray', width='10',
                         command=lambda: controller.stop())
        back = tk.Button(self, text='Back', bg='gray', width='10',
                         command=lambda: controller.show_frame('Main'))
        play.place(relx='0.5', rely='0.1', anchor='center')
        load.place(relx='0.5', rely='0.3', anchor='center')
        pause.place(relx='0.5', rely='0.5', anchor='center')
        stop.place(relx='0.5', rely='0.7', anchor='center')
        back.place(relx='0.5', rely='0.9', anchor='center')


class Spotify(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        canvas = tk.Canvas(self, height=480, width=380, bg='black')
        label = tk.Label(self, text = 'not done', bg = 'white')
        canvas.place(relx='0.5', rely='0.5', anchor = 'center')
        label.place(relx='0.5', rely='0.5', anchor='center')


if __name__ == "__main__":
    mp = MusicPlayer()
    mp.geometry('400x500')
    mp.title("Music Player")
    mp.mainloop()
