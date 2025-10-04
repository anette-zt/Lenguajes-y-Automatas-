"""Contador de emails desde un texto y saber cuantos son correctos o incorrectos """
import re

# Casos de prueba
open ('correos.txt', 'r')
with open('correos.txt', 'r') as file:
    correos = file.read().splitlines()

def validar_correo(correo):
    # Patron del correo
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(patron, correo):
        return True
    else:
        return False       

for correo in correos:
    resultado = "Válido" if validar_correo(correo) else "Inválido"
    print(f"{correo} → {resultado}")