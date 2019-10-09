
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

# 5 Single Number
# Учитывая непустой массив целых чисел, каждый элемент появляется дважды, кроме одного. Найдите этот единственный.
# Примечание:
# Ваш алгоритм должен иметь линейную сложность во время выполнения. Не могли бы вы реализовать это без использования дополнительной памяти?
# Пример 1: Input: [2,2,1] Output: 1
# Input: [4,1,2,1,2] Output: 4
def singlenumber(nums):
    for i in range(len(nums)):
        if (nums[i] not in nums[0:i]) & (nums[i] not in nums[i+1:]):
            break
    return nums[i]

# 6 Intersection of Two Arrays
# Учитывая два массива, напишите функцию для вычисления их пересечения.
# Пример 1: Ввод: nums1 = [1,2,2,1], nums2 = [2,2] Выход: [2,2]
# Пример 2: Ввод: nums1 = [4,9,5], nums2 = [9,4,9,8,4] Выход: [4,9]
# Примечание:
# Каждый элемент в результате должен появляться столько раз, сколько он показывает в обоих массивах.
# Результат может быть в любом порядке.
# Следовать за:
# Что если данный массив уже отсортирован? Как бы вы оптимизировали свой алгоритм?
# Что если размер nums1 маленький по сравнению с размером nums2? Какой алгоритм лучше?
# Что если элементы nums2 хранятся на диске, а память ограничена, так что вы не можете загрузить все элементы в память одновременно?
def Intersection_of_Two_Arrays(nums1, nums2):
    res = []
    for i in nums1:
        if i in nums2:
            res.append(i)
            nums2.remove(i) # Удаляет первый элемент в списке, имеющий значение i.
    return res
# Что если данный массив уже отсортирован? Как бы вы оптимизировали свой алгоритм? - Использовать срезы [i:]
# Что если размер nums1 маленький по сравнению с размером nums2? Какой алгоритм лучше? - Цикл по самому маленькому массиву
# Что если элементы nums2 хранятся на диске, а память ограничена, так что вы не можете загрузить все элементы в память одновременно?

# 7 Plus One
# Дан непустой массив цифр, представляющих неотрицательное целое число, плюс один к целому числу.
# Цифры хранятся таким образом, что наиболее значимая цифра находится в начале списка, а каждый элемент в массиве содержит одну цифру.
# Вы можете предположить, что целое число не содержит ни одного начального нуля, кроме самого числа 0.
def plus_one(nums):
    nums[-1] += 1
    return nums

# 8 Move Zeroes
# Учитывая массив nums, напишите функцию, чтобы переместить все 0 в конец, сохраняя относительный порядок ненулевых элементов.
# Example: Input: [0,1,0,3,12] Output: [1,3,12,0,0] 
# Примечание:
# Вы должны сделать это на месте, не делая копию массива. Минимизируйте общее количество операций
def Move_Zeroes(nums):
    i = len(nums)
    while i > 0:
        if nums[i-1] == 0:
            del nums[i-1]
            nums.append(0)
        i -=1
    return nums

# 9 Two Sum
# Две суммы Решение Получив массив целых чисел, верните индексы двух чисел так, чтобы они суммировались с определенной целью. 
# Вы можете предположить, что каждый вход будет иметь только одно решение, и вы не можете использовать один и тот же элемент 
# дважды. Пример:Заданные числа = [2, 7, 11, 15], цель = 9, Потому что nums [ 0 ] + nums [ 1 ] = 2 + 7 = 9, возврат [ 0 , 1 ].
def two_sum(nums, target):
    j = 0
    for i in range(len(nums)):
        # print(i, nums[i], target - nums[i], nums[i+1:]) for debugging
        if (target - nums[i]) in nums[i+1:]:
            j = nums.index(target - nums[i])
            break
    return i, j



