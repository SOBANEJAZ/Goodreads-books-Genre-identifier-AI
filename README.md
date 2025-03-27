# 📚 Goodreads Book Categorizer AI | Groq Llama LLM

## Overview

Goodreads Book Categorizer AI is an intelligent Python tool that automatically categorizes books from a CSV library using advanced AI models. Leveraging the Groq API with Llama 3.1, this script transforms your raw book data into a richly categorized library.

## 🌟 Features

- **Automatic Book Categorization**: Uses AI to classify books into predefined genres
- **Encoding Detection**: Handles multiple file encodings automatically
- **Text Cleaning**: Removes problematic characters from book titles and author names
- **Comprehensive Genre Coverage**: Includes categories for Fiction, Non-Fiction, Science, and more

## 📦 Prerequisites

- Python 3.12.4
- Groq API Key
- Required Python libraries:
  - pandas
  - groq
  - python-dotenv

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/SOBANEJAZ/Goodreads-books-Genre-identifier-AI.git
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your Groq API key:
```bash
export GROQ_API_KEY='your_groq_api_key_here'
```

## 💡 Usage

1. Prepare your input CSV with columns: 'Title' and 'Author'
2. Run the script:
```bash
python main.py
```
3. Find your categorized books in `categorized_books.csv`

## 🎯 Categorization Scope

The tool categorizes books into rich, nuanced genres:
- Fiction (Classics, Sci-Fi, Fantasy, etc.)
- Non-Fiction (Psychology, Business, Biographies)
- Science & Knowledge
- And many more specialized categories

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
