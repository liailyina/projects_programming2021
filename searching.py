class NewList:
    def __init__(self, arr, element):
        self.arr = arr
        self.element = element

    def binary_search(self, arr, element):
        arr.sort()
        print(arr)
        first = 0
        last = len(arr) - 1
        mid = len(arr) // 2
        while first <= last and arr[mid] != element:
            if element > arr[mid]:
                first = mid + 1
            else:
                last = mid - 1
            mid = (last + first) // 2
        if first <= last:
            print("ID =", mid)
        else:
            print('No element')

    def linear_search(self, arr, element):
        for num in range(len(arr)):
            if arr[num] == element:
                print(f'ID = {num}')
            else:
                print('No element')

lis = NewList
lis.arr = [17, 225, 4006, 3, 45, 2, 67, 8, 19, 555, 10000]
lis.element = 14
lis.binary_search(lis, lis.arr, lis.element)
lis.linear_search(lis, lis.arr, lis.element)