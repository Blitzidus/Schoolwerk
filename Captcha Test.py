from claptcha import Claptcha
from tkinter import Label, Tk
from PIL import ImageTk, Image

c = Claptcha('dank 420 memes', 'c:/windows/fonts/ARLRDBD.TTF', (200, 100), resampling=Image.NEAREST, noise=0.4)
# De PIL image object is hier een tuple
text, img = c.image

root = Tk()
root.geometry('600x300')
imgTk = ImageTk.PhotoImage(img)
label = Label(root, text='Type de gegeven tekst.')
label_img = Label(root, image=imgTk)

label.pack()
label_img.pack()

root.mainloop()