from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

window = Tk()
window.title('Watermarker')
# get user to select image
pic = filedialog.askopenfilename()
image_to_edit = Image.open(pic)
o_size = image_to_edit.size
print(f'o size is {o_size}')
f_size = (400, 400)
factor = min(float(f_size[1])/o_size[1], float(f_size[0])/o_size[0])
print(f'factor is: {factor[]}')
width = int(o_size[0]* factor)
height = int(o_size[1]* factor)

reImg = image_to_edit.resize((width, height), Image.ANTIALIAS)
reImg = ImageTk.PhotoImage(reImg)
canvas = Canvas(height=500, width=500, highlightthickness=0)
image_to_edit = canvas.create_image(250,250, image=reImg)
canvas.grid(column=0,row=0)
window.mainloop()
