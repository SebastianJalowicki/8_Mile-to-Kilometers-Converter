from tkinter import *

def convert():
    new_text = float(input.get())
    km = new_text * 1.609
    label_2.config(text=f'{km}')

window = Tk()
window.title('Mile to Km Converter')
window.minsize(width=300, height=200)
window.config(padx=50, pady=50)

### Label

label_1 = Label(text='Is equal to:', font=('Calibri', 14))
label_1.grid(column=0, row=1)
label_1.config(padx=10, pady=10)

label_2 = Label(text='0', font=('Calibri', 14))
label_2.grid(column=1, row=1)
label_2.config(padx=10, pady=10)

label_3 = Label(text='Miles', font=('Calibri', 14))
label_3.grid(column=2, row=0)
label_3.config(padx=10, pady=10)

label_4 = Label(text='Km', font=('Calibri', 14))
label_4.grid(column=2, row=1)
label_4.config(padx=10, pady=10)

### Button

button = Button(text='Convert', command=convert, font=('Calibri', 14))
button.grid(column=1, row=2)
button.config(padx=10, pady=10)

### Entry

input = Entry(width=10, font=('Calibri', 14))
input.grid(column=1, row=0)



window.mainloop()