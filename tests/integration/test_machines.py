"Test the vm machines mimicking the home setup"

from pytest_terraform import terraform


@terraform('integration/terraform', scope='session')
def test_machines(terraform_outputs) -> None:
    """Terraform fixture"""
    assert terraform_outputs is not None
