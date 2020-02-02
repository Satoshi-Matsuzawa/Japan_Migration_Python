# Clean school.csv file
# Replace null values, 99 or 999, with 0
# Add shares and totals

import pandas as pd
import os
import functions as func

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
major_or_minor = ['major', 'minor']
categories_major = ['high_school', 'employed']
categories_minor = ['part_time_high_school', 'home_and_high_school',
                    'home', 'others']
categories = categories_major + categories_minor

# Major categories use null value 999
# Minor categories use null value 99

for gen in gender:
    for m in major_or_minor:
        for cat in vars()['categories' + '_' + m]:
            func.replace_with_zero(df, gen, cat, vars()['null' + '_' + m])

# Compare subtotal of categories and graduates
# categories_all = categories_major + categories_minor

# for item_g in gender:
#    df[item_g + '_subtotal'] = df.loc[:, item_g + categories_all[0]:
#                                      item_g + categories_all[-1]].sum(axis=1)
#    # Get indices such that the subtotal is not equal to the # of graduates
#    # May delete rows with these indecies
#    vars()[item_g + '_sub_neq_grad_id'] = df[df[item_g + '_subtotal']
#                                           != df[item_g + '_graduates']].index
    # Delete subtotal columns
#    del df[item_g + '_subtotal']


# Create Shares
for gen in gender:
    for cat in categories:
        func.create_share(df, gen, cat, 'graduates')

# Create Totals
columns = ['graduates'] + categories
for col in columns:
    func.create_total(df, col)

# Create total shares
for cat in categories:
    func.create_total_share(df, cat, 'graduates')

# Create cleaned dataset
new_file_name = 'school_cleaned.csv'
file_out = os.path.join(directory, new_file_name)
df.to_csv(file_out, index=False)
