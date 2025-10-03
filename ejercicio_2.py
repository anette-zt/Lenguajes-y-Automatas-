"""Codigo para extraer numeros telefonicos"""

import re

def extraer_telefono(texto):
    patron = r'(\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})'
    telefonos = re.findall(patron, texto)   
    return telefonos    

# Ejemplo de uso
texto = "Contacta a Anette al (646)2563848 o a su Mama al (646)1399814."
telefono = extraer_telefono(texto)
print("Numeros encontrados:", telefono)
