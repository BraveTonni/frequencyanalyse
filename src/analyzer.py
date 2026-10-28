from abc import ABC, abstractmethod
from collections import Counter


class TextAnalyzer(ABC):
    @abstractmethod
    def count_letters(self, text: str) -> Counter:
        pass

    @abstractmethod
    def sort_result(self, freq: Counter) -> list[tuple[str, int]]:
        pass

    @abstractmethod
    def get_analytics_data(self, text: str) -> list[tuple[str, int]]:
        pass


class LetterAnalyzer(TextAnalyzer):
    def count_letters(self, text: str) -> Counter:
        return Counter(ch for ch in text.lower() if "а" <= ch <= "я" or ch == "ё")

    def sort_result(self, freq: Counter) -> list[tuple[str, int]]:
        return freq.most_common()

    def _extract_analytics(self, text: str) -> list[tuple[str, int]]:
        return self.sort_result(self.count_letters(text))

    def get_analytics_data(self, text: str) -> list[tuple[str, int]]:
        return self._extract_analytics(text)
