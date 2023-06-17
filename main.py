
#PDF LERİ DOCX E DÖNÜŞTÜRME
#pdf-to-docx

from pdf2docx import Converter

pdf_path="sample.pdf"
docx_path="sample.docx"

#CONVERTER sınıfından cv adında obje oluşturalım
cv =Converter(pdf_file=pdf_path)
cv.convert(docx_filename=docx_path)
cv.close()