# Import Packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Importing Data
data = pd.read_csv("InfectiousDiseasesJakarta.csv")
print(data)

# Search for Unique Values
print(data['year'].unique())
print(data['region'].unique())
print(data['disease_name'].unique())

# See the data types each columns
print(data.info())

# Changing the data types
data['year']=data['year'].astype('category')
data['region']=data['region'].astype('category')
data['disease_name']=data['disease_name'].astype('category')
print(data.info())

# Checking Missing Value
print(data.isnull().sum())

# Line Plot for Number of Infectious Disease Cases Each Year
yearly = data.groupby('year').number_of_cases.sum()
print(yearly)
yearly.plot(kind='line',xlabel='Year',ylabel='Total',title='Number of Infectious Disease Cases in Jakarta \n  2015-2020')

# Disease trend each year
trend = pd.pivot_table(data, index='year', columns='disease_name', values='number_of_cases')
print(trend)
trend.plot(kind='line',xlabel='Year', title='Number of Infectious Disease Cases in Jakarta \n  2015-2020').legend(loc='upper left')

# Bar Chart for Number of Infectious Disease Cases
def PlotGroup(group,title):
    data_a = data.groupby(group).number_of_cases.sum().sort_values()
    print(data_a)
    data_a.plot(kind="barh",title=title)

# Bar Chart for Number of Infectious Disease Cases 1    
PlotGroup(group='disease_name',title='Number of Infectious Disease Cases in Jakarta \n Grouped by Disease Name')

# Bar Chart for Number of Infectious Disease Cases 2
PlotGroup(group='region',title="Number of Infectious Disease Cases in Jakarta \n Grouped by Region")

# Bar Chart with Multicategory Function
def PlotGrid(x, column, title):
    sns.set_style('darkgrid')
    g1=sns.catplot(x=x,y='number_of_cases', col=column, data=data, kind='bar',ci=None,col_wrap=3,height=5,sharey=False)
    g1.fig.subplots_adjust(top=0.9)
    g1.fig.suptitle(title,fontsize=19)
    g1.set_xticklabels(rotation=30)
    plt.show()
    plt.clf()

# Bar Chart for Number of Infectious Disease Cases in Jakarta Based on Disease Name Seperated by Year
PlotGrid(x='disease_name',column='year',title="Number of Infectious Disease Cases in Jakarta Based on Disease Name \n Seperated by Year")

# Bar Chart for Number of Infectious Disease Cases in Jakarta Based on Disease Name Seperated by Region
PlotGrid(x='disease_name',column='region',title="Number of Infectious Disease Cases in Jakarta Based on Disease Name \n Seperated by Region")

# Bar Chart for Number of Infectious Disease Cases in Jakarta Based on Region Seperated by Year
PlotGrid(x='region',column='year',title="Number of Infectious Disease Cases in Jakarta Based on Region \n Seperated by Year")