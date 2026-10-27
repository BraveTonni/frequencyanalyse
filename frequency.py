from collections import Counter


def count_letters(text: str) -> Counter:
    return Counter(ch for ch in text.lower() if "а" <= ch <= "я" or ch == "ё")


def print_frequencies(freq: Counter, total: int) -> None:
    print("Частота букв:")

    for letter, count in freq.most_common():
        print(f"{letter}: {count} ({count / total:.2%})")
