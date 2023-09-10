import pandas as pd
import matplotlib.pyplot as plt

# Step 2: Read a dataset from a built-in library (e.g., Seaborn)
import seaborn as sns
iris = sns.load_dataset('iris')

# Step 3: Generate summary statistics
summary_statistics = iris.describe()

# Step 4: Create a data visualization (e.g., histogram)
sns.histplot(iris['sepal_length'], kde=True)
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
plt.show()

# Save summary statistics to a CSV file (optional)
summary_statistics.to_csv('summary_statistics.csv', index=False)
