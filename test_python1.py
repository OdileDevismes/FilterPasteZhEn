
import os, csv, re
from  more_itertools import unique_everseen

def cleanFile(file,newline='',encoding="utf8"):
    inputFile = open(file,newline=newline,encoding=encoding)
    logFile = open("input/"+file+'_log.txt','w',encoding=encoding)
    logNbFile = open("input/"+file+'_logNb.txt','w',encoding=encoding)
    outputFile = open("input/"+file+'_out.txt','w',encoding=encoding)    

    alignedLines = []
    newLines = []

    with inputFile:
        for row in csv.reader(inputFile, delimiter='\t'):
            alignedLines.append(row)
    #print(alignedLines)
        
    def isComplete(line):
        """si la 1re et la 2e colonne sont non vides, renvoie true / sinon, renvoie false"""
        return (line[0] and line[1])

    def isBigEnough(line):
        """si la 1re colonne ou la 2e colonne fait moins de 16 caractères"""
        if (((len(line[0])) > 15) and ((len(line[1])) > 8)):
            return (line[0] and line[1])
 
    def contains1Nb(line):
        """si 1 seul segment contient au moins un chiffre => on veut éliminer la ligne"""
        enText = line[0]
        zhText = line[1]
        if ((re.search("[0-9]",enText)) and not (re.search("[0-9一十百千萬億二三四五六七八九]",zhText))):
            return True
            #print('BAD_zh\t'+enText+"\t"+zhText)
        elif (not(re.search("[0-9]",enText)) and (re.search("[0-9一十百千萬億二三四五六七八九]",zhText))):
            return True
            #print('BAD_en\t'+enText+"\t"+zhText)
        
    def contains2Nb(line):
        """si les 2 segments contiennent au moins un chiffre"""
        enText = line[0]
        zhText = line[1]
        if ((re.search("[0-9]",enText)) and (re.search("[0-9一十百千萬億二三四五六七八九]",zhText))):
            return True
            #print('OK\t'+enText+"\t"+zhText)
        
    def containsDifferentNumbers(line):
        """si un chiffre est présent dans un seul des 2 segments"""
        if contains2Nb(line):
            enText = line[0]
            zhText = line[1]
            # chiffre manquant dans le segment zh
            if ((re.search("1",enText)) and not(re.search("[1十百千萬億]",zhText))):
                logNbFile.write("BAD_zh_1\t"+enText+"\t"+zhText+"\n")
                return True
                #print("BAD_zh_1\t"+enText+"\t"+zhText)
            elif ((re.search("2",enText)) and not(re.search("[2二]",zhText))):
                logNbFile.write("BAD_zh_2\t"+enText+"\t"+zhText+"\n")
                return True
                #print("BAD_zh_2\t"+enText+"\t"+zhText)
            elif ((re.search("3",enText)) and not(re.search("[3三]",zhText))):
                logNbFile.write("BAD_zh_3\t"+enText+"\t"+zhText+"\n")
                return True
                #print("BAD_zh_3\t"+enText+"\t"+zhText)
            elif ((re.search("4",enText)) and not(re.search("[4四]",zhText))):
                logNbFile.write("BAD_zh_4\t"+enText+"\t"+zhText+"\n")
                return True
                #print("BAD_zh_4\t"+enText+"\t"+zhText)
            elif ((re.search("5",enText)) and not(re.search("[5五]",zhText))):
                logNbFile.write("BAD_zh_5\t"+enText+"\t"+zhText+"\n")
                return True
                #print("BAD_zh_5\t"+enText+"\t"+zhText)   
            elif ((re.search("6",enText)) and not(re.search("[6六]",zhText))):
                logNbFile.write("BAD_zh_6\t"+enText+"\t"+zhText+"\n")
                return True
                #print("BAD_zh_6\t"+enText+"\t"+zhText)
            elif ((re.search("7",enText)) and not(re.search("[7七]",zhText))):
                logNbFile.write("BAD_zh_7\t"+enText+"\t"+zhText+"\n")
                return True
                #print("BAD_zh_7\t"+enText+"\t"+zhText)    
            elif ((re.search("8",enText)) and not(re.search("[8八]",zhText))):
                logNbFile.write("BAD_zh_8\t"+enText+"\t"+zhText+"\n")
                return True
                #print("BAD_zh_8\t"+enText+"\t"+zhText)
            elif ((re.search("9",enText)) and not(re.search("[9九]",zhText))):
                logNbFile.write("BAD_zh_9\t"+enText+"\t"+zhText+"\n")
                return True
                #print("BAD_zh_9\t"+enText+"\t"+zhText)
            # chiffre manquant dans le segment en
            elif (not(re.search("1",enText)) and (re.search("1",zhText))):
                logNbFile.write("BAD_en_1\t"+enText+"\t"+zhText+"\n")
                return True
                #print("BAD_en_1\t"+enText+"\t"+zhText)
            elif (not(re.search("2",enText)) and (re.search("[2二]",zhText))):
                logNbFile.write("BAD_en_2\t"+enText+"\t"+zhText+"\n")
                return True
                #print("BAD_en_2\t"+enText+"\t"+zhText)
            elif (not(re.search("3",enText)) and (re.search("[3三]",zhText))):
                logNbFile.write("BAD_en_3\t"+enText+"\t"+zhText+"\n")
                return True
                #print("BAD_en_3\t"+enText+"\t"+zhText)
            elif (not(re.search("4",enText)) and (re.search("[4四]",zhText))):
                logNbFile.write("BAD_en_4\t"+enText+"\t"+zhText+"\n")
                return True
                #print("BAD_en_4\t"+enText+"\t"+zhText)
            elif (not(re.search("5",enText)) and (re.search("[5五]",zhText))):
                logNbFile.write("BAD_en_5\t"+enText+"\t"+zhText+"\n")
                return True
                #print("BAD_en_5\t"+enText+"\t"+zhText)   
            elif (not(re.search("6",enText)) and (re.search("[6六]",zhText))):
                logNbFile.write("BAD_en_6\t"+enText+"\t"+zhText+"\n")
                return True
                #print("BAD_en_6\t"+enText+"\t"+zhText)
            elif (not(re.search("7",enText)) and (re.search("[7七]",zhText))):
                logNbFile.write("BAD_en_7\t"+enText+"\t"+zhText+"\n")
                return True
                #print("BAD_en_7\t"+enText+"\t"+zhText)    
            elif (not(re.search("8",enText)) and (re.search("[8八]",zhText))):
                logNbFile.write("BAD_en_8\t"+enText+"\t"+zhText+"\n")
                return True
                #print("BAD_en_8\t"+enText+"\t"+zhText)
            elif (not(re.search("9",enText)) and (re.search("[9九]",zhText))):
                logNbFile.write("BAD_en_9\t"+enText+"\t"+zhText+"\n")
                return True
                #print("BAD_en_9\t"+enText+"\t"+zhText)

    for line in alignedLines:    
        if (line): # si la ligne n'est pas vide
            if (isComplete(line) and isBigEnough(line) and not(contains1Nb(line)) and not(containsDifferentNumbers(line))):
                newLine = line[0],line[1]
                newLines.append(newLine)
            elif not(isComplete(line)):
                logFile.write('INCOMPLETE\t'+line[0]+"\t"+line[1]+"\n")
            elif not(isBigEnough(line)):
                logFile.write('TOO SHORT\t'+line[0]+"\t"+line[1]+"\n")
            elif (contains1Nb(line)):
                logFile.write('MISSING NB\t'+line[0]+"\t"+line[1]+"\n")
            elif (containsDifferentNumbers(line)):
                logFile.write('DIFFERENT NB\t'+line[0]+"\t"+line[1]+"\n")
    #print('alignedLines =',len(alignedLines),'lignes\n')
    #print('newLines =',len(newLines),'lignes\n')

    #dédoublonnage et écriture de la sortie
    for line in unique_everseen(newLines):
        outputFile.write(line[0]+"\t"+line[1]+"\n")

    # si je veux compter les lignes après dédoublonnage pour vérif, réactiver ci-dessous au lieu de ci-dessus
    #newLines2 = list(unique_everseen(newLines))
    #for line in newLines2:
    #    outputFile.write(line[0]+"\t"+line[1]+"\n")
    #print('newLines2 =',len(newLines2),'lignes\n')
    
    #print(file)

    logFile.close()
    logNbFile.close()
    outputFile.close()

files = os.listdir("input")
#print(files)
for file in (files):
    if (re.search("\.txt$",file)):
        print(file)
        cleanFile("input/"+file)
#cleanFile("input/gemini__HTML___LF-Aligner.txt")
