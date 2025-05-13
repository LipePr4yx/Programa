import customtkinter as ctk
import subprocess as sub
ctk.set_appearance_mode("dark")

def open_jan():
    global janela_counter
    janela_counter += 1
    nova_janela = ctk.CTkToplevel()
    nova_janela.title(f"Janela {janela_counter}")
    nova_janela.geometry("300x200")



    nova_janela.lift()
    nova_janela.attributes("-topmost", True)
    

    def close_jan():
        nova_janela.destroy()
    

    fechar_abrolho = ctk.CTkButton(nova_janela, text="Fechar",font=("Helvetica",22),command=close_jan)
    fechar_abrolho.pack(pady=20)


def fechar_aplicacao():
    root.quit()


root = ctk.CTk()


root.title("Janela Principal")
root.geometry("400x300")


janela_counter = 0


abrolho_abrir=ctk.CTkButton(root,text="Abrir Janela",font=("Helvetica",22),fg_color="#32CD32",command=open_jan)
abrolho_abrir.pack(pady=50)



fechar_butt= ctk.CTkButton(root, text="Fechar",font=("Helvetica",22),fg_color="#DC143C",command=fechar_aplicacao)
fechar_butt.pack(pady=20)









root.mainloop()