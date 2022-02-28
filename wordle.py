import random
from os import system, name
def divider(x,y):
    with open(x,'r') as f:
            listl=[]
            for line in f:
                    strip_lines=line.strip()
                    listli=strip_lines.split()
                    
                    m=listl.append(listli)
    z = listl
    x = []
    for element in z:
        if type(element) is list:
         
            for item in element:
                x.append(item)
        else:
            x.append(element)
    only = []
    i = 0
    while i < len(x):
        
        if len(x[i]) == y:
            only.append(x[i])
        i = i + 1
    return only

def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def terminal():
    wordList = []
    correct = False
    list_of_words = divider('guessList.txt',5)
    list_of_ans = divider('answerList.txt',5)
    attempts = 0
    i = 0
    
    answerIndex = random.randint(0,len(list_of_ans)-1)
    answer = list_of_ans[answerIndex]
        
    while (attempts != 6) and (correct != True):
        print_matrix(wordList,answer)
        validInput = False
        while (validInput == False):
            response = input('Enter next guess: ').strip()
            i = 0
            while (i < len(list_of_words)):
                if (response.upper() == list_of_words[i]):
                    validInput = True
                i += 1
            if (validInput == False):
                print("Not in word list")
        wordList.append(response.upper())
        attempts += 1
        if (response.upper() == answer):
            correct = True
            


    print_matrix(wordList,answer)
    if (correct == True):
        
            print("Great!")
    else:
        print("Answer: " + answer)

def print_matrix(wordList,ans):
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")  
    clear()
    print("[W] [O] [R] [D] [L] [E]") 
    i = 0
    extra = 0
    while (len(wordList) != 6):
        wordList.append("     ")
        extra += 1
    while (i < 6):
        j = 0
        print("| ",end='')
        currComp = stringComp(ans,wordList[i])
        while (j < 5):
            if (currComp[j] == 2):
                print("[",end='')
            elif (currComp[j] == 1):
                print("{",end='')
            else:
                print("(",end='')

            print(wordList[i][j],end='')

            if (currComp[j] == 2):
                print("]",end=' ')
            elif (currComp[j] == 1):
                print("}",end=' ')
            else:
                print(")",end=' ')
            j += 1
        print("|")
        i += 1
    k = 0
    #print(ans)
    getLetterList(ans,wordList)
    while (extra != 0):
        wordList.pop()
        extra -= 1

    #getLetterList(wordList,ans)
    



def stringComp(x,y): 
    ans = list(x)
    word = list(y)
    comp = []
    i = 0
    while (i < 5):
        if (word[i] == ans[i]):
            comp.append(2)
        else:
            j = 0
            while (j < 5):
                if (word[i] == ans[j]):
                    comp.append(1)
                j += 1
        i += 1
        if (len(comp) < i):
            comp.append(0)
    # print(comp)
    return comp

def getLetterList(x,y):    
    ans = list(x)
    word = y
    green = []
    yellow = []
    grey = []
    
    i = 0
    while (i < len(y)):
        j = 0
        while (j < 5):
            exist = False
            k = 0
            if (word[i][j] == ans[j]) and ((word[i][j] in green) == False):
                if (word[i][j] in yellow):
                    yellow.remove(word[i][j])
                green.append(word[i][j])
                exist = True
            else:
                while (k < 5):
                    
                    if (word[i][j] == ans[k]) and ((word[i][j] in yellow) == False) and ((word[i][j] in green) == False):
                        yellow.append(word[i][j])
                        exist = True
                    k += 1
            
            if (exist != True) and (word[i] != "     ") and ((word[i][j] in grey) == False) and ((word[i][j] in yellow) == False) and ((word[i][j] in green) == False):
                
                # print(ans)
                grey.append(word[i][j])
            j += 1
        i += 1        
    print("[Green]:  " + str(sorted(green)))
    print("{Yellow}: " + str(sorted(yellow)))
    print("(Grey):   " + str(sorted(grey)))      
       
    

if __name__ == '__main__':
  #print_matrix(["DELTA","ALPHA","MACRO","SPARE","NOPED","BREAD"])
   terminal()
    # print_matrix(["CABIN","BREAK","BLACK","BLOKE"]  , "BLOKE")

# [W] [O] [R] [D] [L] [E]
# | (C) (A) {B} (I) (N) |
# | [B] (R) {E} (A) {K} |
# | [B] [L] (A) (C) {K} |
# | [B] [L] [O] [K] [E] |
# |                     |
# |                     |



# TODO: Add a good letter and bad letter thing





