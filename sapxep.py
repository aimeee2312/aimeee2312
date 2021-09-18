list = [2,6,3,8,1,4,7]
l= len(list)
for i in range(0, l-1 )
  for j in (l,i+1)
  if list[i] < list[j]:
            tmp = list[i]
            list[i] = list[j]
            list[j] = tmp
print(list)