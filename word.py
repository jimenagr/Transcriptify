import docx

def word(d):
    # Ruta al archivo .docx que deseas abrir
    #docx_file_path = r'C:\Users\ramon\OneDrive\Desktop\Tesseract\Portada.docx'

    # Inicializar el objeto Document
    doc = docx.Document(d)

    # Inicializar una variable para almacenar el texto
    text = ''

    # Iterar a través de los párrafos del documento y extraer el texto
    for paragraph in doc.paragraphs:
        text += paragraph.text + '\n'  # Puedes ajustar el formato según tus necesidades

    # Imprimir o almacenar el texto en una variable
    return text
