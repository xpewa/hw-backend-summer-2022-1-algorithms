from typing import Optional

import re

__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    """
    В переданном тексте вернуть слово имеющее наименьшую и наибольшую длину.
    Если такого слова нет - вернуть None
    """
    longest_word = ''
    shortest_word = ''
    p = re.compile(r'\S+')
    for word in p.findall(text):
        if len(word) > len(longest_word):
            longest_word = word
        if len(word) < len(shortest_word) or not shortest_word:
            shortest_word = word
    if not longest_word:
        longest_word = None
        shortest_word = None
    return (shortest_word, longest_word)
