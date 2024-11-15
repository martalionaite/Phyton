# ivedami 5 skaiciai. Surasti didziausia. Naudoti:
# max, list, str for, while

def didziausias(nums):
    largestNum = nums[0]
    for num in nums:
        if largestNum < num:
            largestNum = num
    print(largestNum)
    return largestNum
    
didziausias([1, 2, 3, 4, 5])

sk1 = int(input('sk = '))
sk2 = int(input('sk = '))
sk3 = int(input('sk = '))
sk4 = int(input('sk = '))
sk5 = int(input('sk = '))

