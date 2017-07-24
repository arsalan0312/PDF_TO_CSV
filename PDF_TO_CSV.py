import PyPDF2
import os
import  csv
def main():
    pdfPath("Z:/KIBOR_RATE_PDF_FILE/kibor-20-Jul-17.pdf")

def pdfPath(pathFile):
    try:
        file = open(pathFile,'rb')
        pdfData = PyPDF2.PdfFileReader(file)
        number_of_pages = pdfData.getNumPages()
        page = pdfData.getPage(0)
        print(number_of_pages)
        page_Content = page.extractText()
        print(page_Content)
        page_content_text(page.extractText)



    except Exception as e:
        print(e)

def page_content_text(text):
    try:
        with open ('file.csv', 'wb') as file:
            writer = csv.writer(file, delimiter=',')
            for line in text:
                writer.writerow (line)
            # for line in text:
            #     file.write (line)
            #     file.write ('\n')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()