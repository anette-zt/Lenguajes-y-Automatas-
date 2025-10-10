import re
import json

def leer_factura(nombre_archivo):
    """Lee el contenido de un archivo de factura."""
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
    return contenido

def extraer_numero_factura(texto):
    """Extrae el número de factura."""
    patron = r'Número de Factura:\s*([\w-]+)'
    match = re.search(patron, texto)
    if match:
        return match.group(1)
    return None

def extraer_fecha(texto):
    """Extrae la fecha en formato DD/MM/YYYY."""
    patron = r'Fecha:\s*(\d{2}/\d{2}/\d{4})'
    match = re.search(patron, texto)
    if match:
        return match.group(1)
    return None

def extraer_datos_cliente(texto):
    """Extrae nombre, RFC y correo del cliente."""
    cliente = {}
    patron_nombre = r'Cliente:\s*(.+)'
    match_nombre = re.search(patron_nombre, texto)
    if match_nombre:
        cliente['nombre'] = match_nombre.group(1).strip()
    
    patron_rfc = r'RFC Cliente:\s*(\w+)'
    match_rfc = re.search(patron_rfc, texto)
    if match_rfc:
        cliente['rfc'] = match_rfc.group(1)
    
    patron_correo = r'Correo:\s*([\w._%+-]+@[\w.-]+\.\w+)'
    match_correo = re.search(patron_correo, texto)
    if match_correo:
        cliente['correo'] = match_correo.group(1)
    
    return cliente

def extraer_productos(texto):
    """Extrae la lista de productos con sus detalles."""
    productos = []
    patron = r'\d+\.\s+(.+?)\s+\$(\d+\.\d{2})\s+x(\d+)\s+\$(\d+\.\d{2})'
    matches = re.findall(patron, texto)
    for match in matches:
        producto = {
            'nombre': match[0].strip(),
            'precio_unitario': float(match[1]),
            'cantidad': int(match[2]),
            'total': float(match[3])
        }
        productos.append(producto)
    return productos

def extraer_totales(texto):
    """Extrae subtotal, IVA y total."""
    totales = {}
    patron_subtotal = r'Subtotal:\s*\$(\d+\.\d{2})'
    match = re.search(patron_subtotal, texto)
    if match:
        totales['subtotal'] = float(match.group(1))
    
    patron_iva = r'IVA.*?\$(\d+\.\d{2})'
    match = re.search(patron_iva, texto)
    if match:
        totales['iva'] = float(match.group(1))
    
    patron_total = r'Total:\s*\$(\d+\.\d{2})'
    match = re.search(patron_total, texto)
    if match:
        totales['total'] = float(match.group(1))
    
    return totales

# --- Ejercicios Adicionales ---

def extraer_forma_pago(texto):
    """Ejercicio Avanzado 1: Extrae la forma de pago."""
    patron = r'Forma de pago:\s*(.+)'
    match = re.search(patron, texto)
    if match:
        # Usamos strip() para eliminar posibles espacios o saltos de línea al final
        return match.group(1).strip()
    return None

def validar_totales(factura_datos):
    """Ejercicio Avanzado 2: Valida que los cálculos sean correctos."""
    subtotal = factura_datos['totales'].get('subtotal', 0)
    iva = factura_datos['totales'].get('iva', 0)
    total_calculado = subtotal + iva
    total_factura = factura_datos['totales'].get('total', 0)
    
    # Se compara redondeando a 2 decimales para evitar problemas con la precisión de los flotantes
    if round(total_calculado, 2) == round(total_factura, 2):
        return True, total_calculado
    return False, total_calculado

def guardar_json(factura_datos, nombre_salida):
    """Ejercicio Avanzado 3: Guarda los datos en formato JSON."""
    with open(nombre_salida, 'w', encoding='utf-8') as f:
        json.dump(factura_datos, f, indent=2, ensure_ascii=False)

# --- Funciones Principales ---

def procesar_factura(nombre_archivo):
    """Procesa una factura completa y retorna un diccionario con todos los datos."""
    contenido = leer_factura(nombre_archivo)
    factura_datos = {
        'archivo_origen': nombre_archivo,
        'numero_factura': extraer_numero_factura(contenido),
        'fecha': extraer_fecha(contenido),
        'cliente': extraer_datos_cliente(contenido),
        'productos': extraer_productos(contenido),
        'totales': extraer_totales(contenido),
        'forma_pago': extraer_forma_pago(contenido) # Dato del ejercicio avanzado
    }
    return factura_datos

def imprimir_resumen(factura_datos):
    """Imprime un resumen bonito de la factura."""
    print("\n" + "="*50)
    print(f"FACTURA: {factura_datos['numero_factura']}")
    print(f"FECHA: {factura_datos['fecha']}")
    print("="*50)
    
    cliente = factura_datos.get('cliente', {})
    print(f"\nCLIENTE: {cliente.get('nombre')}")
    print(f"RFC: {cliente.get('rfc')}")
    print(f"Email: {cliente.get('correo')}")
    
    print(f"\nPRODUCTOS ({len(factura_datos.get('productos', []))} items):")
    for prod in factura_datos.get('productos', []):
        print(f"  • {prod['nombre']:30} ${prod['total']:>8.2f}")
    
    totales = factura_datos.get('totales', {})
    print(f"\nSUBTOTAL: ${totales.get('subtotal', 0):>10.2f}")
    print(f"IVA:      ${totales.get('iva', 0):>10.2f}")
    print(f"TOTAL:    ${totales.get('total', 0):>10.2f}")

    print(f"\nForma de Pago: {factura_datos.get('forma_pago', 'No especificada')}")
    print("="*50)

# Programa principal
if __name__ == "__main__":
    archivos_facturas = [f'factura{i}.txt' for i in range(1, 4)]
    
    for nombre_archivo in archivos_facturas:
        print(f"\nProcesando {nombre_archivo}...")
        datos = procesar_factura(nombre_archivo)
        imprimir_resumen(datos)
        
        # Validación de totales (Ejercicio Avanzado 2)
        es_valido, total_calculado = validar_totales(datos)
        if es_valido:
            print(" Verificación de totales: Subtotal + IVA coincide con el Total.")
        else:
            print(f" Verificación de totales: ¡ERROR! Suma calculada ${total_calculado:.2f}, Total en factura ${datos['totales']['total']:.2f}")
