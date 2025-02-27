def sorted_list(char_counts):
    char_list = [{char: count} for char, count in char_counts.items() if char.isalpha()]
    char_list.sort(key=lambda d: list(d.values())[0], reverse=True)
    return char_list

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    char_counts = {}

    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts  # Returns the dictionary
