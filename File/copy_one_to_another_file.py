f_name = 'copy.txt'
# with open("employee.txt", 'r') as file:
#     empl = file.readlines()
# with open(f_name, 'w') as w_file:
#     w_file.writelines(empl)
# print('Program Completed....!')

with open('employee.txt', 'r') as r_file, open(f_name, 'w') as w_file:
    for line in r_file:
        w_file.writelines(line)
print('Program Completed....!')