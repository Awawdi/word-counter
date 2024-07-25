import re


def count_word_occurrences(sentences, words):
    word_count = {}

    # Initialize the count dictionary with 0 for each word
    for word in words:
        word_count[word] = 0

    # Count occurrences of each word in all sentences
    for sentence in sentences:
        # Use regular expressions to replace non-alphanumeric characters except underscores with spaces
        cleaned_sentence = re.sub(r'[^a-zA-Z0-9_]', ' ', sentence)
        sentence_words = cleaned_sentence.split()
        for word in words:
            word_count[word] += sentence_words.count(word)

    return word_count


def main():
    # Read number of sentences
    n = int(input())
    sentences = []

    # Read each sentence
    for _ in range(n):
        sentence = input()
        sentences.append(sentence)

    # Read number of words to count
    t = int(input())
    words = []

    # Read each word
    for _ in range(t):
        word = input()
        words.append(word)

    # Get the word occurrence counts
    result = count_word_occurrences(sentences, words)

    # Print the results
    for word in words:
        print(result[word])


if __name__ == "__main__":
    main()
