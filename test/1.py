from itertools import islice
import json

sanhao_list = []

file_read = open("/home/shiqiaofeng/Desktop/三好网9个学科课程规划.csv")

num = 0

with file_read as file:
    for line in islice(file, 1, None):
        sanhao_list.append(line.rstrip("\n").split(','))

print(sanhao_list)

my_file = open('json', 'w')
# my_file.write(json.dumps(sanhao_list))
my_file.write(json.dumps(sanhao_list, ensure_ascii=False))
# print(json.dumps(sanhao_list, ensure_ascii=False))

# my_file.close()

# my_file1 = open('json')
# my_json = my_file1.read()
# print(my_json)
# my_file1.close()
