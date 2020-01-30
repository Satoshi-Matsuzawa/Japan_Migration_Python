# Classify schools

import pandas as pd
import numpy as np
import os

directory = '../../Data/School/0001'
file_name = 'school.csv'
file_read = os.path.join(directory, file_name)

df = pd.read_csv(file_read)

# Hypothesis: the first two digits in the school_id represents the city
school_group = [item[:-1] for item in df.school_id.unique().astype(str)]
school_group = np.unique(np.array(school_group).astype(int))

# This grouping should be replaced by the new data and "map" method

# Add school groups to the dataframe
for item in school_group:
    search = item.astype(str) + '[0-9]$'
    bool_match = df.school_id.astype(str).str.match(search)
    df.loc[bool_match, 'school_group'] = item

# Aggregate schools by groups
df_school_grouped = df.iloc[:, 1:].groupby('school_group').sum()
