import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Generate summary statistics
summary_stats = df.describe()

# Create a data visualization
sns.pairplot(df, hue=iris.target_names[iris.target])
plt.show()

print(summary_stats)
