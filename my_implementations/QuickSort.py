def swap(arr, i, j):
  temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp

def partition(arr, lo, hi):
  pivot = arr[lo]
  i = lo
  j = hi
  while True:
    while arr[i] <= pivot: # find larger than pivot, scanning from left
      if i == hi:
        break
      i+=1
    while arr[j] > pivot: # find smaller than pivot, scanning from right
      if j == lo:
        break
      j-=1

    if i >= j: #pointers crossed
      break
    swap(arr, i, j)

  swap(arr, lo, j)
  return j # j marks the end of the left subarray

def quickSort(arr, lo, hi):
  if hi <= lo:
    return
  j = partition(arr, lo, hi)
  quickSort(arr, lo, j)
  quickSort(arr, j+1, hi)

testArr = [5, 2, 6 ,9, 4, 8, 1, 7]
quickSort(testArr, 0, len(testArr)-1)
print(testArr)