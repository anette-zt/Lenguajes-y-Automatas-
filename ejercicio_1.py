"""Codigo de expresion regular para validar correos electronicos"""

import re

def validar_correo(correo):
    # Patron del correo
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(patron, correo):
        return True
    else:
        return False       

# Casos de prueba
correos = ["usuario@ejemplo.com", "nombre.apellido@dominio.mx", "usuarioejemplo.com", "@ejemplo.com"]

for correo in correos:
    resultado = "Válido" if validar_correo(correo) else "Inválido"
    print(f"{correo} → {resultado}")