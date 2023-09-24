import PyPDF2

def pdf(file):
    # Ruta al archivo PDF que deseas abrir

    # Inicializar una variable para almacenar el texto
    text = ''

    # Abrir el archivo PDF
    with open(file, 'rb') as pdf_file:
        # Crear un objeto PdfReader en lugar de PdfFileReader
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Leer cada página del PDF
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    # Imprimir o almacenar el texto en una variable
    print(text)
    return text

