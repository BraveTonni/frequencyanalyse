from collections import Counter
from pathlib import Path

TEXT_FILE = Path(__file__).parent / "text.txt"

def count_letters(text: str) -> Counter:
    return Counter(ch for ch in text.lower() if "а" <= ch <= "я" or ch == "ё")


def main() -> None:
    text = TEXT_FILE.read_text(encoding="utf-8", errors="ignore")
    freq = count_letters(text)
    total = sum(freq.values())

    if not freq:
        print("В тексте не найдено кириллических букв.")
        return

    print(freq, total)


if __name__ == "__main__":
    main()
