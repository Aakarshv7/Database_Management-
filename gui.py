from tkinter import * 

main=Tk()
main.title("Restaurent Management System -- ")
main.geometry("1250x620")

Photof=Frame(main)

img=PhotoImage(file="E:\\PySqlProject\\images\\restaurent4.png")
label1= Label(Photof,image=img,background="#D54078")
label1.pack(pady=0,padx=0)
Photof.pack(side=LEFT,pady=0,padx=0)

content=Frame(main)

label2= Label(content,height=80, width=80,background="#D54078")
label2.pack(padx=0, pady=0)
content.pack(side=LEFT,padx=0)

main.mainloop()