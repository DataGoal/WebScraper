import pandas as pd

# Define lists to store extracted data
book_names = []
author_names = []
publications = []
is_winners = []
genre = []
years = []

# Read the .txt file line by line
with open('C:\\Users\\bbala\\Downloads\\book_data.txt', 'r') as file:
    for line in file:
        if "by" in line and "published by" in line:
            # Extract book name
            book_name = line.split(" by ")[0].strip()

            # Extract author name
            author_name = line.split(" by ")[1].split(",")[0].strip()

            # Extract publication
            publication = line.split("published by ")[1].split(".")[0].strip()

            # Check if the line contains "Winner"
            is_winner = "Winner" in line

            # Check if the line contains "Best Novel" and set genre accordingly
            genre.append("Best Novel" if "Best Novel" in line else "NA")

            # Extract year
            year = line.split()[-1].strip()
        else:
            raise ValueError("Line does not contain 'by' and 'published by':\n" + line)

        # Append the extracted values to the respective lists
        book_names.append(book_name)
        author_names.append(author_name)
        publications.append(publication)
        is_winners.append(is_winner)
        years.append(year)

# Create a pandas DataFrame from the lists
data = {
    'book_name': book_names,
    'author_name': author_names,
    'publication': publications,
    'is_winner': is_winners,
    'genre': genre,
    'year': years
}

df = pd.DataFrame(data)

# Save the DataFrame as a CSV file
df.to_csv('C:\\Users\\bbala\\Downloads\\book_data.csv', index=False)