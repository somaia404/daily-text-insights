# Daily Text Insights

A small Python project for extracting simple insights from text files.

Currently supports:
- Word count
- Most common words

This project is intentionally minimal and will be expanded over time.

## How to run

1. Make sure you have Python 3 installed.
2. Place your text inside `sample.txt`.
3. Run the script from the project directory:

```bash
python text_insights.py

---

## 2️⃣ Add example output (README update)

Still editing `README.md`, add **below the run section**:

```markdown
## Example output

```text
Total words: 14
Most common words:
is: 2
data: 1
science: 1
not: 1
magic.: 1


This is subtle but powerful. Reviewers love seeing expected output.

---

## 3️⃣ One NLP upgrade: basic stopword removal + tokenisation

Now we gently level it up without turning it into a monster.

### Replace `text_insights.py` with this version

Edit the file and **replace everything** with:

```python
from collections import Counter
import string

STOPWORDS = {
    "the", "is", "and", "to", "of", "in", "it", "that", "this"
}

def tokenize(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    return [word for word in words if word not in STOPWORDS]

def analyze_text(filepath):
    with open(filepath, "r") as file:
        text = file.read()

    tokens = tokenize(text)
    word_count = len(tokens)
    common_words = Counter(tokens).most_common(5)

    return word_count, common_words


if __name__ == "__main__":
    count, common = analyze_text("sample.txt")
    print(f"Total words (after cleaning): {count}")
    print("Most common words:")
    for word, freq in common:
        print(f"{word}: {freq}")
## Text processing

The analysis includes simple preprocessing steps:
- Lowercasing
- Punctuation removal
- Basic stopword filtering
- Token-based word frequency analysis

