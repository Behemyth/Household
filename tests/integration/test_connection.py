"""Tests ansible inventory connections
"""

from typing import Any


class TestConnection:
    """Verifies connections"""

    def test_connections(self, host: Any) -> None:
        """Tests host connection

        Args:
            host: The Testinfra host
        """
