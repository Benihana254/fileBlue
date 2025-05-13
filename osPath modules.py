import os.path

x= os.path.abspath('.')
print(x)
size = os.path.getsize('.')
print(size)
lists = os.listdir('.')
print(lists)
new_folder_items = os.listdir(r'C:\Users\gh\Desktop\Academics\2.1')
print(new_folder_items)
file_size = os.path.getsize(r'C:\Users\gh\Desktop\Academics\2.1')
print(file_size)
"""
Trying to find the total size of all file in academics folder 
"""
total_size = 0
file_path = r'C:\Users\gh\Desktop\Academics\2.2\MPE 222 Solid Mechanics'
for file in os.listdir(file_path):
    full_path =  os.path.join(file_path, file)
    if os.path.isfile(full_path):
        total_size += os.path.getsize(full_path)
print(f'total size ; {total_size / (1024**2):.2f}')