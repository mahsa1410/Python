#input: numper of voter, then votes => output: candidates and their vote
candidate_count_list = dict()
count = int(input())
for i in range(0,count):
    candidate_name = input().lower()
    if candidate_name in candidate_count_list:
        candidate_count_list[candidate_name]= candidate_count_list[candidate_name]+1
    else:
        candidate_count_list[candidate_name]=1
for i in sorted(candidate_count_list.keys()):
    print (i,candidate_count_list[i])