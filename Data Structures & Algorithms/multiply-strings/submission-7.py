class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1List = [int(num1[i]) for i in range(len(num1)-1, -1, -1)]
        num2List = [int(num2[i]) for i in range(len(num2)-1, -1, -1)]
        if num1List==[0] or num2List==[0]:
            return "0"
        
        resultList = []
        for pow10 in range(len(num1List)):
            # print(pow10)
            currResult = self.helpMultiply(num1List[pow10], pow10, num2List)
            # print(f"current result {currResult}") 
            # print(f"running result {resultList}")
            resultList = self.helpAdd(resultList, currResult)
            # print(f"final result for current iteration: {resultList}")
        result = ""
        for i in range(len(resultList)-1, -1, -1):
            result += str(resultList[i])
        return result

    def helpMultiply(self, digit1: int, digit1Pow: int, num2List: list) -> list:
        resultList = [0] * digit1Pow
        carryOver = 0
        for i in range(len(num2List)):
            currDigit = digit1 * num2List[i] + carryOver
            remainDigit = currDigit % 10 
            carryOver = currDigit // 10
            resultList.append(remainDigit)

        if carryOver > 0:
            resultList.append(carryOver)
        return resultList
    
    def helpAdd(self, list1: list, list2: list) -> list:
        combinedList = []
        i = 0
        carryOver = 0
        while i < len(list1) and i < len(list2):
            currDigit = list1[i] + list2[i] + carryOver
            remainDigit = currDigit % 10 
            carryOver = currDigit // 10
            combinedList.append(remainDigit)
            i += 1

        while i < len(list1):
            currDigit = list1[i] + carryOver
            remainDigit = currDigit % 10 
            carryOver = currDigit // 10
            combinedList.append(remainDigit)
            i += 1
        
        while i < len(list2):
            currDigit = list2[i] + carryOver
            remainDigit = currDigit % 10 
            carryOver = currDigit // 10
            combinedList.append(remainDigit)
            i += 1
        
        if carryOver > 0:
            combinedList.append(carryOver)
        return combinedList