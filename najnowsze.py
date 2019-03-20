
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.graphics.barcode import code39
import xlrd
from barcode import generate
plik = xlrd.open_workbook("numery.xls")
strona = plik.sheet_by_index(0)
total_rows = strona.nrows
c=canvas.Canvas("barcode.pdf",pagesize=A4)
licznik = total_rows // 16

i=0
for d in range(licznik-1):
    c.setFont("Helvetica", 25)
    code = strona.cell(i,0).value
    barcode=code39.Standard39(code,checksum=0,barWidth=0.25*mm,barHeight=30*mm)
#1#1
    barcode.drawOn(c,10*mm,245*mm)
    c.drawString(14*mm,235*mm,code)
    
    i += 1
    code = strona.cell(i,0).value
    barcode=code39.Standard39(code,checksum=0, barWidth=0.25*mm,barHeight=30*mm)
#1#2
    c.drawString(60*mm,250*mm,code)
    barcode.drawOn(c,55*mm,215*mm)
    i += 1
    code = strona.cell(i,0).value
    barcode=code39.Standard39(code,checksum=0, barWidth=0.25*mm,barHeight=30*mm)
    barcode.drawOn(c,100*mm,245*mm)
    c.drawString(105*mm,235*mm,code)
    i += 1
    code = strona.cell(i,0).value
    barcode=code39.Standard39(code,checksum=0, barWidth=0.25*mm,barHeight=30*mm)
    c.drawString(150*mm,250*mm,code)
    barcode.drawOn(c,145*mm,215*mm)
    i += 1
    code = strona.cell(i,0).value
    barcode=code39.Standard39(code,checksum=0, barWidth=0.25*mm,barHeight=30*mm)
    ######
    #####
    barcode.drawOn(c,10*mm,180*mm)
    c.drawString(14*mm,170*mm,code)
    i += 1
    code = strona.cell(i,0).value
    barcode=code39.Standard39(code,checksum=0, barWidth=0.25*mm,barHeight=30*mm)
    c.drawString(60*mm,185*mm,code)
    barcode.drawOn(c,55*mm,150*mm)
    i += 1
    code = strona.cell(i,0).value
    barcode=code39.Standard39(code,checksum=0, barWidth=0.25*mm,barHeight=30*mm)
    barcode.drawOn(c,100*mm,180*mm)
    c.drawString(105*mm,170*mm,code)
    i += 1
    code = strona.cell(i,0).value
    barcode=code39.Standard39(code,checksum=0, barWidth=0.25*mm,barHeight=30*mm)
    c.drawString(150*mm,185*mm,code)
    barcode.drawOn(c,145*mm,150*mm)
    i += 1
    code = strona.cell(i,0).value
    barcode=code39.Standard39(code,checksum=0, barWidth=0.25*mm,barHeight=30*mm)
    #####
    #####

    barcode.drawOn(c,10*mm,117*mm)
    c.drawString(14*mm,108*mm,code)
    i += 1
    code = strona.cell(i,0).value
    barcode=code39.Standard39(code,checksum=0, barWidth=0.25*mm,barHeight=30*mm)
    c.drawString(60*mm,120*mm,code)
    barcode.drawOn(c,55*mm,87*mm)
    i += 1
    code = strona.cell(i,0).value
    barcode=code39.Standard39(code,checksum=0, barWidth=0.25*mm,barHeight=30*mm)
    barcode.drawOn(c,100*mm,117*mm)
    c.drawString(105*mm,108*mm,code)
    i += 1
    code = strona.cell(i,0).value
    barcode=code39.Standard39(code,checksum=0, barWidth=0.25*mm,barHeight=30*mm)
    c.drawString(150*mm,120*mm,code)
    barcode.drawOn(c,145*mm,87*mm)
    i += 1
    code = strona.cell(i,0).value
    barcode=code39.Standard39(code,checksum=0, barWidth=0.25*mm,barHeight=30*mm)



    #######
    #######

    barcode.drawOn(c,10*mm,53*mm)
    c.drawString(14*mm,45*mm,code)
    i += 1
    code = strona.cell(i,0).value
    barcode=code39.Standard39(code,checksum=0, barWidth=0.25*mm,barHeight=30*mm)
    c.drawString(60*mm,55*mm,code)
    barcode.drawOn(c,55*mm,23*mm)
    i += 1
    code = strona.cell(i,0).value
    barcode=code39.Standard39(code,checksum=0, barWidth=0.25*mm,barHeight=30*mm)
    barcode.drawOn(c,100*mm,53*mm)
    c.drawString(105*mm,45*mm,code)
    i += 1
    code = strona.cell(i,0).value
    barcode=code39.Standard39(code,checksum=0, barWidth=0.25*mm,barHeight=30*mm)
    c.drawString(150*mm,55*mm,code)
    barcode.drawOn(c,145*mm,23*mm)
    i += 1
    code = strona.cell(i,0).value
    barcode=code39.Standard39(code,checksum=0, barWidth=0.25*mm,barHeight=30*mm)
    c.showPage()


#####
#####
# now create the actual PDF
c.save()