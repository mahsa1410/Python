#input: some laptop_price and laptop_quality => if (laptop1_price<laptop2_price) and (laptop1_quality>laptop2_quality) print: 'happy irsa' else: 'poor irsa'
def find_best_laptop(lis):
    for i in range(0 , len(lis)-1):
        #print( lis[i][0] , lis[i+1][0])
        if lis[i][0] < lis[i+1][0]:            
            if lis[i][1] > lis[i+1][1]:
                return 1
    return 0

laptop_number = int(input())
laptop_list = lit= []

for i in range(0,laptop_number):
    laptop_qp = input()
    lit = list( map( int , list(laptop_qp.split())))
    laptop_list.append(lit)
#print(laptop_list)

if find_best_laptop(laptop_list):
    print ('happy irsa')
else:
    print ('poor irsa')
