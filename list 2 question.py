n = input("Enter N:")
input_list=[]
for _ in range(int(n)):
     user_value = input("Enter input:")
     input_list.append(user_value)
print(input_list[0])
print(input_list[-3:int(n)])