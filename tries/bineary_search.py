def binary_search(arr, x):
     sol = 0
     sag = len(arr) - 1
     while sol <= sag:
          orta = sol + (sag - sol) // 2
          if arr[orta] == x:
               return orta
          elif arr[orta] < x:
               sol = orta + 1
          else:
               sag = orta - 1
     return -1

# Örnek kullanım
dizi = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
dizi2 = [5,7,7,8,8,10]
aranan_eleman = 12
aranan_eleman2 = 8

sonuc = binary_search(dizi2, aranan_eleman2)

if sonuc != -1:
    print(f"Aranan eleman {sonuc}. indiste bulundu.")
else:
    print("Aranan eleman dizide bulunamadı.")

def binarySearchRecursive(nums, left, right, target, result):

    """
    This is your exit point. 
    If the target is not found, result will be -1 since it won't change from initial value.
    If the target is found, result will be the index of the first occurrence of the target.
    """
    if left > right:
        return result 

    # Overflow prevention
    mid = left + (right - left) // 2

    if nums[mid] == target:
        # We are not sure if this is the first occurrence of the target.
        # So we will store the index to the result now, and keep checking.
        result = mid 
        # Since we are looking for "first occurrence", we discard right half.
        return binarySearchRecursive(nums, left, mid - 1, target, result) 
    elif target < nums[mid]:
        return binarySearchRecursive(nums, left, mid - 1, target, result)
    else:
        return binarySearchRecursive(nums, mid + 1, right, target, result)

if __name__ == '__main__':

    nums = [2,4,4,4,7,7,9]
    target = 4 

    (left, right) = (0, len(nums)-1)
    result = -1 # Initial value
    index = binarySearchRecursive(nums, left, right, target, result)

    if index != -1:
        print("The index is: ", index)
    else:
        print('Not found') 