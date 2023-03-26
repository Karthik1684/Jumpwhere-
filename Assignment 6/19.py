# 19. From a list containing ints, strings and floats, make three lists to store them separately

w=[7, 2.0,4.3,"welcome", 8, 5.3,"hello"]
int_list = []
float_list = []
string_list = []

for i in w:
    if type(i) == int:
        int_list.append(i)
    elif type(i) == float:
        float_list.append(i)
    elif type(i) == str:
        string_list.append(i)
print(int_list)
print(float_list)
print(string_list)