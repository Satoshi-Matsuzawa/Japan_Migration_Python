import os

directory = '../../Data/School/0001'

old_file_names = ['0001_kou', '0001_otsu', '0001_hei', '0001_tei']
new_file_names = ['School_Statistics', 'Employed', 'Home', 'High_School']

for i in range(len(old_file_names)):
    old_file = os.path.join(directory, old_file_names[i]+'.dat')
    new_file = os.path.join(directory, new_file_names[i]+'.dat')
    os.rename(old_file, new_file)
