from tkinter import *
root = Tk()
top = Frame(root)
top.grid(column=0, row=0)

root.title("MAGIC WORD")
root.resizable(width=FALSE, height=FALSE)

class Myapp(object):
    def __init__(self):
        ##Add menubar
        self.menubar = Menu(top)
        menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Help", menu=menu)
        menu.add_command(label="How to", command=self.how)
        menu.add_command(label="About", command=self.about)
        root.config(menu=self.menubar)
        
        ##make "MAGIC WORD"
        self.gif1 = PhotoImage(file = 'logo.gif')
        self.canvas = Canvas(top,width=295,height=170)
        self.canvas.create_image(150, 0, image = self.gif1, anchor = N)
        self.canvas.grid(column=0, row=0, columnspan=3, rowspan=2)

        ##print enter the sentense
        self.mntext = Label(top, text='Enter The Sentense', font='tohoma 9')
        self.mntext.grid(column=0, row=2)
        
        ##print result
        self.nntext = Label(top, text='Result', font='tohoma 9')
        self.nntext.grid(column=0, row=3, sticky=E)

        ##Input
        self.r = StringVar()
        self.r_entry = Entry(top, textvariable=self.r, width=30)
        self.r_entry.grid(column=1, row=2)

        ##Output
        self.s = StringVar()
        self.s_entry = Entry(top, textvariable=self.s, width=30)
        self.s_entry.grid(column=1, row=3)

        self.quit_button = Button(text='END PROGRAM', command=quit,
                     background='#ff5b5b', foreground='#ffffff',height=1, width=41)
        self.quit_button.columnconfigure(0, weight=1)
        self.quit_button.grid(row=6)

    ##Button
    def pressed(self):
        self.r_entry.bind('<Return>', change)
        root.bind('<Delete>', reset)
        try:
            if self.r.get() != root.clipboard_get() and self.s.get() != root.clipboard_get():
                self.r.set(root.clipboard_get())
                change('')
        except:
            pass
        root.after(10, app.pressed)
    ##About
    def about(self):
        message = messagebox.showinfo("About", "This program is automatically switched the language when you forget to change it.\n thai --> english\nenglish --> thai\nThis program created by Voradee Santivarotai and Supanut Suanthawee from faculty of Information Technology KMITL.\nfor PSIT project")
    ##How to
    def how(self):
        message = messagebox.showinfo("How to", "Hold run this program and then when you print error message you can copy this sentence and then you place it.")
##Reset
def reset(self):
    root.clipboard_clear()
    app.r.set('')
    app.s.set('')

##Eng<->Thai
def change(self, temp = ''):
    string = app.r.get()
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
    app.s.set(temp)
    root.clipboard_clear()
    root.clipboard_append(temp)

##Quit program
def quit(event=None):
    root.destroy()

app = Myapp()
root.after(0, reset(''))
root.after(5, app.pressed)
root.mainloop()
