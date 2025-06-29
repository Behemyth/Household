"""Fixtures and integration test configuration"""

import pytest
from tftest import TerraformTest


@pytest.fixture(scope='session')
def infrastructure():
    """Provides a tftest TerraformTest instance for integration tests."""
    tf = TerraformTest('tests/integration/terraform')
    tf.setup()
    tf.init()

    output = tf.output()
    yield output

    tf.destroy()
