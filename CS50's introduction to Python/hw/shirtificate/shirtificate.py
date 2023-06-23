from fpdf import FPDF

'''
:ref https://youtu.be/CASv-fUUqcA
:ref https://cs50.harvard.edu/python/2022/psets/8/shirtificate/#cs50-shirtificate
'''

name = input("Name: ")
pdf = FPDF()
pdf.add_page()
pdf.output("Shirtificate.pdf")