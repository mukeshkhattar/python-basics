def sort(list):
  print(list)
  if len(list) <=1:
    return list
  mid=len(list)//2
  left_half=list[:mid]
  right_half=list[mid:]
  sort(left_half)
  sort(right_half)
  # merge two lists now
  index1=0
  index2=0
  k=0 # index for the main list to be sorted
  while index1<len(left_half) and index2<len(right_half):
    if left_half[index1] <= right_half[index2]:
      list[k]=left_half[index1]
      index1+=1
    else:
      list[k]=right_half[index1]
      index2+=1
    k+=1

  while index1<len(left_half):
    list[k]=left_half[index1]
    index1+=1


  while index2<len(right_half):
    list[k]=right_half[index1]
    index2+=1
  print('returning:',list)


if __name__ == '__main__':
  list=['s','q','e','t','d','sd','sa']
  sort(list)
  print(list)
