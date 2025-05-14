import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt  

# Read the Excel file
df = pd.read_excel("Salary.xlsx")  # replace with your actual path if needed

# Display the first few rows
print(df.head())
print(df.shape)
print(df.describe())
print(df.isnull().sum())

df.plot(x='YearsExperience', y='Salary', style='*') 
plt.title('YearsExperience vs Salary')  
plt.xlabel('YearsExperience')  
plt.ylabel('Salary')  
plt.show()  
