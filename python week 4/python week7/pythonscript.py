import pandas as pd

# Loading the dataset
url = 'path_to_your_dataset.csv' 
df = pd.read_csv(url)

# Display the first few rows of the dataset
df.head()
# Checking data types and missing values
df.info()

# Checking for missing values
df.isnull().sum()
# Droping rows with missing values
df.dropna(inplace=True)

# Alternatively, filling missing values with the mean or median
df.fillna(df.mean(), inplace=True)  # Replacing missing values with column mean

# Computing basic statistics
df.describe()
# Grouping by 'species' and computing mean of numerical columns
grouped = df.groupby('species').mean()

# Display the result
print(grouped)

import matplotlib.pyplot as plt

#time-series data
df['date'] = pd.to_datetime(df['date'])  # Convert to datetime if needed
df.set_index('date', inplace=True)
df['sales'].plot(kind='line')

# Customizing plot
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend(['Sales'])
plt.show()

# Ploting histogram for petal length
df['petal_length'].plot(kind='hist', bins=20)

# Customizing plot
plt.title('Distribution of Petal Length')
plt.xlabel('Petal Length')
plt.show()
# Plot scatter plot between sepal length and petal length
df.plot(kind='scatter', x='sepal_length', y='petal_length')

# Customizing plot
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.show()

import seaborn as sns

# Boxplot to compare numerical columns across categories
sns.boxplot(x='species', y='petal_length', data=df)

# Customize plot
plt.title('Petal Length Distribution by Species')
plt.show()

try:
    df = pd.read_csv('path_to_your_dataset.csv')
except FileNotFoundError:
    print("File not found. Please check the path.")
except pd.errors.EmptyDataError:
    print("No data. The file is empty.")







