from Tkinter import *

root = Tk()     
top = Frame(root)
top.pack(side='top')


##make "MAGIC WORD"
hwframe = Frame(top)
hwframe.pack(side='top') 
font = 'times 18 bold'
hwtext = Label(hwframe, text='MAGIC WORD', font=font)
hwtext.pack(side='top', pady=20)

rframe = Frame(top)
rframe.pack(side='top', padx=10, pady=20)


##enter the sentense
r = StringVar()
r.set('enter the sentense')   
r_entry = Entry(rframe, textvariable=r)
r_entry.pack(side='left')

##button
def pressed():
    print "ANS"

quit_button = Button(top, text='CHANGE', background='#3399ff', foreground='#808080',
                      command = pressed)
quit_button.pack(side='top', pady=5)


##quit program.
def quit(event=None):
    root.destroy()

quit_button = Button(top, text='END PROGRAM', command=quit,
                     background='#ff5b5b', foreground='#ffffff')
quit_button.pack(side='top', pady=5, fill='x')

root.bind('<q>', quit)

root.mainloop()

