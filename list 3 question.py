n = input("Enter N:")
input_list = []
for _ in range(int(n)):
    user_value = input("Enter input:")
    input_list.append(user_value)
for n in input_list:
    if int(n)%5==0:
        print(n)