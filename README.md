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

1.Clone the repository:

```bash
git clone https://github.com/SOBANEJAZ/Goodreads-books-Genre-identifier-AI.git
cd Goodreads-books-Genre-identifier-AI
```

2.Make Virtual Environment:

```bash
python -m venv myenv
source myenv/Scripts/activate
```

3.Install dependencies:

```bash
pip install -r requirements.txt
```

4.Rename .env.example to .env and insert the API key:

```bash
GROQ_API_KEY = "your-api-key"
```

## 💡 Usage

1.Export the Goodreads library from your Account.

2.Run the script:

```bash
python main.py
```

3.Find your categorized books in `categorized_books.csv`

## 🎯 Categorization Scope

📚 Books  
│  
├── 📖 Fiction  
│   ├── 🎭 Classics (Shakespeare, Dostoevsky, Orwell, Austen)  
│   ├── 🔮 Science Fiction (Asimov, Clarke, Bradbury, sci-fi)  
│   ├── 🏰 Fantasy (Tolkien, Sanderson, Martin, fantasy)  
│   ├── 🕵️ Mystery & Thriller (Agatha Christie, Dan Brown, thriller, mystery)  
│   ├── ❤️ Romance (Nicholas Sparks, romance)  
│   ├── 🧠 Philosophical Fiction (Kafka, Camus, Huxley, existential)  
│   ├── 🎭 Contemporary & Literary Fiction (Murakami, Sally Rooney)  
│  
├── 📚 Non-Fiction  
│   ├── 🧠 Psychology & Self-Help (Daniel Kahneman, Mark Manson, psychology, self-help)  
│   ├── 🚀 Business & Productivity (Cal Newport, Peter Thiel, business, productivity)  
│   ├── 🏆 Biographies & Memoirs (Steve Jobs, Michelle Obama, biography, memoir)  
│   ├── 🌍 History & Politics (Yuval Noah Harari, Churchill, history, politics)  
│   ├── 🎨 Philosophy & Thought (Nietzsche, Sartre, Plato, philosophy)  
│   ├── 💰 Finance & Investing (Benjamin Graham, Morgan Housel, finance, investing)  
│   ├── 📖 Writing & Creativity (Stephen King, Julia Cameron, writing, creativity)  
│  
├── 🔬 Science & Knowledge  
│   ├── 💻 Computer Science (AI, Programming, Algorithms, Computer Science)  
│   ├── 🌌 Astronomy & Cosmology (Stephen Hawking, Carl Sagan, cosmology, astronomy)  
│   ├── 🧬 Biology & Life Sciences (Richard Dawkins, E.O. Wilson, biology, evolution)  
│   ├── 🏗️ Engineering & Physics (Feynman, Maxwell, engineering, physics)  
│   ├── 🏥 Medicine & Neuroscience (Oliver Sacks, Robert Sapolsky, medicine, neuroscience)  
│   ├── 🤖 AI & Game Development (John Carmack, Ian Goodfellow, AI, game development)  
│   ├── 🏋️ Health & Fitness (David Goggins, Arnold Schwarzenegger, fitness, health)  
│   ├── 🧘 Religion & Spirituality (Eckhart Tolle, Dalai Lama, religion, spirituality)  

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
