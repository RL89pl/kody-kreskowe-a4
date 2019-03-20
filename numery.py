from xlwt import Workbook
dokument = Workbook()
Arkusz1 = dokument.add_sheet('Arkusz1',cell_overwrite_ok=True)
pozx = 0
pozy = 0
reg = 1
kol = 1
miejsce = 1
while reg < 15:
    Arkusz1.write(pozx,pozy,("C-{:02}-{:02}-{:02}".format(reg, kol, miejsce)))
    dokument.save('numery.xls')
    miejsce += 1
    pozx += 1
    if miejsce > 4:
        kol += 1
        miejsce = 1
        if kol > 54:
            reg += 1
            kol = 1
        else:
            pass
    else:
        pass

        
    
# pozx += 1
# pozy += 1
# reg += 1
# kol += 1
# miejsce += 1
# dokument.save('numery.xls')