#! /usr/bin/env python3
from urllib.request import urlopen
import sys


def fetch_url(url):
    """Fetch a list of words from a URL.

    Args:
        url: The URL of a UTF-8 text document.

    Returns:
        A list of strings containg the words form the document.
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_item(story_words):
    for item in story_words:
        print(item)


def main(url):
    words = fetch_url(url)
    print_item(words)


if __name__ == '__main__':
    main(sys.argv[1])

