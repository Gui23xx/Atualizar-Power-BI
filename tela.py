import pyautogui
import time
from tkinter import *
import customtkinter

# Criar janela CTk
root = customtkinter.CTk()

# Tamanho da Tela
root.geometry("300x200")

# Função a ser executada ao pressionar o botão "Atualizar"
def atualizar_power_bi():
    # Coordenadas do botão "Atualizar" no seu monitor
    x = 2235  # Coloque o valor correto das coordenadas X
    y = -500  # Coloque o valor correto das coordenadas Y

    # Move o mouse para as coordenadas especificadas
    pyautogui.moveTo(x, y)

    intervalo = 3600

    while True:
        # Move o mouse para as coordenadas especificadas
        pyautogui.moveTo(x, y)

        # Clica no botão "Atualizar"
        pyautogui.click()

        # Aguarda o intervalo de tempo
        time.sleep(intervalo)

# Label de texto
texto = Label(root, text="Atualizar o Power BI a cada 1h de forma Automática", font=("Arial", 12), fg="white", bg=root.cget('bg'), wraplength=250)
texto.pack(pady=25)

# Botão (CTk Button)
botao = customtkinter.CTkButton(master=root, text="Atualizar", command=atualizar_power_bi)
botao.pack()

# Tornar a janela não redimensionável
root.resizable(False, False)

root.mainloop()
