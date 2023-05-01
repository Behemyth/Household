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

        google = host.addr("google.com")
        assert google.is_resolvable
        assert google.is_reachable

    def test_mini_wumpus(self) -> None:
        """Verifies that mini-wumpus is setup via jumphost"""

        host = testinfra.get_host("ansible://mini-wumpus")

        # Empty user gets the current user, 'ansible_user'
        username = host.user().name
        assert username == "synodic"

        google = host.addr("google.com")
        assert google.is_resolvable
        assert google.is_reachable

    def test_mini_mush(self) -> None:
        """Verifies that mini-mush is setup via jumphost"""

        host = testinfra.get_host("ansible://mini-mush")

        # Empty user gets the current user, 'ansible_user'
        username = host.user().name
        assert username == "synodic"

        google = host.addr("google.com")
        assert google.is_resolvable
        assert google.is_reachable

    def test_mini_sota(self) -> None:
        """Verifies that mini-sota is setup via jumphost"""

        host = testinfra.get_host("ansible://mini-sota")

        # Empty user gets the current user, 'ansible_user'
        username = host.user().name
        assert username == "synodic"

        google = host.addr("google.com")
        assert google.is_resolvable
        assert google.is_reachable

    def test_mini_mouse(self) -> None:
        """Verifies that mini-mouse is setup via jumphost"""

        host = testinfra.get_host("ansible://mini-mouse")

        # Empty user gets the current user, 'ansible_user'
        username = host.user().name
        assert username == "synodic"

        google = host.addr("google.com")
        assert google.is_resolvable
        assert google.is_reachable
