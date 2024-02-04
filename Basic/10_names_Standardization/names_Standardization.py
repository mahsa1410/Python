#input: BaHram MaHnaZ hooman FaribORZ => output: Bahram Mahnaz Hooman Fariborz
name_list=[]
for i in range(0,4):
    name_list.append(input().lower())

for i in range (0,len(name_list)):
    temp = name_list[i]
    temp = temp[0].upper() + temp[1:]
    print (temp)
