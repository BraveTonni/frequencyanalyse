from collections import Counter
from pathlib import Path

TEXT_FILE = Path(__file__).parent / "text.txt"


class KeyboardLayout:
    def __init__(self, index_finger: list, middle_finger: list, ring_finger: list, little_finger: list):
        self.fingers = {
            "index": index_finger,
            "middle":  middle_finger,
            "ring": ring_finger,
            "little": little_finger
        }

    def print(self):
        names = {
            "index": "Указательный",
            "middle": "Средний",
            "ring": "Безымянный",
            "little": "Мизинец"
        }
        for finger, letters in self.fingers.items():
            print(f"{names[finger]} ({len(letters)}): {', '.join(letters)}")


def count_letters(text: str) -> Counter:
    return Counter(ch for ch in text.lower() if "а" <= ch <= "я" or ch == "ё")


def print_frequencies(freq: Counter, total: int) -> None:
    print("Частота букв:")
    
    for letter, count in freq.most_common():
        print(f"{letter}: {count} ({count / total:.2%})")


def build_layout(freq: Counter) -> KeyboardLayout:
    letters = [letter for letter, _ in freq.most_common()]

    return KeyboardLayout(
        index_finger=letters[:12],
        middle_finger=letters[12:18],
        ring_finger=letters[18:24],
        little_finger=letters[24:33]
    )


def main() -> None:
    text = TEXT_FILE.read_text(encoding="utf-8", errors="ignore")
    freq = count_letters(text)
    total = sum(freq.values())

    if not freq:
        print("В тексте не найдено кириллических букв.")
        return

    print_frequencies(freq, total)
    print()
    print("Раскладка:")
    build_layout(freq).print()


if __name__ == "__main__":
    main()

