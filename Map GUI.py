import webbrowser
from ctypes import windll

import customtkinter
import customtkinter as ctk
from PIL import Image


def open_html_file():
    path = 'draft2.html'
    html_page = f'{path}'
    new = 2
    webbrowser.open(html_page, new=new)


def open_site():
    webbrowser.open_new('https://github.com/AbhinavDeokuliar/InteractiveMaps')


"""GUI Config"""
ctk.set_appearance_mode('dark')
app = ctk.CTk()
app.geometry('900x900')
app.title('InteravtiveAtlas')
windll.shcore.SetProcessDpiAwareness(2)
app.resizable(False, False)

"""GUI Elements"""

frame = ctk.CTkFrame(app)
frame.pack(fill='both')
frame.configure(fg_color='black')

logo = customtkinter.CTkImage(light_image=Image.open("logi.jpg  "),
                              dark_image=Image.open("logi.jpg"),
                              size=(100, 100))
logo_label = customtkinter.CTkLabel(frame, image=logo, text="")

name = ctk.CTkLabel(frame, text='Interactive Atlas', font=('Arial Black', 36), text_color='white', fg_color='grey',
                    corner_radius=16, width=600)
github = ctk.CTkButton(frame, text='GitHub Repositary', command=open_site, width=100)

logo_label.pack(side='left', padx=20, fill='y')
name.pack(side='left', padx=10, pady=10, fill='y')
github.pack(side='left', padx=10, fill='y')

description1 = ctk.CTkLabel(app, text="Chandigarh University's Interactive Maps with Python is a precise project "
                            , font=('Arial ', 12), text_color='#7fffd4', justify='center')
description2 = ctk.CTkLabel(app, text="designed to create dynamic maps using Python. It offers  "
                            , font=('Arial ', 12), text_color='#7fffd4', justify='center')
description3 = ctk.CTkLabel(app, text="students an engaging tool to explore various locations  "
                            , font=('Arial ', 12), text_color='#7fffd4', justify='center')

html_button = ctk.CTkButton(app, text='Show Map', font=('Arial Black', 36), command=open_html_file, corner_radius=16,
                            text_color='black', hover_color='#ff7373', border_color='yellow', fg_color='#e6e6fa')

description1.pack()
description2.pack()
description3.pack()

my_image = customtkinter.CTkImage(light_image=Image.open("cu.jpeg"),
                                  dark_image=Image.open("cu.jpeg"),
                                  size=(600, 500), )
image_label = customtkinter.CTkLabel(app, image=my_image, text="")
image_label.pack()

html_button.pack(pady=10)

app.mainloop()
