import csv

employee = [['name', 'job', 'age'],['spongebob','cook', '30'],['patrick','cook','37']]
file_path = 'a.csv'
try:
    with open(file_path,'w',newline='') as file:
        #json.dump(employee,file)
        writer = csv.writer(file)
        for row in employee:
            writer.writerow(row)

except FileExistsError:
    print('oh noooo')
finally:
    print('success')

import csv
file_path ='a.csv'
with open(file_path,'r') as file:
    content = csv.reader(file)
    for line in content:
        print(line)