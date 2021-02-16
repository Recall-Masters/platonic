import time
from datetime import timedelta

from platonic.timeout import ConstantTimeout, ConstantTimer


def test_constant_timeout():
    delta = timedelta(minutes=2)
    timeout = ConstantTimeout(period=delta)

    timer: ConstantTimer
    with timeout.timer() as timer:
        assert not timer.is_expired
        assert timer.remaining_seconds < 120

        time.sleep(1)
        assert timer.remaining_seconds < 119

    assert timer.remaining_seconds > 0     # noqa: WPS441
    assert timer.remaining_seconds < 119   # noqa: WPS441
    assert timer.elapsed_seconds < 2
