import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a sample grades dataset
data = {
    'Student': ['SREE', 'ADITHYA', 'NATHI', 'ZOYA', 'DEV' ],
    'Programming': [88, 78, 88, 60, 98, ],
    'law': [90, 65, 65, 70, 80,],
    'Data Structure': [78, 72, 88, 65, 82,],
    'AI': [82, 69, 90, 55, 78, ],
    'IoT': [88, 95, 93, 56, 85,]
}
df = pd.DataFrame(data)

# Ask meaningful questions
# - Who are the top performers overall?
# - Is there a subject where students generally score higher or lower?
# - Are there students consistently performing well across all subjects?

# Explore data structure
print("\nData types:\n", df.dtypes)
print("\nSummary statistics:\n", df.describe())

# Identify trends & patterns
df['Average'] = df[['Programming', 'law', 'Data Structure', 'AI', 'IoT']].mean(axis=1)
df_sorted = df.sort_values(by='Average', ascending=False)
print("\nStudents sorted by average score:\n", df_sorted[['Student', 'Average']])

# Plot: Average score per student
sns.barplot(x='Average', y='Student', data=df_sorted, palette='viridis')
plt.title('Average Scores per Student')
plt.xlim(0, 100)
plt.show()

# Plot: Subject-wise average scores
subject_means = df[['Programming', 'law', 'Data Structure', 'AI', 'IoT']].mean()
subject_means.plot(kind='bar', color='teal')
plt.title('Average Score per Subject')
plt.ylabel('Average Score')
plt.ylim(0, 100)
plt.show()

# Test hypotheses and validate assumptions
print("\nMean score in Art:", df['IoT'].mean())
print("Mean score in History:", df['AI'].mean())

# Detect potential data issues
print("\nMissing values:\n", df.isnull().sum())
print("\nStudents with average below 65:\n", df[df['Average'] < 65][['Student', 'Average']])

sns.boxplot(data=df[['Programming', 'law', 'Data Structure', 'AI', 'IoT']])
plt.title('Score Distribution per Subject')
plt.ylim(0, 100)
plt.show()
