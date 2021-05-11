# pdf_merging.py

from PyPDF2 import PdfFileReader, PdfFileWriter
import os


def merge_pdfs(paths, output):
    pdf_writer = PdfFileWriter()
    paths = [os.path.expanduser(path) for path in paths]

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF
    with open(os.path.expanduser(output), "wb") as out:
        pdf_writer.write(out)


if __name__ == "__main__":
    paths = [
        "~/Documents/Home Loan Documents/latest_pay_slips/PayAdvice_20210404_P_1067817993.pdf",
        "~/Documents/Home Loan Documents/latest_pay_slips/PayAdvice_20210328_P_1067817482.pdf",
        "~/Documents/Home Loan Documents/latest_pay_slips/PayAdvice_20210321_P_1067816911.pdf",
        "~/Documents/Home Loan Documents/latest_pay_slips/PayAdvice_20210314_P_1067816396.pdf",
    ]

    merge_pdfs(
        paths,
        output="~/Documents/Home Loan Documents/latest_pay_slips/mamatha_payslip.pdf",
    )
