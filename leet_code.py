
# №1 Remove Duplicates from Sorted Array
# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# Given nums = [1,1,2], Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
# It doesn't matter what you leave beyond the returned length.
def removeDuplicates(nums):
    j = 0
    for i in range(len(nums)):
        if (nums[i-1] != nums[i]) or (i == 0):
            j += 1
        print (i, j, nums[i])
    return j
nums = [1, 1, 2]
removeDuplicates(nums)

# №2 Лучшее время для покупки и продажи акций II
# Допустим, у вас есть массив, для которого i- й элемент является ценой данной акции в день i .
# Разработайте алгоритм поиска максимальной прибыли. Вы можете совершить столько транзакций, сколько захотите (т.е. купить одну и продать одну акцию несколько раз).
# Примечание. Вы не можете участвовать в нескольких транзакциях одновременно (т. Е. Вы должны продать акцию перед повторной покупкой).
def maxSum(nums):
    sdelka = 0 # акция продана
    Sum = 0
    print
    for i in range(len(nums)):
        if ((i + 1) == len(nums)):
            if (sdelka == 1):
                sdelka = 0
                Sum += nums[i]
            break
        if (nums[i] < nums[i+1]) & (sdelka == 0):
            sdelka = 1 # акция куплина
            Sum -= nums[i]
        if (nums[i] > nums[i+1]) & (sdelka == 1):
            sdelka = 0 # акция продана
            Sum += nums[i]
        print (i, sdelka, Sum)
    return Sum

# №3 Повернуть массив
# Решение Для данного массива поверните массив вправо на k шагов, где k неотрицательно.
# Ввод: [1,2,3,4,5,6,7] и k = 3 
# Выход: [5,6,7,1,2,3,4] Объяснение: повернуть на 1 шаг вправо: [7,1,2,3,4,5,6] 
# повернуть на 2 шага вправо: [6,7,1,2,3,4,5] 
# повернуть на 3 шага вправо:[5,6,7,1,2,3,4]
def rotate(nums,k):
    for i in range(len(nums)):
        print (nums[i-k])
    return

# №4 Содержит дубликат
# Решение По заданному массиву целых чисел найдите, содержит ли массив дубликаты.
# Ваша функция должна возвращать true, если какое-либо значение встречается в массиве хотя бы дважды, и возвращать false, если каждый элемент отличается.
# Пример Ввод: [1,2,3,1] Вывод : правда
def containsDuplicate(nums):
    res = False
    for i in range(len(nums)):
        for j in range(len(nums)):
            if (nums[i] == nums[j]) & (j != i):
                res = True
                print (nums[i-k])
    return res