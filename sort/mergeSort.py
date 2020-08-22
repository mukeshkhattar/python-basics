def sort(list):
  print(list)
  if len(list) <=1:
    return list
  mid=len(list)//2
  list1=sort(list[:mid])
  list2=sort(list[mid:])
  list=merge(list1,list2)
  return list

def merge(list1,list2):
  index1=0
  index2=0
  list3=[]
  while index1<len(list1) and index2<len(list2):
    if list1[index1] <= list2[index2]:
      list3.append(list1[index1])
      index1+=1
    else:
      list3.append(list2[index2])
      index2+=1

  while index1<len(list1):
    list3.append(list1[index1])
    index1+=1


  while index2<len(list2):
    list3.append(list2[index2])
    index2+=1
  print('returning:',list3)
  return list3


if __name__ == '__main__':
  list=['s','q','e','t','d','sd','sa']
  sorted=sort(list)
  print(sorted)
