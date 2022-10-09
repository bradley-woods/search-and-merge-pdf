import re
from PyPDF2 import PdfMerger, PdfReader

def main():

    filen = input("Filename: ") 
    #Create and instance of PdfFileMerger() class
    merger = PdfMerger()


    temp = open(f'search/example record sheet/{filen}', 'rb')
    reader = PdfReader(temp)

    first_page = reader.getPage(0)

    text = first_page.extractText().replace(" ","")

    headr = re.findall("PN[0-9]{6}", text)[0]
    print(headr)
    batch = re.findall("B[0-9]{5}", text)

    pdf_files = []
    for filename in batch:
        pdf_files.append(f"merge/material certs/{filename}.pdf")

    print(pdf_files)

    for pdf_file in pdf_files:
        merger.append(pdf_file)

    merger.write(f"search/merged material certs/{headr} material certs.pdf")
    merger.close()


    #Create a list with file names



    #pdf_files = ['pdf_files/sample_page1.pdf', 'pdf_files/sample_page2.pdf']

    #Iterate over the list of file names
    #for pdf_file in pdf_files:
        #Append PDF files
    #   merger.append(pdf_file)

    #Write out the merged PDF
    #merger.write("merged_2_pages.pdf")
    #merger.close()





#def input():



#def merge():



#def output():


if __name__ == "__main__":
    main()