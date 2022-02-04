import tkinter as tk
from tkinter import ttk, font

from tkinter import CENTER

import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=1, #1-40, 1 being smallest version of QR
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

class app:

    def __init__(self, master):
        self.master = master
        self.master.geometry("500x500")
        self.master.title("QR Code")
        self.menu()
        self.messagetext = None


    def menu(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame1 = tk.Frame(self.master, width=300, height=300)
        self.frame1.pack()
        def_font = font.Font(family='MS Sans Serif')
        self.uppertext1 = tk.Label(self.frame1, text="QR Code", font=def_font)
        self.uppertext1.pack()
        self.create_btn = tk.Button(self.frame1, text="Create QR Code", font=def_font, command=self.create)
        self.create_btn.pack()
        def_font = font.Font(family='MS Sans Serif')
        self.decode_btn = tk.Button(self.frame1, text="Decode QR Code", font=def_font,
                                      command=self.decode)
        self.decode_btn.pack()

    def create(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame2 = tk.Frame(self.master, width=300, height=300)
        self.frame2.pack()
        def_font = font.Font(family='MS Sans Serif')
        self.reg_txt2 = tk.Label(self.frame2, text="Create QR Code", font=def_font)
        self.reg_txt2.pack()

        self.message_label = tk.Label(self.frame2, text="Enter the input to encode", font=def_font)
        self.message_label.pack(padx=20, pady=100)
        self.message_entry = tk.Entry(font=(def_font, 25))  # width handled by place()
        self.message_entry.place(x=120, y=140, width=250, height=40)

        self.createQR_btn = tk.Button(self.frame2, text="Create QR", font=def_font, command=self.dostuff)
        self.createQR_btn.pack()

        self.menu_btn = tk.Button(self.frame2, text="Main Menu", font=def_font, command=self.menu)
        self.menu_btn.pack()

    def decode(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame3 = tk.Frame(self.master, width=300, height=300)
        self.frame3.pack()
        def_font = font.Font(family='MS Sans Serif')
        self.uppertext2 = tk.Label(self.frame3, text="Decode QR", font=def_font)
        self.uppertext2.pack()
        self.menu_btn = tk.Button(self.frame3, text="Main Menu", font=def_font, command=self.menu)


        self.decodeQR_btn = tk.Button(self.frame3, text="Decode QR", font=def_font, command=self.printstuff)
        self.decodeQR_btn.pack()
        self.menu_btn.pack()


    def dostuff(self):
        messagetext = self.message_entry.get()
        print("message: " + messagetext)
        generatedQR = self.generateqr(messagetext)


    def generateqr(self, messagetext):
        qr.add_data(messagetext)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
        img.save("sample.png")
        image = Image.open('sample.png')
        image.show()




root = tk.Tk()
app(root)
root.mainloop()




