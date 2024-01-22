# The Sparks Foundation , GRIP 
# Exploratory data Analysis 
# NAME- VIBHU KANT 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st
import seaborn as sns

# loading Excel file
data=pd.read_csv('C:/Users/user/Desktop/IIT DELHI/SPARKS/SampleSuperstore.csv')
data
data.describe()     # summary of data
total=data.isnull().sum().sort_values(ascending=False)   # To find any missing Values in data
total
# Checking for outliers  
plt.scatter(data.Category,data.Profit)     # through scatterplot 
plt.show()
plt.boxplot(data.Profit)        # through boxplot
plt.show()

# removing outliers only from Each Categories 
tech_data=data[data["Category"]=="Technology"]      # Technology category Subpart
tech_data
office_data=data[data["Category"]=="Office Supplies"]       # Office supplies category Subpart
office_data
furniture_data=data[data["Category"]=="Furniture"]          # Furniture category Subpart
furniture_data

# outlier removing function
def rmv_outl_iqr(data,coloumn):
    q1=np.percentile(coloumn,25)
    q3=np.percentile(coloumn,75)
    iqr=q3-q1
    lower_bound=q1-1.5*iqr
    upper_bound=q3+1.5*iqr
    outliers=(coloumn<lower_bound)| (coloumn>upper_bound)
    clean_data=data[~outliers]
    return clean_data

cleaned_data1=rmv_outl_iqr(tech_data,tech_data.Profit)         # Outlier removed Tech category data
cleaned_data1
cleaned_data2=rmv_outl_iqr(office_data,office_data.Profit)      # Outlier removed Office category data
cleaned_data2
cleaned_data3=rmv_outl_iqr(furniture_data,furniture_data.Profit)    # Outlier removed Furniture category data
cleaned_data3
#  Merging all three outlier removed data
cleaned_data=pd.concat([cleaned_data1,cleaned_data2,cleaned_data3],axis=0,ignore_index=True)  
cleaned_data

# Category wise Profit Plot
plt.scatter(cleaned_data.Category,cleaned_data.Profit)
plt.show()
# Category wise sum of Profit
result=cleaned_data.groupby('Category')['Profit'].sum()
result

# Subcategory wise Profit Plot
plt.scatter(cleaned_data.Subcategory,cleaned_data.Profit)
plt.show()

# Sum of profit in each subcategories

result1=cleaned_data.groupby('Subcategory')['Profit'].sum()
result1

# Plotting a line graph for this result1
result2 = {
    'Accessories': 23386.6622,
    'Appliances': 3855.7580,
    'Art': 4806.5315,
    'Binders': 5230.4905,
    'Bookcases': 1163.7095,
    'Chairs': 5490.5005,
    'Copiers': 2182.9326,
    'Envelopes': 2797.1255,
    'Fasteners': 949.5182,
    'Furnishings': 11568.0608,
    'Labels': 3228.3857,
    'Machines': 1901.5791,
    'Paper': 14374.6311,
    'Phones': 26317.7075,
    'Storage': 5190.6370,
    'Supplies': 1066.5462,
    'Tables': -370.8917,
}

# Sorting the data by values in ascending order
sorted_data = sorted(result2.items(), key=lambda x: x[1])

# Extracting the categories and values for plotting
Subcategories, Profit = zip(*sorted_data)

# Creating the line plot
plt.figure(figsize=(10, 6))
plt.plot(Subcategories, Profit, marker='o', linestyle='-', color='b')
plt.title('Line Plot for profit of  Subcategories')
plt.xlabel('Subcategories')
plt.ylabel('Profit')
plt.xticks(rotation=45, ha='right')
plt.grid(True)
plt.show()


## finding correlation of the cleaned data and Creating Heat map
correlation_matrix = cleaned_data[['Sales', 'Quantity', 'Discount', 'Profit']].corr()
correlation_matrix
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Correlation Heatmap')
plt.show()

## Findings of Exploratory Data Analysis

# The given data has 0 missing values. Outliers were present in the profit coloumn.
# Category wise Technology gives the highest profit and Furniture gives the lowest , 
# hence we should work on furniture segment. Subcategory wise, Table is one which is making loss 
# and also Fasteners, Supplies and Bookcases are making very low profit while Phone , 
# Accessories and Paper are generating highest profit. There is a moderate positive correlation 
# between sales and profit, which suggests that increasing sales could lead to higher profits. 
# However, there is also a negative correlation between discount and profit, 
# meaning that offering too many discounts could decrease profits. 
# The company could focus on reducing discounts to increase profitability.

# Some of the Business Problems that can be derived are as follows- 
# Some items in Furniture segment is generating very few profit. 
# Giving discount is not increasing the sells hence reducing the profit. 
# Some outliers are present in the data , So company should investigate about cause of it.


