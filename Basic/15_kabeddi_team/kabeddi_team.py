#visit this link for problem description
#https://maktabkhooneh.org/course/%D8%A2%D9%85%D9%88%D8%B2%D8%B4-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87-%D9%86%D9%88%DB%8C%D8%B3%DB%8C-%D8%A8%D8%A7-%D9%BE%D8%A7%DB%8C%D8%AA%D9%88%D9%86-%D9%85%D9%82%D8%AF%D9%85%D8%A7%D8%AA%DB%8C-mk346/%D9%81%D8%B5%D9%84-%D8%B3%D9%88%D9%85-%D8%B3%D8%A7%D8%AE%D8%AA%D8%A7%D8%B1%D9%87%D8%A7%DB%8C-%D8%AF%D8%A7%D8%AF%D9%87-%D9%BE%D8%A7%DB%8C%D8%AA%D9%88%D9%86-ch597/%D9%BE%D8%B1%D9%88%DA%98%D9%87-%D8%A2%D9%86%D9%84%D8%A7%DB%8C%D9%86-%D8%AA%D9%85%D8%B1%DB%8C%D9%86-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87-%D9%86%D9%88%DB%8C%D8%B3%DB%8C-%D9%85%D8%B3%D8%A7%D8%A8%D9%82%D8%A7%D8%AA-%D8%AC%D9%87%D8%A7%D9%86%DB%8C-%DA%A9%D8%A8%D8%AF%DB%8C/

players_Number = input()
player_history = input()
history_list = player_history.split()
history_list = list(map(int , history_list))

valid_players = int(( history_list.count(0)+ history_list.count(1)+ history_list.count(2))/3)
print(valid_players)
