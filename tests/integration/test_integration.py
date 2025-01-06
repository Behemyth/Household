"""Tests for molecule scenarios."""

from pytest_ansible.molecule import MoleculeScenario


def test_integration(molecule_scenario: MoleculeScenario) -> None:
    """Run molecule for each scenario.

    molecule_scenario: The parameterized molecule scenario object.
    """
    proc = molecule_scenario.test()
    assert proc.returncode == 0
