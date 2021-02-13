import logging
import subprocess
from dataclasses import dataclass

from dependencies import Injector, value

logger = logging.getLogger(__name__)


@dataclass
class Isort:
    """Isort sorts imports."""

    project_name: str

    def __call__(self):
        """Apply isort to current project."""
        subprocess.run(['isort', self.project_name])


@dataclass
class FlakeHell:
    """Find flake8 errors."""

    project_name: str

    def __call__(self) -> bool:
        """Call flakehell for this project."""
        process = subprocess.run([
            'flakehell',
            'lint',
            self.project_name,
            'tests',
        ])
        return process.returncode == 0


@dataclass
class Lint:
    """Run all available linters."""

    flakehell: FlakeHell

    def __call__(self) -> None:
        """Call all known linters."""
        self.flakehell()  # FIXME: hardcode


class Make(Injector):
    """Build and service this project."""

    # Machine readable project name (and its main directory)
    project_name = 'platonic'

    isort = Isort
    flakehell = FlakeHell

    # noinspection PyMethodParameters
    @value
    def format(isort: Isort) -> None:  # noqa: N805
        """Auto format project code."""
        isort()


if __name__ == '__main__':
    logger.info(Make.format)
