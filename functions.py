def getHammingDistance(str1, str2):
    #compare size of str1 and str2
    if len(str1) == len(str2):
        c = zip(str1,str2)
        d=0;
        for s1,s2 in c:
            if s1!=s2:
                d=d+1

        return d

    else:
        print "Error! Strings are not equal!"

def countSubstrPattern(original, pattern):
    count = 0
    plen = len(pattern)
    
    for i in range(len(original)):
        if original[i:i+plen] == pattern:
            count += 1
    return count


def isValidString(str1, alphabet):
   
    count = 0
    for letter in str1:
       if alphabet.count(letter) == 0:
           return False
  

    return True




