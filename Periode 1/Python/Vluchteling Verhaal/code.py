import io
import os
code = open("tekstcode.txt", "r", errors='ignore')
output = open("output.txt", "w", errors='ignore')
regels = sum(1 for line in open('tekstcode.txt'))
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
                
                tekst = code.readline().strip()
                line += 1
                if not tekst == "CODE::":
                    output.write(tabs + tekst + "\n")
                else:
                    break

        
        
        
        output.write(tabs + "print(\""+ tekst + "\")\n")
        line += 1
        
    
    if line == regels:
        code = open("tekstcode.txt", "r", errors='ignore')
        output = open("output.txt", "w", errors='ignore')
        line = 0
        print()
        input("Klaar")
        
        os.system("cls")
        
        