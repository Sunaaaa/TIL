friuts = ["사과", "사과", "바나나", "바나나", "파인애플", "딸기", "파인애플", "딸기"]

my_dict = {}

for friut in friuts:
    my_dict[friut] = my_dict.get(friut,0)+1

for key, value in my_dict.items():
    print(key, ":", value)
