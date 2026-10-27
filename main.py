from pathlib import Path

from frequency import count_letters, print_frequencies
from layout import KeyboardLayout

TEXT_FILE = Path(__file__).parent / "text.txt"


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
    KeyboardLayout.from_frequencies(freq).print()


if __name__ == "__main__":
    main()
