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
# May create a file that maps categorical variables

# Drop rows which don't have the salary and firm size info.
df = df[(df.salary != 99999) & (df.firm_size != 9999)]

#
# Distribution of salary at individual level.

directory_graph = '../../Graphs/Students_Employed'

func.plot_dist(df, 'salary', 'salary', 'salary_unconditional', directory_graph)

func.plot_dist(df[df.channel_agg == 'school'], 'salary',
               'salary whose channel is school', 'salary_school',
               directory_graph)

func.plot_dist(df[df.channel_agg == 'connections'], 'salary',
               'salary whose channel is connections', 'salary_connections',
               directory_graph)


# Distribution of salary at individual level.
# Ignore these graphs because they are not informative.
# plot_dist(df[df.firm_size != 9999], 'firm_size',
#          'firm_size', 'firm_size_unconditional')

# plot_dist(df[(df.firm_size != 9999) & (df.channel_agg == 'school')],
#          'firm_size', 'firm size whose channel is school',
#          'firm_size_school')

# plot_dist(df[(df.firm_size != 9999) & (df.channel_agg == 'connections')],
#          'firm_size', 'firm size whose channel is connections',
#          'firm_size_connections')

# Show jobs through school are more likely to be manufacturing.
data = df[(df.channel_agg == 'school') | (df.channel_agg == 'connections')]
func.plot_count(data, 'industry', 'channel_agg',
                'industry for each channels', 'industry', directory_graph)

#
# Get average salary for each channel at the school level.
df_mean = df.groupby(['school_id', 'channel_agg']).mean()
df_mean_salary = df_mean.salary.unstack(level=-1).reset_index()
df_mean_firm_size = df_mean.firm_size.unstack(level=-1).reset_index()

# Plot salaries for each category at the school level.
func.plot_dist(df_mean_salary, 'school',
               'the mean salary whose channel is school', 'mean_salary_school',
               directory_graph)

func.plot_dist(df_mean_salary, 'connections',
               'the mean salary whose channel is connections',
               'mean_salary_connections', directory_graph)

# Plot firm size for each category at the school level.
func.plot_dist(df_mean_firm_size, 'school',
               'the mean firm size whose channel is school',
               'mean_firm_size_school', directory_graph)

func.plot_dist(df_mean_firm_size, 'connections',
               'the mean firm size whose channel is connections',
               'mean_firm_size_connections', directory_graph)

# Compare the mean of salary whose channel is school vs. connections.
df_mean_salary['salary_gap'] = df_mean_salary.school - \
    df_mean_salary.connections
func.plot_dist(df_mean_salary, 'salary_gap', 'salary gap at the school level',
               'salary_gap_at_school', directory_graph, bins=30)
# Compare the mean of firm size.
df_mean_firm_size['firm_size_gap'] = df_mean_firm_size.school - \
    df_mean_firm_size.connections
func.plot_dist(df_mean_firm_size, 'firm_size_gap',
               'firm size gap at the school level', 'firm_size_gap_at_school',
               directory_graph, bins=30)
