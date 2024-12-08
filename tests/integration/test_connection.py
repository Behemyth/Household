# type: ignore

"""Tests ansible inventory connections. Type hints turned off because of testinfra"""

import pytest
from testinfra.host import Host


@pytest.mark.setup
class TestConnection:
    """Setup verification"""

    @staticmethod
    def test_mini_behemyth(host: Host) -> None:
        """Verifies that mini-behemyth is setup for subnet connections"""
        external_host = host.get_host('ansible://mini-behemyth')

        # Empty user gets the current user, 'ansible_user'
        username = external_host.user().name
        assert username == 'asher'

        google = external_host.addr('google.com')
        assert google.is_resolvable
        assert google.is_reachable

    @staticmethod
    def test_mini_wumpus(host: Host) -> None:
        """Verifies that mini-wumpus is setup via jumphost"""
        external_host = host.get_host('ansible://mini-wumpus')

        # Empty user gets the current user, 'ansible_user'
        username = external_host.user.name
        assert username == 'synodic'

        google = external_host.addr('google.com')
        assert google.is_resolvable
        assert google.is_reachable

    @staticmethod
    def test_mini_mush(host: Host) -> None:
        """Verifies that mini-mush is setup via jumphost"""
        external_host = host.get_host('ansible://mini-mush')

        # Empty user gets the current user, 'ansible_user'
        username = external_host.user.name
        assert username == 'synodic'

        google = external_host.addr('google.com')
        assert google.is_resolvable
        assert google.is_reachable

    @staticmethod
    def test_mini_sota(host: Host) -> None:
        """Verifies that mini-sota is setup via jumphost"""
        external_host = host.get_host('ansible://mini-sota')

        # Empty user gets the current user, 'ansible_user'
        username = external_host.user.name
        assert username == 'synodic'

        google = external_host.addr('google.com')
        assert google.is_resolvable
        assert google.is_reachable

    @staticmethod
    def test_mini_mouse(host: Host) -> None:
        """Verifies that mini-mouse is setup via jumphost"""
        external_host = host.get_host('ansible://mini-mouse')

        # Empty user gets the current user, 'ansible_user'
        username = external_host.user.name
        assert username == 'synodic'

        google = external_host.addr('google.com')
        assert google.is_resolvable
        assert google.is_reachable
