import matplotlib.pyplot as plt
import seaborn as sns
import os

# Functions for data cleaning


def replace_with_zero(df, gender, category, null):
    column = gender + '_' + category
    df.loc[:, column][df.loc[:, column] == null] = 0


# Functions for creating shares and totals
def create_share(df, gender, category, denominator):
    df[gender + '_' + category + '_share'] = df[gender +
                                                '_' + category] / df[gender + '_' + denominator]


def create_total(df, category):
    df['total' + '_' + category] = df['male' + '_' +
                                      category] + df['female' + '_' + category]


def create_total_share(df, category, denominator):
    df['total' + '_' + category + '_share'] = df['total' + '_' +
                                                 category] / df['total' + '_' + denominator]


# Fuctions for seaborn graphs.
plt.rcParams['figure.figsize'] = [10, 5]


def plot_dist(data, column, title_name, output_name, directory_graph, bins=20):
    sns_plot = sns.distplot(data[column].dropna(), bins=bins)
    sns_fig = sns_plot.get_figure()
    plt.title('Distribution of ' + title_name)
    file_name = output_name + '_dist.png'
    file_out = os.path.join(directory_graph, file_name)
    sns_fig.savefig(file_out)
    plt.show()


def plot_count(data, column, category, title_name, output_name, directory_graph):
    sns_plot = sns.catplot(x=column, kind='count', hue=category, data=data)
    plt.title('Counts of ' + title_name)
    file_name = output_name + '_count.png'
    file_out = os.path.join(directory_graph, file_name)
    sns_plot.savefig(file_out)
    plt.show()


def plot_joint(data, column1, column2, title_name, output_name, directory_graph):
    sns_plot = sns.jointplot(x=column1, y=column2, data=data)
    plt.title('Joint plot of ' + title_name)
    file_name = output_name + '_joint.png'
    file_out = os.path.join(directory_graph, file_name)
    sns_plot.savefig(file_out)
    plt.show()
