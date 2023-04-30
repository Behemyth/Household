"""Tests ansible inventory connections
"""

import pytest
import testinfra


@pytest.mark.setup
class TestConnection:
    """Setup verification"""

    def test_mini_behemyth(self) -> None:
        """Verifies that mini-behemyth is setup for subnet connections"""

        host = testinfra.get_host("ansible://mini-behemyth")

        # Empty user gets the current user, 'ansible_user'
        username = host.user().name
        assert username == "asher"
