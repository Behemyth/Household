# type: ignore

"""Tests ansible inventory connections. Type hints turned off because of testinfra"""

import pytest
from testinfra.host import Host


@pytest.mark.setup
@pytest.mark.parametrize(
    'host_name',
    [
        ('ansible://mini-behemyth'),
        ('ansible://mini-wumpus'),
        ('ansible://mini-mush'),
        ('ansible://mini-sota'),
        ('ansible://mini-mouse'),
    ],
)
class TestConnection:
    """Setup verification"""

    @staticmethod
    def test_mini_behemyth(
        host: Host,
        host_name: str,
    ) -> None:
        """Verifies that mini-behemyth is setup for subnet connections"""
        external_host = host.get_host(host_name)

        # Empty user gets the current user, 'ansible_user'
        username = external_host.user.name
        assert username == 'synodic'

        google = external_host.addr('google.com')
        assert google.is_resolvable
        assert google.is_reachable
