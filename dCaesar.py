print("""     
     888  .d8888b.                                              
     888 d88P  Y88b                                             
     888 888    888                                             
 .d88888 888         8888b.   .d88b.  .d8888b   8888b.  888d888 
d88" 888 888            "88b d8P  Y8b 88K          "88b 888P"   
888  888 888    888 .d888888 88888888 "Y8888b. .d888888 888     
Y88b 888 Y88b  d88P 888  888 Y8b.          X88 888  888 888     
 "Y88888  "Y8888P"  "Y888888  "Y8888   88888P' "Y888888 888     
                                                          By Batuhan Dilek     """)
print("\n\n\n")

import time

class DCaesar:
    def __init__(self):
        
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.keySpace = len(self.alphabet)
        
    
    def encryption(self, text):
        # x + k mod 26
        tmpList = list(text)

        for i in range(0, len(tmpList)):
            if not tmpList[i] in self.alphabet:
                continue
            x = self.alphabet.index(tmpList[i])
            if (x + (13 % self.keySpace) > self.keySpace - 1):
                moduloRes = self.alphabet[0 + (13 % self.keySpace) - (self.keySpace - 1 - x) - 1]
                tmpList[i] = moduloRes
            else:
                moduloRes = self.alphabet[x + (13 % self.keySpace)]
                tmpList[i] = moduloRes

        for i in range(0, len(tmpList)):
            if not tmpList[i] in self.alphabet:
                continue
            x = self.alphabet.index(tmpList[i])
            if (x + (9 % self.keySpace) > self.keySpace - 1):
                moduloRes = self.alphabet[0 + (9 % self.keySpace) - (self.keySpace - 1 - x) - 1]
                tmpList[i] = moduloRes
            else:
                moduloRes = self.alphabet[x + (9 % self.keySpace)]
                tmpList[i] = moduloRes
        last = "".join(tmpList)
        print("Encrypted message : " + last)

    def decryption(self, text):
        # y - k mod 26
        tmpList = list(text)

        for i in range(0, len(tmpList)):
            
            if not tmpList[i] in self.alphabet:
                continue
            else:
                y = self.alphabet.index(tmpList[i])
                
                if (y - (9 % self.keySpace) < 0):
                    moduloRes = self.alphabet[self.keySpace - ((9 % self.keySpace) - y)]
                    tmpList[i] = moduloRes
                else:
                    moduloRes = self.alphabet[y - (9 % self.keySpace)]
                    
                    tmpList[i] = moduloRes

        for i in range(0, len(tmpList)):
            
            if not tmpList[i] in self.alphabet:
                continue
            else:
                y = self.alphabet.index(tmpList[i])
                
                if (y - (13 % self.keySpace) < 0):
                    moduloRes = self.alphabet[self.keySpace - ((13 % self.keySpace) - y)]
                    tmpList[i] = moduloRes
                else:
                    moduloRes = self.alphabet[y - (13 % self.keySpace)]
                    
                    tmpList[i] = moduloRes
                    
                    
        last = "".join(tmpList)
        print("Decrypted message : " + last)

if(int(input("Enter '1' to encrypt, enter '0' to decrypt : "))):


    inpStr = input("enter the text : ")
    a = DCaesar()
    timerStart = time.perf_counter()
    a.encryption(inpStr)
    timerEnd = time.perf_counter()
    timer = timerEnd - timerStart

    print(f"It took {timer:0.4f} seconds to encrypt")
else:
    inpStr = input("enter the text : ")
    
    a = DCaesar()
    timerStart = time.perf_counter()
    a.decryption(inpStr)
    timerEnd = time.perf_counter()
    timer = timerEnd - timerStart
    print(f"It took {timer:0.4f} seconds to decipher")
