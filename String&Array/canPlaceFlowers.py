def canPlaceFlowers(flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        possibleSpaces = 0
        beforeIndex = 0
        afterIndex = 0
        
        for i in range(len(flowerbed)) :
            actual = flowerbed[i]
            
            if i-1 < 0 :
                beforeIndex = 0
                if i+1 <= len(flowerbed)-1:
                    afterIndex = flowerbed[i+1]

            elif i+1 > len(flowerbed)-1:
                beforeIndex = flowerbed[i-1]
                afterIndex = 0
            else:
                beforeIndex = flowerbed[i-1]
                afterIndex = flowerbed[i+1]
                
            if  beforeIndex == 0 and afterIndex == 0 and actual == 0:
                possibleSpaces += 1
                flowerbed[i] = 1
            
        if n <= possibleSpaces:
            print(True)
        else:
            print(False)
                

test1 = [1,0,0,0,1,0,0]

canPlaceFlowers(test1,2)