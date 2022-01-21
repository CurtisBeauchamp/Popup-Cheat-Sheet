import tkinter as tk
from PIL import ImageTk, Image

path = './sample-sheet.png'

root = tk.Tk()
root.title("Popup Cheat Sheet")
img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.bind("<KeyPress>", lambda e: root.destroy())
root.mainloop()