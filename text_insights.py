from collections import Counter

def analyze_text(filepath):
    with open(filepath, "r") as file:
        text = file.read().lower()

    words = text.split()
    word_count = len(words)
    common_words = Counter(words).most_common(5)

    return word_count, common_words


if __name__ == "__main__":
    count, common = analyze_text("sample.txt")
    print(f"Total words: {count}")
    print("Most common words:")
    for word, freq in common:
        print(f"{word}: {freq}")
