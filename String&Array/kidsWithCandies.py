def kidsWithCandies(candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        
        GreatestCandies = max(candies)
        
        result=[]
        
        for kid in candies:
            kidCandies = kid + extraCandies
            if kidCandies >= GreatestCandies:
                result.append(True)
            else:
                result.append(False)
        
        print(result)
    
kidsWithCandies([2,3,5,1,3],3)