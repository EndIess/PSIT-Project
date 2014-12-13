from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
root = Tk()     
top = Frame(root)
top.grid(columnspan=3, rowspan=2)

##windows
root.title("MAGIC WORD")
root.resizable(width=FALSE, height=FALSE)
root.config(bg='#414141')

image = Image.open("logo.gif")
photo = ImageTk.PhotoImage(image)
label = tk.Label(image=photo)
label.image = photo 
label.grid(column=0, row=5, padx=25, pady= 15)


def change(string, temp = ''):
    """eng -> thai"""
    str1 = '1234567890-=qwertyuiop[]asdfghjkl;\'zxcvbnm,./'
    str2 = 'ๅ/-ภถุึคตจขชๆไำพะัีรนยบลฟหกดเ้่าสวงผปแอิืทมใฝ'
    str3 = '!@#$%^&*()_+QWERTYUIOP{}ASDFGHJKL:\"ZXCVBNM<>?'
    str4 = '+๑๒๓๔ู฿๕๖๗๘๙๐"ฎฑธํ๊ณฯญฐ,ฤฆฏโฌ็๋ษศซ.()ฉฮฺ์?ฒฬฦ'
    for i in string:
        if i in str1:
            temp += str2[str1.find(i)]
        elif i in str2:
            temp += str1[str2.find(i)]
        elif i in str3:
            temp += str4[str3.find(i)]
        elif i in str4:
            temp += str3[str4.find(i)]
        else:temp += i
    return(temp)

####make "MAGIC WORD"
##hwtext = Label(top, text='MAGIC WORD', font='times 18 bold', bg='#414141')
##hwtext.grid(column=0, row=1, columnspan=2)

##print enter the sentense
mntext = Label(top, text='Enter The Sentense', font='tohoma 9', bg='#414141')
mntext.grid(column=0, row=1, sticky=E)

##print result
nntext = Label(top, text='Result', font='tohoma 9', bg='#414141')
nntext.grid(column=0, row=2, sticky=E)

##input
r = StringVar()
r_entry = Entry(top, textvariable=r, bg='#ff8040')
r_entry.grid(column=1, row=1)

##output
s = StringVar()
s_entry = Entry(top, textvariable=s, bg='#ff8040')
s_entry.grid(column=1, row=2)

##button
def pressed():
    try:
        if r.get() != root.clipboard_get() and s.get() != root.clipboard_get():
            r.set(root.clipboard_get())
            string = change(r.get())
            s.set(string)
            root.clipboard_clear()
            root.clipboard_append(string)
    except:
        pass
    root.after(10, pressed)

##quit program.
def quit(event=None):
    root.destroy()

quit_button = Button(text='END PROGRAM', command=quit,
                     background='#ff5b5b', foreground='#ffffff',height=1, width=33)
quit_button.columnconfigure(0, weight=1)
quit_button.grid(row=4)

##root.bind_all('<q>', quit)
root.after(0, pressed)
root.mainloop()
