import PySimpleGUI as sg
import pyautogui
from time import sleep
import threading

class TelaPython:
    def __init__(self):
        # Layout
        layout = [
            [sg.Text("Atualizar Power BI", justification='center', font=('Helvetica', 14), size=(20, 1))],
            [sg.Button('Atualizar', size=(20, 3), font=('Helvetica', 12, 'bold'), button_color=('#ffffff', '#505050'), border_width=0, pad=(50, 50), key='-ATUALIZAR-')]
        ]
        # Janela
        self.janela = sg.Window("Atualizar", size=(300, 200), layout=layout, element_justification='center', finalize=True, no_titlebar=False, keep_on_top=True, alpha_channel=0.95, resizable=False, grab_anywhere=True)
        
    def Iniciar(self):
        rodando = False
        thread = None
        
        while True:
            event, values = self.janela.Read(timeout=100)
            
            if event == sg.WINDOW_CLOSED:
                self.janela.close()
                break
                
            if event == '-ATUALIZAR-':
                if not rodando:
                    rodando = True
                    thread = threading.Thread(target=self.executar_automatico)
                    thread.start()
                
            if event == 'Parar':
                rodando = False
                if thread is not None and thread.is_alive():
                    thread.join()
                    
    def executar_automatico(self):
        while True:
            pyautogui.click(623, 86, duration=1)
            sleep(3600)

if __name__ == '__main__':
    tela = TelaPython()
    tela.Iniciar()
