import sys
from stats import count_words, count_characters, sorted_list

def get_book_text(filepath):
    """Reads the book file and returns its text content."""
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def main():
    # Ensure a book path is provided as an argument
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  # Exit with error status 1

    # Get book path from command-line argument
    book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    book_text = get_book_text(book_path)

    # Count words
    num_words = count_words(book_text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    # Count and sort character frequencies
    char_counts = count_characters(book_text)
    sorted_chars = sorted_list(char_counts)

    print("--------- Character Count -------")
    for entry in sorted_chars:
        for char, count in entry.items():
            if char.isalpha():  # Only print alphabetic characters
                print(f"{char}: {count}")

    print("============= END ===============")

if __name__ == "__main__":
    main()
