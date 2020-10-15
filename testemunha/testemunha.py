from xmlrpc.client import ServerProxy
import time
import threading
from tkinter import *

s = ServerProxy('http://localhost:20064', allow_none=True)
StartTime = time.time()


def verdict_response():
    if s.veredito(input_name.get()) != 'Aguardando Veredito para '+ input_name.get():
        inter.cancel()
        global lbl_result
        lbl_result.grid_forget()
        lbl_result = Label(root, text=s.veredito(input_name.get()))
        lbl_result.grid(row=3, column=1)
    print("Veredito: ", s.veredito(input_name.get()))

def send_response_yes():
    print(str(input_name.get()))
    s.set(input_name.get(), 'sim')
    print('Enviando Resposta ao Servidor')
    # print("Veredito: ", s.veredito('Lula'))
    global inter
    global lbl_result
    lbl_result.grid_forget()
    lbl_result = Label(root, text=s.veredito(input_name.get()))
    lbl_result.grid(row=3, column=1)
    inter = SetInterval(1, verdict_response)

def send_response_no():
    s.set(input_name.get(), 'não')
    print('Enviando Resposta ao Servidor')
    # print("Veredito: ", s.veredito(input_name.get))
    global inter
    global lbl_result
    lbl_result.grid_forget()
    lbl_result = Label(root, text=s.veredito(input_name.get()))
    lbl_result.grid(row=3, column=1)
    inter = SetInterval(1, verdict_response)
    


class SetInterval:
    def __init__(self, interval, action):
        self.interval = interval
        self.action = action
        self.stopEvent = threading.Event()
        thread = threading.Thread(target=self.__setInterval)
        thread.start()

    def __setInterval(self):
        nextTime = time.time() + self.interval
        while not self.stopEvent.wait(nextTime - time.time()) :
            nextTime += self.interval
            self.action()

    def cancel(self):
        self.stopEvent.set()

root = Tk()
root.title('RPC Python')
root.geometry('450x150')
root.columnconfigure(0, minsize=200)
root.columnconfigure(1, minsize=200)
root.rowconfigure(0, minsize=10)
root.rowconfigure(1, minsize=10)
root.rowconfigure(2, minsize=10)
root.rowconfigure(3, minsize=10)

name = Label(root, text='Nome')
name.grid(row=1, column=0)
input_name = Entry(root)
input_name.grid(row=1, column=1)
lbl_title = Label(root, text='Você vai Testemunhar?')
lbl_title.grid(row=0, column=0, columnspan=2)
btn_yes = Button(root, text='Sim', command=send_response_yes)
btn_yes.grid(row=2, column=0)
btn_no = Button(root, text='Não', command=send_response_no)
btn_no.grid(row=2, column=1)
lbl_veredito = Label(root, text='Veredito: ')
lbl_veredito.grid(row=3, column=0)
lbl_result = Label(root, text='')
lbl_result.grid(row=3, column=1)

root.mainloop()

