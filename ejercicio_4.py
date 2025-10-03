"""Extraer URL de un texto y sus dominios"""

import re

texto = "Visita https://www.google.com o http://github.com/usuario."

# Captura toda la URL
patron = r'(https?://[^\s]+|www\.[^\s]+)'

urls = re.findall(patron, texto)

for i, url in enumerate(urls, 1):
    print(f"URL {i}: {url}")
    # Sacar protocolo
    if url.startswith("http://"):
        protocolo = "http"
    elif url.startswith("https://"):
        protocolo = "https"
    else:
        protocolo = "N/A"
    # Seccion que saca el dominio y ruta
    partes = url.replace("http://", "").replace("https://", "")
    if "/" in partes:
        dominio, ruta = partes.split("/", 1)
        ruta = "/" + ruta
    else:
        dominio, ruta = partes, ""
    
    print(f"  Protocolo: {protocolo}")
    print(f"  Dominio: {dominio}")
    print(f"  Ruta: {ruta}")