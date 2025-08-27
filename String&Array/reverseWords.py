def reverseWords(s):
        """
        :type s: str
        :rtype: str
        """
        
        words = s.split()
        
        reversed = []
        for i in range(len(words)-1,-1,-1):
            reversed.append(words[i])
        
        s = " ".join(reversed)
        
        return s
        
        
print(reverseWords("the sky is blue"))