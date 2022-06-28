import time
from PIL import Image
import pytesseract
import numpy as np
import sys
import aspose.words as aw



#cleaner
original_stdout = sys.stdout
cleanertotal = ['2.txt', 'temp.txt' ,'filters.txt']
temp = cleanertotal[1]
for temp in cleanertotal :
    with open(temp, 'w' , encoding="utf-8") as f:
        sys.stdout = f
        f.write("")
        sys.stdout = original_stdout
        f.close();
#body
filters = []
n = int(input("Enter number of Words in each line to search in pdf file : "))
b = print("Enter Words you have to find in each line : ")
for i in range(0, n):
    ele = str(input())
    filters.append(ele) # adding the element
print('Please wait ...')



#convert pdf to jpg
doc = aw.Document('pdf.pdf')    
for page in range(0, doc.page_count):
    extractedPage = doc.extract_pages(page, 1)
    extractedPage.save(f"Output_{page + 1}.jpg")
    #input file name for my for
    filename =(f"Output_{page + 1}.jpg")
    #ai text scanner
    custom_config = r' --psm 4'
    extractedInformation = pytesseract.image_to_string(Image.open(filename) , lang='fas'  , config=custom_config)
    #write to file
    original_stdout = sys.stdout
    with open('2.txt', 'a' , encoding="utf-8") as f:
        sys.stdout = f
        f.write(filename + "\n")
        f.write(extractedInformation)
        sys.stdout = original_stdout
        f.close();

#main
counter = 0;
i = 0;
word=[]
founded=[]
with open('2.txt', encoding="utf-8") as file:
    for line in file:
    
        words = line.split(" ");
        for words in line:
            finalword = "".join(word)
            original_stdout = sys.stdout
            with open('temp.txt',"a", encoding="utf-8") as ffind:
                sys.stdout = ffind
                if words == ("\n") or words == (" "):
                    words = ("")
                    ffind.write("\n")
                    counter = i + 1
                    i = counter
                    filterslen = len(filters)
                    if finalword in filters:
                        with open('filters.txt',"a", encoding="utf-8") as filtersfile:
                            sys.stdout = filtersfile
                            filtersfile.write(finalword + "\n")
                            founded.append(finalword)
                    word=[]
                else:
                    ffind.write(words) 
                    word.append(words)
                    
                sys.stdout = original_stdout    
        original_stdout = sys.stdout
    file.close();
print('\n')
print('Number of All Words : ' + str(counter))
print("Number of Used in File : " + str(len(founded)))


