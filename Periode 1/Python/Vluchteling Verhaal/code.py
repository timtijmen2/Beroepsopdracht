import io
import os
import time
code = open("tekstcode.txt", "r", encoding='utf-8')
output = open("output.txt", "w", encoding='utf-8')
regels = sum(1 for line in open('tekstcode.txt', encoding='utf-8'))
line = 0
tabsaantal = 0
tabs = ""
while True:
    
    if line < regels:
        tekst = code.readline().strip()
        if tekst == "[]":
            tabsaantal += 1
            if tabsaantal == 1:
                tabs = "\t"
            elif tabsaantal == 2:
                tabs = "\t\t"
            elif tabsaantal == 3:
                tabs = "\t\t\t"
        elif tekst == "[/]":
            tabsaantal -= 1
            if tabsaantal == 1:
                tabs = "\t"
            elif tabsaantal == 2:
                tabs = "\t\t"
            elif tabsaantal == 3:
                tabs = "\t\t\t"
        
        if tekst == "CODE:":
            line += 1
            while True:
                if tekst == "[]":
                    tabsaantal += 1
                if tabsaantal == 1:
                    tabs = "\t"
                elif tabsaantal == 2:
                    tabs = "\t\t"
                elif tabsaantal == 3:
                   tabs = "\t\t\t"
                elif tekst == "[/]":
                   tabsaantal -= 1
                if tabsaantal == 1:
                    tabs = "\t"
                elif tabsaantal == 2:
                    tabs = "\t\t"
                elif tabsaantal == 3:
                    tabs = "\t\t\t"
                elif tabsaantal == 4:
                    tabs = "\t\t\t\t"
                
                line += 1
                if not tekst == "CODE::":
                    tekst = code.readline().strip()
                    output.write(tabs + tekst + "\n")
                else:
                    tekst = code.readline().strip()
                    break

        
        
        
        output.write(tabs + "print(\""+ tekst + "\")\n")
        line += 1
        print(line)
        time.sleep(0.1)
    if line == regels:
        code = open("tekstcode.txt", "r", encoding='utf-8')
        output = open("output.txt", "w", encoding='utf-8')
        line = 0
        print()
        input("Klaar")
        
        os.system("cls")
        
        