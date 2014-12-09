from tkinter import *

root = Tk()     
top = Frame(root)
top.pack(side='top')

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
##make "MAGIC WORD"
hwframe = Frame(top)
hwframe.pack(side='top') 
font = 'times 18 bold'
hwtext = Label(hwframe, text='MAGIC WORD', font=font)
hwtext.pack(side='top', pady=20)

rframe = Frame(top)
rframe.pack(side='top', padx=10, pady=20)

##print enter the sentense
mntext = Label(hwframe, text='enter the sentense', font='times 14')
mntext.pack()

##enter the sentense
r = StringVar()
r_entry = Entry(rframe, textvariable=r)
r_entry.pack(side='top')

##output
s = StringVar()
s_entry = Entry(rframe, textvariable=s)
s_entry.pack(side='bottom')

##button
def pressed():
    s.set(change(r.get()))
    
quit_button = Button(top, text='CHANGE', background='#3399ff', foreground='#808080',
                      command = pressed)
quit_button.pack(side='top', pady=5)


##quit program.
def quit(event=None):
    root.destroy()

quit_button = Button(top, text='END PROGRAM', command=quit,
                     background='#ff5b5b', foreground='#ffffff')
quit_button.pack(side='top', pady=5, fill='x')

#root.bind('<q>', quit)

root.mainloop()
