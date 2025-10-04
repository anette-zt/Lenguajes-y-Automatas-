"""Contador de emails desde un texto y saber cuántos son correctos o incorrectos"""
import re
import matplotlib.pyplot as plt

# Archivo txt que contiene los correo correctos e incorrectos
archivo = open("correos.txt", "r") 
lineas = archivo.readlines() 
archivo.close()

def validar_correos(correo):
    correo = correo.strip().lower()
    #patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    patron = r'^\d+\.\s*[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, correo) is not None

# Contador de correos
validos = 0
invalidos = 0

# Evalua cada correo, para verificar si esta bien o mal 
for correo in lineas:
    correo = correo.strip()
    if validar_correos(correo):
        resultado = "Válido"
        validos += 1
    else:
        resultado = "Inválido"
        invalidos += 1
    print(f"{correo} → {resultado}")

# Resumen de los correos validos e invalidos 
print("\n RESULTADOS")
print(f"Total de correos: {len(lineas)}")
print(f"Correos válidos: {validos}")
print(f"Correos inválidos: {invalidos}")

Categorias = ['Válidos', 'Inválidos']
valores = [validos, invalidos]

plt.bar(Categorias, valores, color=['green', 'red'])
plt.title('Correos Válidos vs Inválidos')
plt.ylabel("valores")
plt.xlabel("Tipo de correo")


plt.show()   