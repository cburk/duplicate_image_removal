from appJar import gui

import Tkinter as tk
from PIL import ImageTk, Image

class Popup():
    def __init__(self):
        self.root = -1
        self.result = False


    def conf(self):
        self.result = True
        self.root.destroy()

    def deny(self):
        self.result = False
        self.root.destroy()

    def spawn_popup(self, img1, img2):
        self.root = tk.Tk()
        T = tk.Label(self.root, text = "Are these images identical (if yes the top one will be deleted)")
        T.pack()
        imga = ImageTk.PhotoImage(Image.open(img1))
        panel1 = tk.Label(self.root, image = imga)
        panel1.pack(side = "bottom", fill = "both", expand = "yes")

        quitButton = tk.Button(self.root, text="Yes",
                            command=self.conf)
        quitButton.pack()
        quitButton = tk.Button(self.root, text="No",
                               command=self.deny)
        quitButton.pack()

        imgb = ImageTk.PhotoImage(Image.open(img2))
        panel2 = tk.Label(self.root, image = imgb)
        panel2.pack(side = "bottom", fill = "both", expand = "yes")

        self.root.mainloop()
        return self.result