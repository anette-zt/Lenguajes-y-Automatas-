"""Codigo de expresion regular para validar correos electronicos"""

import re 

def validacion_correos(correo):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(patron, correo):
        return True
    else:
        return False
    
correos = ["anette.@dial.com","juan@navico.mx", "@ejemplo.com", "usuarioejemplo.com"]

for correo in correos:
    resultado = "valido" if validacion_correos(correo) else "invalido"
    print(f"{correo} {resultado}")