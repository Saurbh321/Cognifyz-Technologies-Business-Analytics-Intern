#!/usr/bin/env python
# coding: utf-8

# **Task 1: Data Overview
# Objective: Understand the dataset structure**

# In[35]:


import pandas as pd

#Load the dataset

file_path = '/mnt/data/Data_set 2 - Copy.csv'
df = pd.read_csv('/content/Data_set 2 - Copy.csv')

#information from the dataset

df_info = df.info()

#Display row

df_head = df.head()
df_info, df_head


# **Task 2: Gender Distribution
# Objective: Visualize gender distribution in
# the dataset.**

# In[40]:


import matplotlib.pyplot as plt

# Extract gender information

gender_counts = df['gender'].value_counts()

# Create a bar chart for gender distribution
plt.figure(figsize=(6, 4))
gender_counts.plot(kind='bar', color=['skyblue', 'lightgreen'])
plt.title('Gender Distribution in the Dataset')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.show()


# **Task 3: Descriptive Statistics
# Objective: Present basic statistics for
# numerical columns**

# In[48]:


# Identify numerical columns
numerical_columns = df.select_dtypes(include=['int64', 'float64'])

# Calculate descriptive statistics: mean, median, and standard deviation

descriptive_stats = numerical_columns.agg(['mean', 'median', 'std'])

descriptive_stats


# **Task 4: Most Preferred Investment
# Avenue
# Objective: Identify the most preferred
# investment avenue**

# In[49]:


# Extract the 'Investment_Avenues' column
avenue_counts = df['Investment_Avenues'].value_counts()

# Display the most preferred investment avenue
most_preferred = avenue_counts.idxmax()
print(f"The most preferred investment avenue is: {most_preferred}")

# Optional: Visualize the distribution
avenue_counts.plot(kind='bar', title='Investment Avenue Preferences')
plt.xlabel('Investment Avenues')
plt.ylabel('Frequency')
plt.show()


# **Task 5: Reasons for Investment
# Objective: Analyze and summarize reasons
# for investment choices.**

# In[50]:


# Extract all reason columns
reason_columns = ['Reason_Equity', 'Reason_Mutual', 'Reason_Bonds', 'Reason_FD']
all_reasons = df[reason_columns].values.flatten()

# Convert to DataFrame for easier analysis
reasons_df = pd.DataFrame(all_reasons, columns=['Reason'])

# Group by reason and count occurrences
reason_counts = reasons_df['Reason'].value_counts()
print(reason_counts)

# Optional: Categorize into themes manually based on content analysis


# **Task 6: Savings Objectives
# Objective: Identify and present main
# savings objectives**

# In[51]:


# Extract the 'savings objectives' column
savings_objectives = df['What are your savings objectives?']

# Count occurrences of each unique objective
objective_counts = savings_objectives.value_counts()

# Print the summary
print("Main Savings Objectives:\n", objective_counts)

# Optional: Visualize with a bar chart
objective_counts.plot(kind='bar', title='Savings Objectives')
plt.xlabel('Savings Objectives')
plt.ylabel('Frequency')
plt.show()


# **Task 7: Common Information Sources
# Objective: Analyze common sources participants
# rely on for investment information.**

# In[52]:


# Extract the 'Source' column
info_sources = df['Source']

# Count occurrences of each unique source
source_counts = info_sources.value_counts()

# Print the summary
print("Common Information Sources:\n", source_counts)

# Optional: Visualize with a bar chart
source_counts.plot(kind='bar', title='Investment Information Sources')
plt.xlabel('Sources')
plt.ylabel('Frequency')
plt.show()


# **Task 8: Investment Duration
# Objective: Calculate the average investment
# duration.**

# In[53]:


# Map duration categories to numerical values (in years)
duration_mapping = {
    'Less than 1 year': 0.5,
    '1-3 years': 2,
    '3-5 years': 4,
    'More than 5 years': 6  # or another estimate
}

# Apply the mapping to the 'Duration' column
df['Duration_Numeric'] = df['Duration'].map(duration_mapping)

# Calculate the average duration
average_duration = df['Duration_Numeric'].mean()
print(f"The average investment duration is approximately {average_duration:.2f} years.")


# **Task 9: Expectations from Investments
# Objective: Summarize participants' expectations
# from investments**

# In[54]:


# Extract the 'Expect' column
expectations = df['Expect']

# Count occurrences of each unique expectation
expectation_counts = expectations.value_counts()

# Print the summary
print("Participants' Investment Expectations:\n", expectation_counts)

# Optional: Visualize with a bar chart
expectation_counts.plot(kind='bar', title='Investment Expectations')
plt.xlabel('Expectation Categories')
plt.ylabel('Frequency')
plt.show()


# **Task 10: Correlation Analysis
# Objective: Explore potential correlations
# between factors**

# In[58]:


import seaborn as sns
import matplotlib.pyplot as plt

# Ensure that all relevant columns are numeric
# Assuming 'Duration_Numeric' already created, we may also map 'Expect' to numeric

expectation_mapping = {'10%-20%': 15, '20%-30%': 25, '30%-40%': 35, 'More than 40%': 45}
df['Expect_Numeric'] = df['Expect'].map(expectation_mapping)

# Select numerical columns for correlation
corr_columns = ['age', 'Duration_Numeric', 'Expect_Numeric']

# Calculate correlation matrix
correlation_matrix = df[corr_columns].corr()

# Visualize the correlation matrix with a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix for Age, Investment Duration, and Expected Returns')
plt.show()

# Optional: Scatter plots to visualize relationships
sns.pairplot(df[corr_columns])
plt.show()

