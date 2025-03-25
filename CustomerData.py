
# prompt: analyze the customer_data.csv and give me result ; fioelds are Customer Number	Show price	Clothes ironed	Watch Price	Age	Phone price	Gold	Bought?
# also plot graphs

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the customer data
df = pd.read_csv('customer_data.csv')

# Display basic information
print(df.info())
print(df.describe())

# Visualize the distribution of customer age
plt.figure(figsize=(8, 6))
sns.histplot(df['Age'], bins=20, kde=True)
plt.title('Distribution of Customer Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Visualize the relationship between show price and watch price
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Show price', y='Watch Price', data=df)
plt.title('Show Price vs. Watch Price')
plt.xlabel('Show Price')
plt.ylabel('Watch Price')
plt.show()

# Analyze the relationship between age and whether a customer bought a product
plt.figure(figsize=(8, 6))
sns.boxplot(x='Bought?', y='Age', data=df)
plt.title('Age Distribution by Purchase')
plt.xlabel('Bought?')
plt.ylabel('Age')
plt.show()

# Analyze the correlation between different features
correlation_matrix = df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Analyze the relationship between gold ownership and purchase
plt.figure(figsize=(8, 6))
sns.countplot(x='Gold', hue='Bought?', data=df)
plt.title('Gold Ownership and Purchase')
plt.xlabel('Gold')
plt.ylabel('Count')
plt.show()

# Analyze the relationship between phone price and purchase
plt.figure(figsize=(8, 6))
sns.boxplot(x='Bought?', y='Phone price', data=df)
plt.title('Phone Price Distribution by Purchase')
plt.xlabel('Bought?')
plt.ylabel('Phone Price')
plt.show()


# You can continue adding more analyses and visualizations based on your specific needs and interests.
# For example, you can analyze the impact of Clothes ironed, or create more complex plots like pairplots.
