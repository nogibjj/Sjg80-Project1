import pandas as pd
import matplotlib.pyplot as plt
import io
import pdfkit
import markdown
import matplotlib.pyplot as plt

# Step 2: Read a dataset CSV
import seaborn as sns
iris = pd.read_csv("iris.csv")

# Step 3: Generate summary statistics
summary_statistics = iris.describe()
print(summary_statistics)

# Step 4: Create a data visualization (e.g., histogram)
sns.histplot(iris["sepal_length"], kde=True)
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Frequency")
plt.show()

# Save summary statistics to a CSV file
summary_statistics.to_csv("summary_statistics.csv", index=False)

# Convert summary statistics to Markdown string
markdown_string = markdown.markdown(summary_statistics.to_markdown())

# Save Markdown string to PDF file
with open('iris_summary_statistics.pdf', 'w') as f:
  f.write(markdown_string)

# Save Markdown string to Markdown file
with open('iris_summary_statistics.md', 'w') as f:
  f.write(markdown_string)
