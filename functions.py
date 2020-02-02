import matplotlib.pyplot as plt
import matplotlib
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


def plot_dist(data, column, title_name, output_name, directory_graph, bins=20):
    plt.figure(figsize=(3.8, 2.0))
    sns_plot = sns.distplot(data[column].dropna(), bins=bins)
    sns_fig = sns_plot.get_figure()
    plt.title('Distribution of ' + title_name)
    file_name_pgf = output_name + '_dist.pgf'
    file_out_pgf = os.path.join(directory_graph, file_name_pgf)
    sns_fig.savefig(file_out_pgf)
    plt.show()
#    file_name_pdf = output_name + '_dist.pdf'
#    file_out_pdf = os.path.join(directory_graph, file_name_pdf)
#    sns_fig.savefig(file_out_pdf)
#    plt.show()


def plot_count(data, column, category, title_name, output_name, directory_graph):
    plt.figure(figsize=(3.8, 2.0))
    sns_plot = sns.catplot(y=column, kind='count', hue=category, data=data)
    plt.title('Counts of ' + title_name)
    file_name_pgf = output_name + '_count.pgf'
    file_out_pgf = os.path.join(directory_graph, file_name_pgf)
    sns_plot.savefig(file_out_pgf)
    plt.show()
#    file_name_pdf = output_name + '_count.pdf'
#    file_out_pdf = os.path.join(directory_graph, file_name_pdf)
#    sns_plot.savefig(file_out_pdf)
#    plt.show()


def plot_joint(data, column1, column2, title_name, output_name, directory_graph):
    plt.figure(figsize=(3.8, 2.0))
    sns_plot = sns.jointplot(x=column1, y=column2, data=data)
    plt.title('Joint plot of ' + title_name)
    file_name_pgf = output_name + '_joint.pgf'
    file_out_pgf = os.path.join(directory_graph, file_name_pgf)
    sns_plot.savefig(file_out_pgf)
    plt.show()
#    file_name_pdf = output_name + '_joint.pdf'
#    file_out_pdf = os.path.join(directory_graph, file_name_pdf)
#    sns_plot.savefig(file_out_pdf)
#    plt.show()
