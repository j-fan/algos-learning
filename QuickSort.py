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

# 3 way partition
def partition3(arr, lo, hi):
  pivot = arr[lo]
  lt = lo
  gt = hi
  i = lo
  while i <= gt:
    if arr[i] < pivot:
      swap(arr, lt, i)
      lt += 1
      i += 1
    elif arr[i] > pivot:
      swap(arr, gt, i)
      gt -= 1
    else:
      i += 1
  return (lt-1, gt+1)

def quickSort(arr, lo, hi):
  if hi <= lo:
    return
  lohi = partition3(arr, lo, hi)
  quickSort(arr, lo, lohi[0])
  quickSort(arr, lohi[1], hi)


testArr = [5, 2, 6 ,9, 4, 8, 1, 7]
quickSort(testArr, 0, len(testArr)-1)
print(testArr)