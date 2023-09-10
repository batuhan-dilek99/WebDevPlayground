from sympy.ntheory.factor_ import totient
class Affine:

    def __init__(self):
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.keySpace = 26

    def encrypt(self,text,keys):
        # E(x) = (ax + b) mod 26
        tmpList = list(text)
        encryptedText = []
        for letter in tmpList:
            if (not letter in self.alphabet):
                continue
            enc = ((keys[0] * self.alphabet.index(letter)) + keys[1]) % self.keySpace
            encryptedText.append(self.alphabet[enc])

        last = "".join(encryptedText)
        print(last)

    def modInverse(self, x):
        table =[[1,3,5,7,9,11,15,17,19,21,23,25], [1,9,21,15,3,19,7,23,11,5,17,25]] 
        index = table[0].index(x)
        result = table[1][index]
        return(result)

    def decrypt(self, text, keys):
        #D(x) = c(y-b)mod26
        modInv = self.modInverse(keys[0])
        
        tmpList = list(text)
        decryptedText = []
        
        for letter in tmpList:
            if (not letter in self.alphabet):
                continue
            dec = modInv*(self.alphabet.index(letter) - keys[1]) % self.keySpace
            decryptedText.append(self.alphabet[dec])
        
        last = "".join(decryptedText)
        print(last)

opt = int(input("Enter '1' to encrypt, '0' to decrypt : "))
inp = input("enter Text : ")
inp = inp.upper()
keys = []
for i in range(0,2):
    keys.append(int(input("Enter key " + str(i+1) + " : ")))

a = Affine()

if opt:
    a.encrypt(inp, keys)
else:
    a.decrypt(inp, keys)