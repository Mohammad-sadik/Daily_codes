f_name = 'copy.txt'
with open("employee.text", 'r') as file:
    empl = file.readlines()


with open(f_name, 'w') as w_file:
    w_file.writelines(empl)

print('Program Completed....!')