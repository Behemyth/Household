"""Tests ansible inventory connections
"""
from typing import Any

import pytest


@pytest.mark.setup
class TestConnection:
    """Setup verification"""

    def test_connection(self, host: Any) -> None:
        """Verifies that each host can be connected to

        Args:
            host: The Testinfra host
        """
        assert host.user.exists

    def test_internet(self, host: Any) -> None:
        """Verifies that each host can access the outside world

        Args:
            host: The Testinfra host
        """

        google = host.addr("google.com")

        assert google.is_resolvable
        assert google.is_reachable
