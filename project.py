import re
from PyPDF2 import PdfMerger, PdfReader

def main():
    # ask user for input file name
    while True:
        inputfile = input("Filename: ")

        # check for pdf file
        if ".pdf" not in inputfile:
            print("Not a PDF file")
            continue

        # read text from input file
        try:
            text = read_input(inputfile)

        # except if the file does not exist
        except FileNotFoundError:
            print("PDF file does not exist")
            continue

        # merge the files with filenames from text
        merger = merge_files(text)

        # write the merged file to pdf
        try:
            write_output(merger, text)

        # except if the file is open, user has no permission
        except PermissionError:
            print("The file is open, close it and try again")
            continue
        break


# function to open and read the input file
def read_input(inputfile):

    # open filepath
    filepath = open(f'search/example record sheet/{inputfile}', 'rb')

    # read the pdf file
    reader = PdfReader(filepath)

    # define first page
    first_page = reader.getPage(0)

    # extract the text from the page and remove any
    # whitespace which may be caused from reading pdf files
    text = first_page.extractText().replace(" ","")

    # return the extracted text
    return text


# function to merge the desired PDF file
def merge_files(text):

    # find and list the batch numbers with format BXXXXX
    batch = re.findall("B[0-9]{5}", text)

    # initialise list of pdf files to be merged
    pdf_files = []

    # loop through the batch numbers and append file directory and
    # pdf extension to create the full filenames of the pdfs
    for filename in batch:
        pdf_files.append(f"merge/material certs/{filename}.pdf")

    # create an instance of PdfMerger() class
    merger = PdfMerger()

    # loop through the pdf_files and merge all results
    for pdf_file in pdf_files:
        merger.append(pdf_file)

    # return the merged file
    return merger


# function to write the merged file to new directory
def write_output(merger, text):

    # part number to be used in the filename of the exported file
    partnumber = re.findall("PN[0-9]{6}", text)[0]

    # write the merged file to desired directory with 
    # suitable filename containing the part number
    merger.write(f"search/merged material certs/{partnumber} material certs.pdf")
    merger.close()


if __name__ == "__main__":
    main()