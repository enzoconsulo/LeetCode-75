def reverseVowels(s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ["a","e","i","o","u"]
        
        indexes = []
        
        for i in range(len(s)):
            if s[i].lower() in vowels:
                indexes.append(i)
        
        s2 = list(s) # need to convert to list bcs strings are imutables
        indexesSize = len(indexes)-1
        for i in range(len(indexes)//2):

            tmp = s2[indexes[i]]
            s2[indexes[i]] = s2[indexes[indexesSize-i]]
            s2[indexes[indexesSize-i]] = tmp
        
        s = "".join(s2)
        
        return s
            
s = "IceCreAm"
s= reverseVowels(s)
print(s)
