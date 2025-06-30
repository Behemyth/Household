"""Fixtures"""

import os
import subprocess

import pytest


@pytest.fixture(scope='session')
def infrastructure():
    """Spins up the Vagrant cluster before tests and destroys it after all tests complete."""
    vagrant_dir = os.path.join(os.path.dirname(__file__), 'vagrant')
    # Start the Vagrant environment
    subprocess.run(['vagrant', 'up'], check=True, cwd=vagrant_dir)
    yield
    subprocess.run(['vagrant', 'destroy', '-f'], check=True, cwd=vagrant_dir)
