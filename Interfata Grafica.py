#interfata grafica
root = Tk()


#functia de afisare a mesajului
def send():
    send = 'Dvs: ' + e.get()
    txt.insert(END, "\n" + send)
    txt.insert(END, "\n" + 'Botul Studi: ' + get_response(e.get()))


    if e.get() in exit_list:
        root.after(1000, lambda: root.destroy())

    e.delete(0, END)

#customizarea interfetei
root.resizable(width=False, height=False)

txt = Text(root)
txt.configure(bg='skyblue')
txt.grid(row=0, column=0, columnspan=2)

txt.insert(END, "Botul Studi: Eu sunt Botul Studi si voi incerca sa iti raspund la intrebari!\nCautati folosind indexul UPT! :)")

e = Entry(root, width=100)
e.grid(row=1,column=0)
e.configure(bg='gainsboro')
send = Button(root, text='Send', command=send, height=2, width=6, font=FONT_BOLD, bg='red').grid(row=1, column=1)


root.title("Bine ai venit!")
root.mainloop()
