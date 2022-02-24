import random
def divider(y):
    with open('words_alpha.txt','r') as f:
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
def terminal():
    
    
    #Getting the 15 numbers and the 1 answer from those 15
    list_of_words = divider(5)
    chosenList = []
    i = 0
    
    answerIndex = random.randint(0,len(list_of_words)-1)
    answer = list_of_words[answerIndex]
        
    print(answer)
    print(list_of_words)    



def print_matrix(wordList):
    i = 0
    while (i < 6):
        j = 0
        while (j < 5):
            print(" | ",end='')
            print(wordList[i][j],end='')
            
            
            j += 1
        print(" | ")
        #print("")
        
        i += 1
if __name__ == '__main__':
  print_matrix(["DELTA","ALPHA","MACRO","SPARE","NOPED","BREAD"])

