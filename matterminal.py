import database as db

# titolo della finestra
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("MatTerminal")

import os

info_str="""\ninfo/i = lista comandi
add/a = aggiungi comando
modifica/m = modifica comandi e percorsi
font verde 
q = esci\n"""

while(True):
    
    user_input = input("\n"+db.username+"€  ")

    if(user_input=="info" or user_input=="i"):
        print(info_str)
        db.stampa_comandi()
        continue
    
    if(user_input=="font verde"):
        os.system('color 2')    # verde
        continue

    if(user_input=="modifica" or user_input=="m"):
        db.modifica()
        continue

    if(user_input=="q"):
        break

    if(user_input=="add" or user_input=="a"):
        db.aggiungi_comando()
        continue

    db.esegui(user_input)