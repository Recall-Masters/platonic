from abc import abstractmethod
from contextlib import contextmanager
from typing import Iterator


class BaseTimer:
    """Timer."""

    @property
    @abstractmethod
    def remaining_seconds(self) -> float:
        """Remaining number of seconds."""


class BaseTimeout:
    """Abstract timeout class."""

    @contextmanager
    @abstractmethod
    def timer(self) -> Iterator[BaseTimer]:
        """Context manager returning a timer instance."""
