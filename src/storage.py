from abc import ABC, abstractmethod
from pathlib import Path


class FileStorage(ABC):
    @abstractmethod
    def _read(self) -> str:
        pass

    @abstractmethod
    def write(self, content: str) -> None:
        pass


class LocalFileStorage(FileStorage):
    def __init__(self, path: Path):
        self._path = path

    def _read(self) -> str:
        return self._path.read_text(encoding="utf-8", errors="ignore")

    def write(self, content: str) -> None:
        self._path.write_text(content, encoding="utf-8")

    def extract_data(self) -> str:
        return self._read()
