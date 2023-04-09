"""Tests ansible inventory connections
"""

from typing import Any


class TestConnection:
    """Setup verification"""

    def test_require_ansible(self, host: Any) -> None:
        """Verifies that ansible is being used as the Testinfra backend

        Args:
            host: The Testinfra host
        """

        host.ansible("--version")

    def test_connection(self, host: Any) -> None:
        """Verifies that all hosts can be reached

        Args:
            host: The Testinfra host
        """

        host.ansible("all -i inventory -m ping")
