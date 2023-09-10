print(""" _                _             
| |              | |            
| |__  _ __ _   _| |_ _   _ ___ 
| '_ \| '__| | | | __| | | / __|
| |_) | |  | |_| | |_| |_| \__ \\
|_.__/|_|   \__,_|\__|\__,_|___/
                        By Batuhan Dilek """)


#TODO Letter frequency analysis

#Get the analitics and put them in an array
#get the input and count every letter and store them 
#Each key, decrypt the message and check if the most frequent keys are matching
#if not iterate

import time

class Brutus:

    def __init__(self):
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.keySpace = 26
        self.analitics = [8.4966,2.0720,4.5388,3.3844,11.1607,1.8121,2.4705,3.0034,7.5448,0.1965,1.1016,5.4893,3.0129,6.6544,7.1635,
                          3.1671,0.1962,7.5809,5.7351,6.9509,3.6308,1.0074,1.2899,0.2902,1.7779,0.2722]
        

    def findBiggestIndexes(self):
        copyAnalytic = self.analitics
        result = []
        for maxCount in range(0, len(self.analitics)- 6):
            max = 0
            for ent in copyAnalytic:
                if ent > max:
                    max = ent

            result.append(self.analitics.index(max))
            copyAnalytic[copyAnalytic.index(max)] = 0     
        return result               


    def cracker(self, text):
        # y - k mod 26
        tmpList = list(text)
        wordCountofText = []
        hitCount = 0
        biggestOriginal = self.findBiggestIndexes()
        sortedWordIndexes = []
        biggest = []
        for i in range(0, self.keySpace):
            biggest.append(0)
        moduloRes = 0
        keyProbs = []
        possibleKeys = [0,0,0,0,0]
        for j in range (0, self.keySpace):
            wordCountofText.append(0)
            keyProbs.append(0)
        #Decryption

        for k in range(1, self.keySpace):
            tmpList = list(text)
            hitCount = 0
            for a in range (0, self.keySpace):
                wordCountofText[a] = 0
                #keyProbs[a] = 0
            #print("K = " + str(k))
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
            lastList = list(last)

        
            #letter counting
            for x in lastList:
                if (not x in self.alphabet):
                    continue
                index = self.alphabet.index(x)
                wordCountofText[index] = wordCountofText[index] + 1
            #print("Wordcounts " + str(wordCountofText))
            #find biggest three in text
            biggest[0] = 0
            for maxCount in range(0,self.keySpace):
                max1 = 0
                for wordIndex in range(0, len(wordCountofText)):
                    if wordCountofText[wordIndex] > max1:
                        max1 = wordCountofText[wordIndex]

                biggest[maxCount] = wordCountofText.index(max1)
                wordCountofText[wordCountofText.index(max1)] = 0

            
            #print("Biggest indexes of the alphabet are : \n" + str(biggest))
            #check hits
            for p in biggest:
               
                if p in biggestOriginal:
                    hitCount = hitCount + 1

            keyProbs[k] = hitCount
            
            #print("Key probs : " + str(keyProbs))    
            #print("-------------------------------")
        #print("Key probs : " + str(keyProbs))
        print("\n\n\nCalculating the best keys[ ]")
        copyOfKeyProbs = keyProbs
        #print(keyProbs)
        possibleKeys[0] = keyProbs[0]
        for p in range(0,5):
            max = 0
            for key in range(0, len(keyProbs)):
                if copyOfKeyProbs[key] > max:
                    max = copyOfKeyProbs[key]
            possibleKeys[p] = copyOfKeyProbs.index(max)
            copyOfKeyProbs[copyOfKeyProbs.index(max)] = 0


        print("Best possible keys are : ")
        print(possibleKeys)
        print()
        

        
        for k in possibleKeys:
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
            print("Key : " + str(k) + " Decrypted message : " + last + "\n")


a = Brutus()
inp = input("Input text : ")

timerStart = time.perf_counter()
a.cracker(inp)
timerEnd = time.perf_counter()
timer = timerEnd - timerStart
print(f"It took {timer:0.4f} seconds to find keys and decipher the message")