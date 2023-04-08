"""Tests ansible inventory connections
"""

from typing import Any

import pytest


class TestConnection:
    """Verifies connections"""

    def test_require_ansible(self, host: Any) -> None:
        """Tests host connection

        Args:
            host: The Testinfra host
        """

        with pytest.raises(RuntimeError):
            host.ansible("setup")
