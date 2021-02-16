import math
from contextlib import contextmanager
from typing import Iterable

from platonic.timeout.base import BaseTimeout, BaseTimer


class InfiniteTimer(BaseTimer):
    @property
    def remaining_seconds(self) -> float:
        """The timeout is eternal."""
        return math.inf


class InfiniteTimeout(BaseTimeout):
    @contextmanager
    def timer(self) -> Iterable[InfiniteTimer]:
        """Always yield infinite timeout."""
        yield InfiniteTimer()
