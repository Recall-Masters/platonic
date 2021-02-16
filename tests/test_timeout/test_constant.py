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
        assert timer.remaining_seconds < 121

    assert timer.remaining_seconds > 0
