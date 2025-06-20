"""Tests for the docker setup."""

import docker
import pytest
from docker.errors import DockerException


def test_docker() -> None:
    """Test that Docker is installed and running."""
    try:
        client = docker.from_env()
        client.ping()  # type: ignore
    except DockerException as e:
        pytest.fail(f'Docker is not running or not accessible: {e}')
