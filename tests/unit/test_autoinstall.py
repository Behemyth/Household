"""Unit tests for the autoinstall playbook."""

import os

import pytest

PLAYBOOK_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../playbooks/autoinstall.yml'))


def test_autoinstall_playbook_exists():
    """Test that the autoinstall playbook file exists."""
    assert os.path.isfile(PLAYBOOK_PATH), f'Playbook not found: {PLAYBOOK_PATH}'


@pytest.mark.ansible
def test_autoinstall_playbook_syntax(ansible_adhoc):
    """Test that the autoinstall playbook passes ansible syntax check using ansible.builtin.command."""
    result = ansible_adhoc().localhost.shell(f'ansible-playbook --syntax-check {PLAYBOOK_PATH}')

    localhost_result = result['localhost']
    assert localhost_result['rc'] == 0, f'Syntax check failed: {localhost_result["stderr"]}'
