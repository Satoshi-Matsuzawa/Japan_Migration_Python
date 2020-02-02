import pandas as pd
import os
import functions as func

directory_data = '../../Data/School/0001'
file_name = 'student_employed.csv'
file_read = os.path.join(directory_data, file_name)

df = pd.read_csv(file_read)

# Aggregate Employmnet Channels
dict_channel = {1: 'school', 2: 'school', 3: 'school',
                4: 'connections', 5: 'connections', 6: 'connections',
                7: 'ad', 8: 'high_school', 9: 'firm', 99: 'no_response'}
df['channel_agg'] = df.employment_channel
df.channel_agg = df.channel_agg.map(dict_channel)

#
# Get the share of students for each channel for each school.
dict_gender = {1: 'male', 2: 'female'}
df['gender_mapped'] = df.gender.map(dict_gender)
df['gender_count'] = 1
df_sum = pd.get_dummies(df, columns=['channel_agg']).groupby(
    ['school_id', 'gender_mapped']).sum()
# Count the total for each channel
df_sum_channel = df_sum.iloc[:, -6:].unstack(level=-1).reset_index()
# Rename multi-index columns
mi = df_sum_channel.columns
#   Save categories for later use
categories = list(pd.Index(e[0]for e in mi.tolist()[1:]).unique())
gender = list(pd.Index(e[1]for e in mi.tolist()[1:]).unique())

ind_channel = pd.Index([e[1] + '_' + e[0] for e in mi.tolist()[1:]])
ind_channel = ind_channel.insert(0, 'school_id')
df_sum_channel.columns = ind_channel

# Count the total number of graduates
df_sum_total = df_sum.iloc[:, -7].unstack(level=-1).reset_index()
df_sum_total.columns = ['school_id', 'female_employed', 'male_employed']

# Merge two dfs
df_merged = pd.merge(df_sum_channel, df_sum_total, on='school_id')

# Create Shares
for gen in gender:
    for cat in categories:
        func.create_share(df_merged, gen, cat, 'employed')

# Create Totals
columns = categories + ['employed']
for col in columns:
    func.create_total(df_merged, col)

# Create total shares
for cat in categories:
    func.create_total_share(df_merged, cat, 'employed')

# Plot Graphs
directory_graph = '../../Graphs/Students_Summary'
func.plot_dist(df_merged, 'total_channel_agg_school_share',
               'the share of students who used school', 'school_share',
               directory_graph)

func.plot_dist(df_merged, 'total_channel_agg_connections_share',
               'the share of students who used connections',
               'connections_share', directory_graph)

func.plot_joint(df_merged, 'total_channel_agg_school_share',
                'total_channel_agg_connections_share',
                'the share of school and connections',
                'school_and_connections', directory_graph)
