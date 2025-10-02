"""Deteccion y Conversion de Fechas"""

import re
from datetime import datetime

# Map de meses en español a número
meses = {
    "Enero": "01", "Febrero": "02", "Marzo": "03", "Abril": "04",
    "Mayo": "05", "Junio": "06", "Julio": "07", "Agosto": "08",
    "Septiembre": "09", "Octubre": "10", "Noviembre": "11", "Diciembre": "12",
    "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
    "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
    "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
}

def formatear_fecha(fecha):
    # DD/MM/YYYY
    match = re.match(r'(\d{2})/(\d{2})/(\d{4})', fecha)
    if match:
        return f"{match[3]}-{match[2]}-{match[1]}"
    # YYYY-MM-DD
    match = re.match(r'(\d{4})-(\d{2})-(\d{2})', fecha)
    if match:
        return f"{match[1]}-{match[2]}-{match[3]}"
    # DD-MMM-YYYY
    match = re.match(r'(\d{2})-([A-Za-z]{3})-(\d{4})', fecha)
    if match:
        mes = meses.get(match[2].title(), "01")
        return f"{match[3]}-{mes}-{match[1]}"
    # Mes DD, YYYY
    match = re.match(r'([A-Za-z]+) (\d{2}), (\d{4})', fecha)
    if match:
        mes = meses.get(match[1].title(), "01")
        return f"{match[3]}-{mes}-{match[2]}"
    return "Formato desconocido"

texto = "La reunión es el 15/03/2024. El proyecto inicia el 2024-04-20 y termina en Junio 30, 2024. La entrega final es 01-Jul-2024."
fechas = re.findall(r'(\d{2}/\d{2}/\d{4}|\d{4}-\d{2}-\d{2}|\d{2}-[A-Za-z]{3}-\d{4}|[A-Za-z]+ \d{2}, \d{4})', texto)

print("Fechas encontradas y convertidas:")
for f in fechas:
    estandar = formatear_fecha(f)
    print(f"- Formato original: {f} → Estándar: {estandar}")
    try:
        datetime.strptime(estandar, "%Y-%m-%d")
    except ValueError:
        print(f"  ¡Error! La fecha {f} no es válida.")