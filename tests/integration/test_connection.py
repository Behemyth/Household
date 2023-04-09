"""Tests ansible inventory connections
"""

from testinfra.host import Host


class TestConnection:
    """Setup verification"""

    def test_connection(self, host: Host) -> None:
        """Verifies that each host can be connected to

        Args:
            host: The Testinfra host
        """
        assert host.user.exists

    def test_internet(self, host: Host) -> None:
        """Verifies that each host can access the outside world

        Args:
            host: The Testinfra host
        """

        google = host.addr("google.com")

        assert google.is_resolvable
        assert google.is_reachable
