import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

directory_data = '../../Data/School/0001'
file_name = 'student_employed.csv'
file_read = os.path.join(directory_data, file_name)

df = pd.read_csv(file_read)

# Drop rows which don't have the salary info
df = df[(df.salary != 99999)]

# Fuctions for seaborn graphs
plt.rcParams['figure.figsize'] = [10, 5]
directory_graph = '../../Graphs/Students_Employed'


def plot_dist(data, column, title_name, output_name, bins=20):
    sns_plot = sns.distplot(data[column].dropna())
    sns_fig = sns_plot.get_figure()
    plt.title('Distribution of ' + title_name)
    file_name = output_name + '_dist.png'
    file_out = os.path.join(directory_graph, file_name)
    sns_fig.savefig(file_out)
    plt.show()


def plot_count(data, column, category, title_name, output_name):
    sns_plot = sns.catplot(x=column, kind='count', hue=category, data=data)
    plt.title('Counts of ' + title_name)
    file_name = output_name + '_count.png'
    file_out = os.path.join(directory_graph, file_name)
    sns_plot.savefig(file_out)
    plt.show()


# Aggregate Employmnet Channels
dict_channel = {1: 'school', 2: 'school', 3: 'school',
                4: 'connections', 5: 'connections', 6: 'connections',
                7: 'ad', 8: 'high_school', 9: 'firm', 99: 'no_response'}
df['channel_agg'] = df.employment_channel
df.channel_agg = df.channel_agg.map(dict_channel)


# Distribution of salary at individual level
plot_dist(df, 'salary', 'salary', 'salary_unconditional')

plot_dist(df[df.channel_agg == 'school'], 'salary',
          'salary whose channel is school', 'salary_school')

plot_dist(df[df.channel_agg == 'connections'], 'salary',
          'salary whose channel is connections', 'salary_connections')


# Distribution of salary at individual level
# Ignore these graphs because they are not informative
# plot_dist(df[df.firm_size != 9999], 'firm_size',
#          'firm_size', 'firm_size_unconditional')

# plot_dist(df[(df.firm_size != 9999) & (df.channel_agg == 'school')],
#          'firm_size', 'firm size whose channel is school',
#          'firm_size_school')

# plot_dist(df[(df.firm_size != 9999) & (df.channel_agg == 'connections')],
#          'firm_size', 'firm size whose channel is connections',
#          'firm_size_connections')

# Show jobs through school are more likely to be manufacturing
data = df[(
    df.channel_agg == 'school') | (df.channel_agg == 'connections')]
plot_count(data, 'industry', 'channel_agg',
           'industry for each channels', 'industry')


# Get average salary for each channel at the school level
df_mean = df.groupby(['school_id', 'channel_agg']).mean()
df_mean_salary = df_mean.salary.unstack(level=-1).reset_index()
df_mean_firm_size = df_mean.firm_size.unstack(level=-1).reset_index()

# Plot salaries for each category at the school level
plot_dist(df_mean_salary, 'school',
          'the mean salary whose channel is school', 'mean_salary_school')

plot_dist(df_mean_salary, 'connections',
          'the mean salary whose channel is connections', 'mean_salary_connections')

# Compare the mean of salary whose channel is school vs. connections
df_mean_salary['salary_gap'] = df_mean_salary.school - \
    df_mean_salary.connections
plot_dist(df_mean_salary, 'salary_gap', 'salary gap at the school level',
          'salary_gap_at_school', bins=25)

# Compare the mean of firm size
