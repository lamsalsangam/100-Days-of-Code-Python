with open("file1.txt") as file1:
    data_content = file1.readlines()
    datas_1 = [int(number) for number in data_content]
    # print(datas_1)

with open("file2.txt") as file2:
    data_content = file2.readlines()
    datas_2 = [int(number) for number in data_content]
    # print(datas_2)

result = [number for number in datas_1 if number in datas_2]
print(result)
