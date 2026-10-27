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


@dataclass
class KeyboardLayout:
    fingers: Fingers

    @classmethod
    def from_frequencies(cls, freq: Counter) -> "KeyboardLayout":
        letters = [letter for letter, _ in freq.most_common()]

        return cls(
            fingers=Fingers(
                index=Finger("Указательный", letters[:12]),
                middle=Finger("Средний", letters[12:18]),
                ring=Finger("Безымянный", letters[18:24]),
                little=Finger("Мизинец", letters[24:33]),
            )
        )

    def print(self) -> None:
        for finger in self.fingers:
            finger.print()
