import csv
import os
from termcolor import colored
import subprocess

def username():
    return open("./memoria/username.txt", "r").read()

def stampa_comandi():
    with open("./memoria/comandi.csv", newline="") as filecsv:
            lettore = csv.reader(filecsv, delimiter=",")
            for riga in lettore:
                print(riga[0] + " = " + riga[1] + " -> " + riga[2])

def modifica():
    subprocess.Popen("notepad.exe .\memoria\comandi.csv")
    return

def aggiungi_comando():
    nome_comando = input("nome comando: ")
    azione = input("apri filesystem[open] / esegui[exe] / [link] / [code]:  ")
    if(azione=="open"):
        azione = "explorer.exe"
    elif(azione=="code"):
        azione = "vscode"
    else:
        print("Errore...")
        return
    path = input("path/link: ")
    path = path.replace("C:/", "/mnt/c/")
    csv_line = nome_comando + "," + azione + ',"' + path +'"'
    with open('./memoria/comandi.csv','a') as filecsv:
        filecsv.write(csv_line+"\n")

def esegui(user_input):
    azione = ""
    path = ""
    with open("./memoria/comandi.csv", newline="") as filecsv:
            lettore = csv.reader(filecsv, delimiter=",")
            for riga in lettore:
                if user_input==riga[0]:
                    azione = riga[1]
                    path = riga[2]
                    break
    if azione=="":
        print("Comando non valido")
        return
    if azione=="explorer.exe":
        subprocess.Popen("explorer "+path)
        return
    if azione=="vscode":
        os.system('code "'+path+'"')
        return