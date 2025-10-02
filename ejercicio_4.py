"""Extraer URL de un texto y sus dominios"""

import re

def extraer_urls(texto):
    patron = r'((https?://)?(www\.)?[\w.-]+\.\w+(/[^\s]*)?)'
    urls = re.findall(patron, texto)
    resultados = []
    for url in urls:
        protocolo = "http" if url[1] else "N/A"
        dominio = url[2] + url[0].split("://")[-1].split("/")[0] if url[2] else url[0].split("://")[-1].split("/")[0]
        ruta = "/" + "/".join(url[0].split("://")[-1].split("/")[1:]) if "/" in url[0].split("://")[-1] else ""
        resultados.append({"url": url[0], "protocolo": protocolo, "dominio": dominio, "ruta": ruta})
    return resultados

# Ejemplo de texto
texto = "Visita https://www.google.com o http://github.com/usuario."
urls = extraer_urls(texto)
for i, u in enumerate(urls, 1):
    print(f"URL {i}: {u['url']}\n  Protocolo: {u['protocolo']}\n  Dominio: {u['dominio']}\n  Ruta: {u['ruta']}")
