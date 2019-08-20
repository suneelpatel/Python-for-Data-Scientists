import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

# Set Directory
print(os.getcwd())

#Read dataset

original_df = pd.read_csv("Titanic.csv")

print("# of passengers in original data:" + str(len(original_df.index)))
print(original_df.head())

# Data Wrangling
# Finding Null Values
print(original_df.isnull().sum())

# Remove null values from age column
age_wrangled_df = original_df[pd.notnull(original_df['Age'])]
print("# of passengers in age wrangled data: " + str(len(age_wrangled_df.index))+ '\n')

embark_wrangled_df = age_wrangled_df[pd.notnull(age_wrangled_df['Embarked'])]
print("# of passengers in age & embark wrangled data:" + str(len(embark_wrangled_df.index)))

# Group Data by gender

gender_data = embark_wrangled_df.groupby('Sex', as_index = False)
gender_mean_data = gender_data.mean()

print('Total Survival Rate: ' + str(embark_wrangled_df['Survived'].mean()))

print('\n mean data by Gender')
print(gender_mean_data[['Sex','Survived','Age','Pclass','SibSp','Parch','Fare']])

# Look inside the data survival rates genderwise
total_df = gender_data['PassengerId'].count()
print(total_df)

total_df.columns = ['Sex','Total']
print(total_df)

gender_list = total_df['Sex'] # Save 'Sex" column in list for input in future plot
del total_df['Sex']
print(total_df)
print(gender_data)


# Find number of male and female survived
gender_survived_df = gender_data['Survived'].sum()
print(gender_survived_df)
del gender_survived_df['Sex']
print(gender_survived_df)

#Combine Series using vectorized operations
combined_df = total_df.add(gender_survived_df,fill_value = 0)
print(combined_df)

#Plot bar chart
combined_df.plot.bar(color = ['limegreen','dodgerblue'])
plt.title('Effect of Gender on Survival')
plt.xlabel('Gender')
plt.ylabel('# of People')
plt.xticks(range(len(gender_list)),gender_list)

survival_gender_list = [combined_df.loc[0]['Survived'],combined_df.loc[1]['Survived']]
total_gender_list = [combined_df.loc[0]['Total'],combined_df.loc[1]['Total']]

#define function to create value label plots
def create_value_labels(list_data, decimals, x_adjust,y_adjust):
    for x,y in enumerate(list_data):
        plt.text(x + x_adjust,  y + y_adjust, round(list_data[x], decimals), color = 'w', fontweight = 'bold')

create_value_labels(survival_gender_list, 1, -0.2, -50)
create_value_labels(total_gender_list, 1, 0.05, -50)
plt.show()

survivor_data = embark_wrangled_df.groupby('Survived', as_index=False)
survivor_mean_data = survivor_data.mean()
print(survivor_mean_data)

#Split data in to children and adults
children_data = embark_wrangled_df[embark_wrangled_df['Age']<=18] #children are passengers with ages<=18

adult_data = embark_wrangled_df[embark_wrangled_df['Age']>18]

## Count number of total and survival children and adults
children_count = children_data['PassengerId'].count()

adult_count = adult_data['PassengerId'].count()

survive_children_count = children_data['Survived'].sum()
survive_adult_count = adult_data['Survived'].sum()

##Put into list
children_list = [survive_children_count,children_count]
adult_list = [survive_adult_count,adult_count]
total_list = [children_count,adult_count]

print(children_list)
print(adult_list)
print(total_list)

survived_list = [survive_children_count, survive_adult_count]

## Create Pandas DataFrame for counts above
CvsA_df = pd.DataFrame([children_list, adult_list], columns=["Survived","Total"], index=['Children','Adult'])
print(CvsA_df)

## Create Plot

CvsA_df.plot.bar(color = ['limegreen', 'dodgerblue'])
plt.title('Number of survivals between children and adults')
plt.ylabel('# of people')
plt.xticks(range(len(CvsA_df.index)),CvsA_df.index)
## Add value labels
create_value_labels(survived_list, 1, -0.2, -50)
create_value_labels(total_list, 1, 0.05, -50)
plt.show()

## Create list with survival rates for children and adults

survival_rats_CvaA = [children_data.mean()['Survived'],adult_data.mean()['Survived']]
#
plt.bar(range(len(survival_rats_CvaA)),survival_rats_CvaA,align="center", color = ['dodgerblue','limegreen'])
plt.title('Survival rates between children and adults')
plt.ylabel("Suvival Rates")
plt.xticks(range(len(survival_rats_CvaA)),['Children','Adult'])

## Add value labels
create_value_labels(survival_rats_CvaA, 4, -0.1, -0.1)
plt.show()

## plot age distribution of all passangers
embark_wrangled_df['Age'].plot.hist(bins=range(100),color='dodgerblue')
plt.title('Age Distribution of all Passangers')
plt.xlabel('Age')
plt.ylabel('# of passangers')
plt.show()

## plot survior age distribution
survivor_data['Age'].plot.hist(bins=range(100),color = 'limegreen',label = "Survived")
plt.xlabel('Age')
plt.title('Survivor Age Distribution')
plt.ylabel('# of Passangers')
plt.show()

# Survived Stats
survived_stats = survivor_data['Age'].describe()
print(survived_stats)

# group data by age
age_data = embark_wrangled_df.groupby('Age', as_index=False)
age_mean_data = age_data.mean()

## Creates list that stores all age of passengers
age_list = age_mean_data['Age'].tolist()

## Determine number of passengers in age group
num_passengers_in_age = age_data.count()["PassengerId"]

## plot survival rates by age on scatter plot
scatter_plot1 = plt.scatter(age_mean_data['Age'],age_mean_data['Survived'], s=30, \
                            alpha= 0.9, c = num_passengers_in_age, cmap='RdYlGn',edgecolors='none',vmin= 0, vmax= 30)
plt.title('Effect of Age on Survival Rates')
plt.colorbar(scatter_plot1, label = "# of passanger")
plt.ylabel("Survival Rates")
plt.xlabel('Age')
plt.show()

#
count_age = age_data['PassengerId'].count()
## Get DataFrame of ages that have greater than 5 passengers

count_age_gt5 = count_age[count_age['PassengerId']>5]

## create list that stores all ages of passangers that have more than 5  passangers
age_gt5_list = count_age_gt5['Age'].values.tolist()
print(age_gt5_list)

## Keep data only with ages that have greater than 5 passengers
age_gt5_df = embark_wrangled_df[embark_wrangled_df['Age'].isin(age_gt5_list)]
print(age_gt5_df['PassengerId'].count())

##
age_gt5_df['Age'].plot.hist(bins=range(100),color = 'mediumorchid')
plt.title('Age Distribution of All Passengers [Cleaned Data]')
plt.xlabel('Age')
plt.ylabel('# of Passengers')
plt.show()

## group data by age
age_gt5_data = age_gt5_df.groupby('Age',as_index=False)
age_gt5_mean_data = age_gt5_data.mean()

## determine number of passengers in age group and put into new list
num_passengers_in_age_gt5 = age_gt5_data.count()['PassengerId']

## Re-plot survival rates by age on scatter plot
scatter_plot2 = plt.scatter(age_gt5_list,age_gt5_mean_data['Survived'], s=30, \
                            alpha=0.9, c= num_passengers_in_age_gt5, cmap='RdYlGn', edgecolors='none', vmin=0, vmax=30)
plt.title('Effect of Age on Survival Rates [Cleaned Data]')
plt.colorbar(scatter_plot2, label="# of passanger")
plt.ylabel("Survival Rates")
plt.xlabel('Age')
plt.show()

