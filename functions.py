
def getHammingDistance(str1, str2): 
    #compare size of str1 and str2
    if len(str1) == len(str2):
        #if length of 2 strings are equal
        c = zip(str1,str2)
        d=0;
        for s1,s2 in c:
            if s1!=s2: #checks if the current character is not equal
                d=d+1  #increments d(hamming distacnce) 

        return d #returns hamming distance

    else:
        print "Error! Strings are not equal!"

#counts how many times the pattern occur in the string
def countSubstrPattern(original, pattern): 
    count = 0 # number of occurence of the pattern
    plen = len(pattern)
    
    for i in range(len(original)):
        if original[i:i+plen] == pattern: #if pattern is found
            count += 1 #increments count
    return count #return 

#checks if the character in str1 is in the alphabet
def isValidString(str1, alphabet):
    count = 0
    for letter in str1: #traverses str1 
       if alphabet.count(letter) == 0: #if the current character is
           return False                #not the alphabet the function
    return True                        #returns false else true

#gets Skew given n and str1
def getSkew(str1, n):
     c = 0
     g = 0
     for i in range(n):
        if str1[i] == "C": #count number of C's
            c = c + 1 
        if str1[i] == "G": #count number of G's
            g = g + 1
     return g-c # skew = g-c , return skew

#gets maximum skew from 1-N
def getMaxSkewN(str1, n):
    maximum = 0 #initialize maximum to least possible skew
    for i in range(1,n+1): #begins @1
        if getSkew(str1, i) > maximum:
            maximum = getSkew(str1, i)
    return maximum

#gets minimum skew from 1-N
def getMinSkewN(str1, n):
    minimum = len(str1) #initialize minimum to max possible skew
    for i in range(1,n+1): #begins @ 1
        if getSkew(str1, i) < minimum: 
            minimum = getSkew(str1, i)
    return minimum


  

       

