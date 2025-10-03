"""Validación de Contraseñas"""

import re

def validar_contrasena(password):
    criterios = {
        "longitud": len(password) >= 8, 
        "mayuscula": re.search(r'[A-Z]', password) is not None,
        "minuscula": re.search(r'[a-z]', password) is not None,
        "numero": re.search(r'\d', password) is not None,
        "especial": re.search(r'[@$!%*?&#]', password) is not None
    }

    if all(criterios.values()):
        return True, []
    else:
        no_cumple = [c for c, cumple in criterios.items() if not cumple]
        return False, no_cumple

# Casos de prueba
contrasenas = ["Segura123!", "contrasena", "MAYUSCULA123!", "P@ssw0rd"]

for pwd in contrasenas:
    valida, fallos = validar_contrasena(pwd)
    if valida:
        print(f"{pwd} → Válida")
    else:
        print(f"{pwd} → Inválida. No cumple: {', '.join(fallos)}")