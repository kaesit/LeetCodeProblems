input=["+1A", "+3E", "-1A", "+4F", "+1A", "-3E", "+4F", "+4F", "+4F"]
dict={}
for el in input:
     if el not in dict:
          dict[el]=1
     else:
          dict[el]+=1
i=0
k=""
for el in dict:
     if dict[el] > i:
          i = dict[el]
          k = el
print(dict[el])
print(k)