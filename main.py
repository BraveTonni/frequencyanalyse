from pathlib import Path

from analyzer import LetterAnalyzer
from keyboard import KeyboardBuilder
from storage import LocalFileStorage

TEXT_FILE = Path(__file__).parent / "text.txt"


def main() -> None:
    storage = LocalFileStorage(TEXT_FILE)
    text = storage.extract_data()

    analyzer = LetterAnalyzer()
    freq = analyzer.count_letters(text)
    total = sum(freq.values())

    if not freq:
        print("В тексте не найдено кириллических букв.")
        return

    print("Частота букв:")
    for letter, count in analyzer.sort_result(freq):
        print(f"{letter}: {count} ({count / total:.2%})")

    print()
    print("Раскладка:")
    builder = KeyboardBuilder()
    builder.print(freq)


if __name__ == "__main__":
    main()
