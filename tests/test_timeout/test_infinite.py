import math

from platonic.timeout.infinite import InfiniteTimeout


def test_infinite_timeout():
    """Test infinite timeout and its timer."""
    timeout = InfiniteTimeout()

    with timeout.timer() as timer:
        assert timer.remaining_seconds == math.inf
        assert timer.remaining_seconds > 10
