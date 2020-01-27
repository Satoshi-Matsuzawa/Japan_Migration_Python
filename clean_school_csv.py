# Cleans school.csv file
# Replace 99 or 999 with 0
# Except for two rows, this causes no problem

import pandas as pd
import os

directory = '../../Data/School/0001'
file_name = 'school.csv'
file_read = os.path.join(directory, file_name)

df = pd.read_csv(file_read)

# Null values read from README files
null_major = 999
null_minor = 99

# Remove empty rows
df = df[df.male_graduates != null_major]

# Replace null values with 0
gender = ['male', 'female']
major_or_minor = ['_major', '_minor']
categories_major = ['_high_school', '_employed']
categories_minor = ['_part_time_high_school', '_home_and_high_school',
                    '_home', '_others']

for item_g in gender:
    for item_m in major_or_minor:
        for item_c in vars()['categories' + item_m]:
            column = item_g + item_c
            df.loc[:, column][df.loc[:, column] == vars()['null' + item_m]] = 0

# Compare subtotal of categories and graduates
categories_all = categories_major + categories_minor

for item_g in gender:
    df[item_g+'_subtotal'] = df.loc[:, item_g + categories_all[0]:
                                    item_g + categories_all[-1]].sum(axis=1)
    # Get indices such that the subtotal is not equal to the # of graduates
    # May delete rows with these indecies
    vars()[item_g+'_sub_neq_grad_id'] = df[df[item_g + '_subtotal']
                                           != df[item_g + '_graduates']].index
    # Delete subtotal columns
    del df[item_g + '_subtotal']

# Create cleaned dataset
new_file_name = 'school_cleaned.csv'
file_out = os.path.join(directory, new_file_name)
df.to_csv(file_out, index=False)
