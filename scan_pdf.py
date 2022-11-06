import PyPDF2


def metadata(file, output):
    pdfFile = PyPDF2.PdfFileReader(file, 'rb')
    data = pdfFile.getDocumentInfo()
    output.write("----PDF metadata----" )

    for metadata in data:
        output.write(metadata + ": " + data[metadata])
    
    return
