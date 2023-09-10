import pandas as pd
import matplotlib.pyplot as plt
import io
import pdfkit

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

# Create a PDF file
pdf = pdfkit.PDF()

# Write the summary statistics to the PDF file
with io.open('summary_statistics.pdf', 'w', encoding='utf-8') as f:
    pdf.write(f, orientation='landscape')

# Create a Markdown file
markdown = "## Summary Statistics"
markdown += iris.describe().to_markdown()

# Write the summary statistics to the Markdown file
with open('summary_statistics.md', 'w') as f:
    f.write(markdown)
