import os
os.makedirs('C:\\delicious\\walnut\\waffles')
my_files = ['train.docx', 'test.docx', 'blue.txt']
for file in my_files:
    result = os.path.join('C:\\Users\\asweigart', file)
    print(result)
current_working_directory = os.getcwd()
print(current_working_directory)

