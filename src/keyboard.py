from abc import ABC, abstractmethod
from collections import Counter
from collections.abc import Iterator
from dataclasses import dataclass


@dataclass
class Finger:
    name: str
    letters: list[str]

    @property
    def count(self) -> int:
        return len(self.letters)

    def print(self) -> None:
        print(f"{self.name} ({self.count}): {', '.join(self.letters)}")


@dataclass
class Fingers:
    index: Finger
    middle: Finger
    ring: Finger
    little: Finger

    def __iter__(self) -> Iterator[Finger]:
        return iter((self.index, self.middle, self.ring, self.little))


class KeyboardLayoutProvider(ABC):
    @abstractmethod
    def arrange_letters(self, freq: Counter) -> list[str]:
        pass


class KeyboardBuilder(KeyboardLayoutProvider):
    def arrange_letters(self, freq: Counter) -> list[str]:
        return [letter for letter, _ in freq.most_common()]

    def distribute_fingers(self, letters: list[str]) -> Fingers:
        return Fingers(
            index=Finger("Указательный", letters[:12]),
            middle=Finger("Средний", letters[12:18]),
            ring=Finger("Безымянный", letters[18:24]),
            little=Finger("Мизинец", letters[24:33]),
        )

    def build_layout(self, freq: Counter) -> Fingers:
        letters = self.arrange_letters(freq)
        return self.distribute_fingers(letters)

    def print(self, freq: Counter) -> None:
        fingers = self.build_layout(freq)
        for finger in fingers:
            finger.print()

    def save_to_file(self, freq: Counter) -> str:
        fingers = self.build_layout(freq)
        lines = []

        for finger in fingers:
            lines.append(f"{finger.name} ({finger.count}): {', '.join(finger.letters)}")

        return "\n".join(lines)

    def build(self, freq: Counter) -> None:
        self.print(freq)
        self.save_to_file(freq)
