from pypdf import PdfMerger, PdfReader
import os

percorso = "/home/nick/Desktop/alius/allegati/"
merger = PdfMerger()
'''
for filename in percorso:
    for file in filename
    merger.append(PdfReader(open(filename, 'rb')))
'''

listafile = []
try:
    for path, dir, files in os.walk(percorso):
        if files:
            for file in files:
                print(path + file)
                listafile.append(path + file)
                #merger.append(PdfReader(open(path + file, 'rb')))
                #PdfReader(open(file, 'rb'))
          
except Exception as e:
    print(e)

listafile.sort()
for el in listafile:
    merger.append(PdfReader(open(el, 'rb')))
    
merger.write("/home/nick/Desktop/alius/allegati/Programma uscieri giugno.pdf")

print("OK")


'''
/home/nick/Desktop/AHI python/document-output.pdf
/home/nick/Desktop/AHI python/document-output.pdf
/home/nick/Desktop/AHI python/document-output.pdf
/home/nick/Desktop/AHI python/document-output.pdf
'''