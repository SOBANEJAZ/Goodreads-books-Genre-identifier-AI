import pandas as pd

# This additional script is to restructure the categorized books data
 
# Run this file after the main.py script
# Run this file after the main.py script
# Run this file after the main.py script

df = pd.read_csv("categorized_books.csv")

# Group by category and aggregate book titles
category_dict = df.groupby("Category")["Title"].apply(list).to_dict()

# Find the max number of books in any category
max_len = max(len(books) for books in category_dict.values())

# Create a new DataFrame with categories as columns
restructured_data = {category: books + [""] * (max_len - len(books)) for category, books in category_dict.items()}

# Convert dictionary to DataFrame
df_restructured = pd.DataFrame(restructured_data)

# Save to CSV
df_restructured.to_csv("restructured_books.csv", index=False)

print("File saved as 'restructured_books.csv'")
