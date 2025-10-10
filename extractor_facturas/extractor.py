import re

def leer_factura(nombre_archivo):
    """Lee el contenido de un archivo de factura"""
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
    return contenido

def extraer_numero_factura(texto):
    """Extrae el número de factura"""
    patron = r'Número de Factura:\s*([\w-]+)'
    match = re.search(patron, texto)
    if match:
        return match.group(1)
    return None

def extraer_fecha(texto):
    """Extrae la fecha en formato DD/MM/YYYY"""
    patron = r'Fecha:\s*(\d{2}/\d{2}/\d{4})'
    match = re.search(patron, texto)
    if match:
        return match.group(1)
    return None

def extraer_datos_cliente(texto):
    """Extrae nombre, RFC y correo del cliente"""
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
    """Extrae la lista de productos con sus detalles"""
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
    """Extrae subtotal, IVA y total"""
    totales = {}
    
    patron_subtotal = r'Subtotal:\s*\$([\d\.]+)'
    match = re.search(patron_subtotal, texto)
    if match:
        totales['subtotal'] = float(match.group(1))
    
    patron_iva = r'IVA.*?\$([\d\.]+)'
    match = re.search(patron_iva, texto)
    if match:
        totales['iva'] = float(match.group(1))
    
    patron_total = r'Total:\s*\$([\d\.]+)'
    match = re.search(patron_total, texto)
    if match:
        totales['total'] = float(match.group(1))
    
    return totales

# --- Solución al Ejercicio Avanzado 1 ---
def extraer_forma_pago(texto):
    """Extrae la forma de pago de la factura"""
    patron = r'Forma de pago:\s*(.+)'
    match = re.search(patron, texto)
    if match:
        # Usamos strip() para limpiar espacios o líneas en blanco
        return match.group(1).strip()
    return None
# --- Fin de la solución ---


def procesar_factura(nombre_archivo):
    """Procesa una factura completa y retorna un diccionario con todos los datos"""
    contenido = leer_factura(nombre_archivo)
    
    factura_datos = {
        'numero_factura': extraer_numero_factura(contenido),
        'fecha': extraer_fecha(contenido),
        'cliente': extraer_datos_cliente(contenido),
        'productos': extraer_productos(contenido),
        'totales': extraer_totales(contenido),
        'forma_pago': extraer_forma_pago(contenido) # Integración del nuevo dato
    }
    
    return factura_datos

def imprimir_resumen(factura_datos):
    """Imprime un resumen bonito de la factura"""
    print("\n" + "="*50)
    print(f"FACTURA: {factura_datos['numero_factura']}")
    print(f"FECHA: {factura_datos['fecha']}")
    print("="*50)
    
    print(f"\nCLIENTE: {factura_datos['cliente']['nombre']}")
    print(f"RFC: {factura_datos['cliente']['rfc']}")
    print(f"Email: {factura_datos['cliente']['correo']}")
    
    print(f"\nPRODUCTOS ({len(factura_datos['productos'])} items):")
    for prod in factura_datos['productos']:
        # :30 alinea el texto a la izquierda, >8.2f alinea el número a la derecha
        print(f"  • {prod['nombre']:30} ${prod['total']:>8.2f}")
    
    print(f"\nSUBTOTAL: ${factura_datos['totales']['subtotal']:>10.2f}")
    print(f"IVA:      ${factura_datos['totales']['iva']:>10.2f}")
    print(f"TOTAL:    ${factura_datos['totales']['total']:>10.2f}")
    
    # Imprimir la forma de pago
    if factura_datos['forma_pago']:
        print(f"\nFORMA DE PAGO: {factura_datos['forma_pago']}")
        
    print("="*50)

# Programa principal
if __name__ == "__main__":
    # Procesar las tres facturas
    for i in range(1, 4):
        nombre = f'factura{i}.txt'
        print(f"Procesando {nombre}...")
        datos = procesar_factura(nombre)
        imprimir_resumen(datos)