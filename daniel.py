import PyPDF2
import os

def unir_pdfs(ruta_directorio, salida):
    # Crear un objeto PdfWriter para el archivo de salida
    pdf_salida = PyPDF2.PdfWriter()

    # Obtener una lista de todos los archivos PDF en el directorio
    archivos_pdf = [nombre for nombre in os.listdir(ruta_directorio) if nombre.endswith('.pdf')]

    # Ordenar los archivos PDF por tamaño (de menor a mayor)
    archivos_pdf.sort(key=lambda nombre: os.path.getsize(os.path.join(ruta_directorio, nombre)))

    # Para cada archivo en la lista ordenada
    for nombre_archivo in archivos_pdf:
        # Crear un objeto PdfFileReader para el archivo PDF
        pdf = PyPDF2.PdfReader(os.path.join(ruta_directorio, nombre_archivo))

        # Añadir las páginas del PDF al archivo de salida
        for pagina in range(len(pdf.pages)):
            pdf_salida.add_page(pdf.pages[pagina])

    # Escribir el archivo de salida
    with open(salida, 'wb') as f:
        pdf_salida.write(f)

ruta = './SOPORTES'
archivos = os.listdir(ruta)

# archivos es la variable que guarda el numero de documento de los pacientes
cedulas = [archivo.split(' ')[0] for archivo in archivos]

for ruta, cedula in zip(archivos, cedulas):
    # Ruta al directorio con los archivos PDF
    ruta_directorio = f'./SOPORTES/{ruta}'

    # Ruta al archivo de salida
    salida = f'./FINAL/{cedula}.pdf'

    # Llamar a la función para unir los PDFs
    unir_pdfs(ruta_directorio, salida)