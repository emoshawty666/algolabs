import random

def increaseSort(arr):
    n = len(arr)
    for i in range(n):
        min_arr = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_arr]:
                min_arr = j
        arr[i],arr[min_arr] = arr[min_arr],arr[i]


# k = random.randint(2,30)
# a = [random.randint(2,103) for x in range(k)]

# print("Неотсортированный массив", a)
# increaseSort(a)
# print("Отсортированный массив", a)


def decreasingSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] < arr[j]:
                arr[i],arr[j] = arr[j],arr[i]


# count = random.randint(2, 30)
# array = [random.randint(2, 103) for x in range(count)]
# print("Неотсортированный массив", array)
# decreasingSort(array)
# print("Отсортированный массив", array)

def TelephoneSort(phone):
    n = len(phone)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if phone[j] < phone[min_index]:
                min_index = j
        phone[i], phone[min_index] = phone[min_index], phone[i]


phone = ["21-32-45", "89-94-02", "98-76-54", "12-34-56", "55-55-55", "23-45-67", "87-65-43"]
print("Неотсортированный список телефонов:", phone)
TelephoneSort(phone)
print("Отсортированный список телефонов:", phone)
