import os
import csv
import time
import pandas as pd
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")


def detect_encoding(file_path):
    """
    Detect the file encoding by attempting to read with different encodings.

    Args:
        file_path (str): Path to the input file.

    Returns:
        str: Detected encoding or 'utf-8' as a fallback.
    """
    encodings_to_try = ["utf-8", "latin-1", "iso-8859-1", "cp1252"]
    for encoding in encodings_to_try:
        try:
            with open(file_path, "r", encoding=encoding) as f:
                f.read()
            return encoding
        except UnicodeDecodeError:
            continue
    return "utf-8"  # Fallback to utf-8 if no encoding works


def clean_text(text):
    """
    Clean text by removing or replacing problematic characters.

    Args:
        text (str): Input text.

    Returns:
        str: Cleaned text.
    """
    if pd.isna(text):
        return "Unknown"
    if not isinstance(text, str):
        return str(text)
    # Remove or replace problematic characters
    return text.encode("ascii", "ignore").decode("ascii")


def categorize_book(title: str, author: str, client) -> str:
    """
    Use Groq Llama to categorize a book based on predefined categories.

    Args:
        title (str): Title of the book.
        author (str): Author of the book.
        client: Groq API client

    Returns:
        str: Categorized book genre.
    """
    categories = """
    - Classics: Shakespeare, Dostoevsky, Orwell, Austen
    - Science Fiction: Asimov, Clarke, Bradbury, sci-fi
    - Fantasy: Tolkien, Sanderson, Martin, fantasy
    - Mystery & Thriller: Agatha Christie, Dan Brown, thriller, mystery
    - Romance: Nicholas Sparks, romance
    - Philosophical Fiction: Kafka, Camus, Huxley, existential
    - Contemporary & Literary Fiction: Murakami, Sally Rooney
    - Historical Fiction: Khaled Hosseini, Marcus Zusak
    - Horror: Stephen King, Lovecraft
    - Magical Realism: Gabriel Garcia Marquez, Isabel Allende
    - LGBTQ+ Fiction: Andre Aciman, Ocean Vuong
    - Young Adult: John Green, Suzanne Collins
    - Psychology & Self-Help: Daniel Kahneman, Mark Manson, psychology, self-help
    - Business & Productivity: Cal Newport, Peter Thiel, business, productivity
    - Biographies & Memoirs: Steve Jobs, Michelle Obama, biography, memoir
    - History & Politics: Yuval Noah Harari, Churchill, history, politics
    - Philosophy & Thought: Nietzsche, Sartre, Plato, philosophy
    - Finance & Investing: Benjamin Graham, Morgan Housel, finance, investing
    - True Crime: Truman Capote, Ann Rule, true crime
    - Travel & Adventure: Bill Bryson, Cheryl Strayed, travel, adventure
    - Food & Cookbooks: Julia Child, Samin Nosrat, food, cookbooks
    - Social Justice & Activism: Angela Davis, Bryan Stevenson, Ibram X. Kendi, Naomi Klein activism
    - Computer Science: AI, Programming, Algorithms, Computer Science, web development
    - Astronomy & Cosmology: Stephen Hawking, Carl Sagan, cosmology, astronomy
    - Biology & Life Sciences: Richard Dawkins, E.O. Wilson, biology, evolution
    - Engineering & Physics: Feynman, Maxwell, engineering, physics
    - Medicine & Neuroscience: Oliver Sacks, Robert Sapolsky, medicine, neuroscience
    - Health & Fitness: David Goggins, Arnold Schwarzenegger, fitness, health
    - Religion & Spirituality: Eckhart Tolle, Dalai Lama, religion, spirituality
    - Climate & Environment: Bill McKibben, Elizabeth Kolbert, climate, environment
    """

    prompt = f"""
    Categorize the following book into one of the predefined categories.
    Book Title: {title}
    Author: {author}

    Available Categories:
    {categories}
    Examples: 
    1. "The Book Thief" by Markus Zusak -> Historical Fiction
    2. "1984" by George Orwell -> Classics
    3. "Sapiens" by Yuval Noah Harari -> History & Politics
    4. "The 7 Habits of Highly Effective People" by Stephen Covey -> Psychology & Self-Help
    5. "The Da Vinci Code" by Dan Brown -> Mystery & Thriller
    8. "The Selfish Gene" by Richard Dawkins -> Biology & Life Sciences


    Provide ONLY the most appropriate category name. Be precise and concise. 
    Return just the category name without any additional text or explanation.
    """

    try:
        time.sleep(5)
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful book categorization assistant. Respond with only the category name.",
                },
                {"role": "user", "content": prompt},
            ],
            max_tokens=50,
            temperature=0.7,
        )
        category = response.choices[0].message.content.strip()
        return category
    except Exception as e:
        print(f"Error categorizing book '{title}' by {author}: {e}")
        return "Uncategorized"


def process_books_csv(input_file: str, output_file: str):
    """
    Process input CSV and create a categorized output CSV.

    Args:
        input_file (str): Path to input CSV.
        output_file (str): Path to output CSV.
    """
    # Load API key from environment variable
    api_key = GROQ_API_KEY
    if not api_key:
        raise ValueError("GROQ_API_KEY environment variable not set")

    # Initialize Groq client
    client = Groq(api_key=api_key)

    # Detect encoding
    detected_encoding = detect_encoding(input_file)
    print(f"Detected encoding: {detected_encoding}")

    # Read input CSV with detected encoding
    df = pd.read_csv(input_file, encoding=detected_encoding)

    # Validate column names
    required_columns = ["Title", "Author"]
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Required column '{col}' not found in the CSV")

    # Keep only essential columns
    df = df[["Title", "Author"]]

    # Clean column names and data
    df.columns = [clean_text(col) for col in df.columns]
    df["Title"] = df["Title"].apply(clean_text)
    df["Author"] = df["Author"].apply(clean_text)

    # Add category column with error handling
    categories = []
    for index, row in df.iterrows():
        try:
            category = categorize_book(row["Title"], row["Author"], client)
            categories.append(category)
            print(f"Categorized: {row['Title']} by {row['Author']} - {category}")
        except Exception as e:
            print(f"Failed to categorize row {index}: {e}")
            categories.append("Uncategorized")

    df["Category"] = categories

    # Save to output CSV
    df.to_csv(output_file, index=False, encoding="utf-8")
    print(f"Categorization complete. Results saved to {output_file}")


def main():
    input_file = "goodreads_library_export.csv"  # Replace with your input file path
    output_file = "categorized_books.csv"
    process_books_csv(input_file, output_file)


if __name__ == "__main__":
    main()
