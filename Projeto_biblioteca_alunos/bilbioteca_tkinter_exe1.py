import customtkinter as ctk
janela=ctk.CTk()
janela.geometry("500x500")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

texto=ctk.CTkLabel(janela, text="Testando a biblioteca Tkinter ensinado pelo aluno Celso")
texto.pack()

texto2=ctk.CTkEntry(janela, placeholder_text="Testando umas das fumções")
texto2.place(x=200, y=125)
texto2.pack()

texto3=ctk.CTkButton(janela, text="login")
texto3.place(x=200, y=200)
texto3.pack()


janela.mainloop()
