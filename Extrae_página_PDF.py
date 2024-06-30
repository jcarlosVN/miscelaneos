import PyPDF2

def extraer_pagina(input_pdf, pagina, output_pdf):
    with open(input_pdf, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        writer = PyPDF2.PdfFileWriter()
        
        if pagina < 0 or pagina >= reader.getNumPages():
            raise ValueError("Número de página inválido")
        
        # app page
        writer.addPage(reader.getPage(pagina))
        
        # save page
        with open(output_pdf, 'wb') as output_file:
            writer.write(output_file)
            print(f"Se extrajo la página {pagina} y se guardó en {output_pdf}")


input_pdf = './extrae_PDF/Asis_y_vot_de_la_sesión_del_13-6-2024.pdf'
pagina = 2  # El número de la página que quieres extraer (0-indexado)
output_pdf = f'./extrae_PDF/pagina_extraida {pagina}.pdf'

try:
    extraer_pagina(input_pdf, pagina, output_pdf)
except ValueError as e:
    print(f"Error: {e}")
