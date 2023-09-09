import time

class Caesar:
    def __init__(self):
        
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.keySpace = len(self.alphabet)
        
    
    def encryption(self, text, k):
        # x + k mod 26
        tmpList = list(text)

        for i in range(0, len(tmpList)):
            if not tmpList[i] in self.alphabet:
                continue
            x = self.alphabet.index(tmpList[i])
            if (x + (k % self.keySpace) > self.keySpace - 1):
                moduloRes = self.alphabet[0 + (k % self.keySpace) - (self.keySpace - 1 - x) - 1]
                tmpList[i] = moduloRes
            else:
                moduloRes = self.alphabet[x + (k % self.keySpace)]
                tmpList[i] = moduloRes
        last = "".join(tmpList)
        print("Encrypted message : " + last)

    def decryption(self, text, k):
        # y - k mod 26
        tmpList = list(text)

        for i in range(0, len(tmpList)):
            
            if not tmpList[i] in self.alphabet:
                continue
            else:
                y = self.alphabet.index(tmpList[i])
                
                if (y - (k % self.keySpace) < 0):
                    moduloRes = self.alphabet[self.keySpace - ((k % self.keySpace) - y)]
                    tmpList[i] = moduloRes
                else:
                    moduloRes = self.alphabet[y - (k % self.keySpace)]
                    
                    tmpList[i] = moduloRes
                    
                    
        last = "".join(tmpList)
        print("Decrypted message : " + last)

        




print("""
  ___ __ _  ___  ___  __ _ _ __ 
 / __/ _` |/ _ \/ __|/ _` | '__|
| (_| (_| |  __/\__ \ (_| | |   
 \___\__,_|\___||___/\__,_|_|
                        By Batuhan Dilek   """)
print("\n\n\n")

if(int(input("Enter '1' to encrypt, enter '0' to decrypt : "))):


    inpStr = input("enter the text : ")
    k = -1
    while (k <= 0):
        k = int(input("Enter the shift amount : "))
        if(k <= 0):
            print("shift amount must be bigger than 0")
    a = Caesar()
    timerStart = time.perf_counter()
    a.encryption(inpStr, k)
    timerEnd = time.perf_counter()
    timer = timerEnd - timerStart

    print(f"It took {timer:0.4f} seconds to encrypt")
else:
    inpStr = input("enter the text : ")
    k = -1
    while (k <= 0):
        k = int(input("Enter the shift amount : "))
        if(k <= 0):
            print("shift amount must be bigger than 0")
    a = Caesar()
    timerStart = time.perf_counter()
    a.decryption(inpStr, k)
    timerEnd = time.perf_counter()
    timer = timerEnd - timerStart
    print(f"It took {timer:0.4f} seconds to decipher")


