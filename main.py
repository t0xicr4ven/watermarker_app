from tkinter import * 
from PIL import Image, ImageTk
from tkinter import filedialog

BACK_COLOR = '#03A9F4'
window = Tk()
window.title('Watermarker')
WATERMARK = Image.open('waterMark.png')


def quit_root():
    window.destroy()

def select_img():
    # get user to select image
    pic = filedialog.askopenfilename(title='Select A Image')
    image = Image.open(pic)
    image_size = image.size
    #re size watermark
    wm_re = WATERMARK.resize((round(image.size[0]*.35), round(image.size[1]*.35)))
    wm_pos = (image_size[0] - wm_re.size[0], image_size[1] - wm_re.size[1])
    #add watermark
    transparent = Image.new('RGBA', image_size, (0, 0, 0, 0))
    transparent.paste(image, (0, 0))
    transparent.paste(wm_re, wm_pos, mask=wm_re)
    transparent.show()
    
    #save image
    save_path = filedialog.asksaveasfilename(defaultextension='.png')
    complete_img = transparent
    complete_img.save(save_path)
    transparent.close()


logo_str_1 = '{  }'
logo_str_2 = 'Code Jar'
canvas = Canvas(window, height=500, width=600, highlightthickness=0,
        bg=BACK_COLOR)
canvas.grid(columnspan=2, rowspan=1, padx=10, pady=10)
canvas.create_text(300, 150, text=logo_str_1, font=('Arial',60))
canvas.create_text(300, 250, text=logo_str_2, font=('Arial',60))
#buttons
select_img_btn = Button(window, text='Select Image', command=select_img)
select_img_btn.grid(column=0, row=1, padx=10, pady=10)
quit_btn = Button(window, text='Quit', command=quit_root)
quit_btn.grid(column=1, row=1, padx=10, pady=10)
window.mainloop()
