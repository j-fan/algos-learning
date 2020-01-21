def isSorted(arr, lo, hi):
  print()
  for i in rangeInclusive(lo, hi):
    print(arr[i], end=' ')
    if i+1 > hi:
      break
    if arr[i] > arr[i+1]:
      return False
  return True

def merge(arr, aux, lo, mid, hi):
  assert isSorted(arr, lo, mid)
  assert isSorted(arr, mid+1, hi)
  aux = arr.copy()
  i = lo
  j = mid+1
  for x in rangeInclusive(lo, hi):
    # handle case where one subarray has beeen completed. Also helps prevent running off the end
    if i > mid:
      arr[x] = aux[j]
      j += 1
    elif j > hi:
      arr[x] = aux[i]
      i += 1
    # pick the larger element out of the 2 sub arrays
    elif aux[i] > aux[j]:
      arr[x] = aux[j]
      j += 1
    else:
      arr[x] = aux[i]
      i += 1
  assert isSorted(arr, lo, hi)

def mergeSort(arr, aux, lo, hi):
  if hi <= lo:
    return
  mid = lo + (hi - lo) // 2
  mergeSort(arr, aux, lo, mid)
  mergeSort(arr, aux, mid+1, hi)
  merge(arr, aux, lo, mid, hi)

def rangeInclusive(start, end):
  return range(start, end+1)

# testArr = [1,3,5,7,9,2,4,6,8]
testAux = []
# merge(testArr, testAux, 0, len(testArr)-1)

randomArr = [11,7,3,9,4,0,16,4,5,2,6,1]
mergeSort(randomArr, testAux, 0, len(randomArr)-1)