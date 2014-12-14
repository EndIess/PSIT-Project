from tkinter import *
root = Tk()     
top = Frame(root)
top.grid(column=0, row=0)

def change(self, temp = ''):
    """eng <-> thai"""
    string = r.get()
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
    s.set(temp)
    root.clipboard_clear()
    root.clipboard_append(temp)

##make "MAGIC WORD"
gif1 = PhotoImage(file = 'logo.gif')
canvas = Canvas(top,width=295,height=170)
canvas.create_image(150, 0, image = gif1, anchor = N)
canvas.grid(column=0, row=0, columnspan=3, rowspan=2)

##print enter the sentense
mntext = Label(top, text='Enter The Sentense', font='tohoma 9')
mntext.grid(column=0, row=2)

##print result
nntext = Label(top, text='Result', font='tohoma 9')
nntext.grid(column=0, row=3, sticky=E)

##input
r = StringVar()
r_entry = Entry(top, textvariable=r, width=30)
r_entry.grid(column=1, row=2)

##output
s = StringVar()
s_entry = Entry(top, textvariable=s, width=30)
s_entry.grid(column=1, row=3)

##reset
def reset(self):
    root.clipboard_clear()
    r.set('')
    s.set('')
    
##button
def pressed():
    r_entry.bind('<Return>', change)
    root.bind('<Delete>', reset)
    try:
        if r.get() != root.clipboard_get() and s.get() != root.clipboard_get():
            r.set(root.clipboard_get())
            change('a')
    except:
        pass
    root.after(10, pressed)

##quit program.
def quit(event=None):
    root.destroy()

quit_button = Button(text='END PROGRAM', command=quit,
                     background='#ff5b5b', foreground='#ffffff',height=1, width=41)
quit_button.columnconfigure(0, weight=1)
quit_button.grid(row=6)
root.after(0, pressed)
root.mainloop()
