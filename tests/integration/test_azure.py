"Test the azure setup mimicking the home setup"

WORKER_IPS_COUNT = 4


def test_terraform_outputs(infrastructure):
    """Check that Terraform outputs manager and worker IPs."""
    assert 'manager_ip' in infrastructure, 'manager_ip output missing'
    assert 'worker_ips' in infrastructure, 'worker_ips output missing'
    assert isinstance(infrastructure['worker_ips']['value'], list)
    assert len(infrastructure['worker_ips']['value']) == WORKER_IPS_COUNT
