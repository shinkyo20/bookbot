def main():
    with open('/home/shinkyo/workspace/github.com/shinkyo20/bookbot/books/frankenstein.txt') as f:
        file_contents = f.read()
    text = file_contents.lower()
    letter_counts = lettercount(text)
    word_count = len(text.split())
    
    items = list(letter_counts.items())
    items.sort(key=lambda item: item[1], reverse=True)

    print(f"--- Begin report ---")
    print(f"{word_count} words found in the document")
    for letter, count in items:
        print(f"The '{letter}' character was found {count} times")
    print(f"--- End report ---")

def lettercount(text):
    counts = {}
    for char in text:
        if char.isalpha():
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
    return counts

if __name__ == "__main__":
    main()