from tkinter import *
import customtkinter as ctk
from qrcode import make_qr
import tomllib

with open("config.toml", "rb") as file:
    config = tomllib.load(file)


ctk.set_default_color_theme("dark-blue")

class App(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()

        def create_qrcode():
            make_qr(
                self.url.get(),
                self.location.get(),
                self.logo.get(),
                (self.output.get() != "" and self.output.get() or None)
            )

        self.geometry("500x300")

        self.title("QRCode creator")
        self.minsize(400, 300)

        bold25 = ctk.CTkFont(self, size=25, weight="bold")

        self.grid_rowconfigure(0, weight=0, minsize=100)
        self.grid_columnconfigure((0, 1), weight=1)

        msg = ctk.CTkLabel(self, font=bold25, text="Make a QR Code")
        msg.grid(columnspan=2)
        msg.bind('<Configure>', lambda e: msg.configure(wraplength=msg.winfo_width()))

        ctk.CTkLabel(self, text="URL").grid(row=1, sticky=NW)
        self.url = ctk.CTkEntry(self, corner_radius=10, width=375, placeholder_text="URL to go to")
        self.url.grid(row=1, column=1, sticky=W)

        ctk.CTkLabel(self, text="Location").grid(row=2, sticky=NW)
        self.location = ctk.CTkOptionMenu(self, values=config["INFO"]["locations"])
        self.location.set("bhm")
        self.location.grid(row=2, column=1, sticky=W)

        ctk.CTkLabel(self, text="Add location logo").grid(row=3, sticky=NW)
        self.logo = ctk.CTkSwitch(self, text="")
        self.logo.select()
        self.logo.grid(row=3, column=1, sticky=W)

        ctk.CTkLabel(self, text="Output [Ext must be png]").grid(row=4, sticky="NW")
        self.output = ctk.CTkEntry(self, corner_radius=10, width=375, placeholder_text="qrcode.png")
        self.output.grid(row=4, column=1, sticky=W)

        ctk.CTkButton(self, text="Create QR Code", command=create_qrcode).grid(row=5, columnspan=2)




if __name__ == "__main__":
    app = App()
    app.mainloop()