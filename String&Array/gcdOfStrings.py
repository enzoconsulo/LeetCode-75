class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        result = ""
        for i in range(1,min(len(str1),len(str2))+1):               
        # for i in range 1(first char) to min between str1 and str2 len +1(adjust to char index)
        #   was necessary to get the minimal value bcs minimal len that result can have is the len of the smaller str
            if str1[:i] == str2[:i]:
                result = str1[:i]

        i=0
        len1,len2 = len(str1),len(str2)    
        #declaring here only to be easier to understand the if conditions,but can be directly used into if condition

        final = ""
        for i in range(len(result),0,-1):                           
        #we'll try to get the minimal result len of results, so we'll test each combination of result starting in bigger to smaller
            
            len3 = len(result[:i])                                  
            #have to declare here bcs each therm in result will have a value, but can also be directed use into if condition
            
            if len(result) == 0: continue                           
            #checking to not divide by 0
                
            if (len1 % len3 == 0 and len2 % len3 == 0 ):          
            #if the actual result substring was applicable to each len of str
                str1Ammount = len1 // len3
                str2Ammount = len2 // len3
                if result[:i] * str1Ammount == str1 and result[:i] * str2Ammount == str2:   
                #now is the essential of function. Verify if each str was divisable to actual result substring
                    final = result[:i] 
                    # if divisable, set this substring as actual result. and keep looping searching to smaller ones
                    break
                    #this break is essential to get the greater(bigger result)

        return final