


# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(list,first,last):
  print('partitioning list:',list,first,last)
  pivot_value=list[first]
  leftmark=first+1
  rightmark=last
  done=False
  while not done:
    # note list[] needs to be set as a second condition to avoid index out of bound error
    while  leftmark<=rightmark and list[leftmark] <= pivot_value:
      leftmark+=1
    while leftmark<=rightmark and list[rightmark] >= pivot_value:
      rightmark-=1
    if rightmark < leftmark:
      done=True
    else:
      list[righmark],list[leftmark]=list[leftmark],list[rightmark]
  list[first],list[rightmark]=list[rightmark],list[first]
  return rightmark


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
def sort(list,first,last):
  if first < last:
    pivot_index=partition(list,first,last)
    sort(list,first,pivot_index-1)
    sort(list,pivot_index+1,last)


if __name__ == '__main__':
  list=['1','2','7','6','5','4','3']
  sort(list,0,len(list)-1)
  print(list)
