import pytest
from retrying import retry


@pytest.fixture()
def AnsibleDefaults(Ansible):
    return Ansible("include_vars", "defaults/main.yml")["ansible_facts"]


def test_airflow_user(User, Group, AnsibleDefaults):
    user = User(AnsibleDefaults["airflow_user"])
    group = Group(AnsibleDefaults["airflow_group"])

    assert user.exists
    assert group.exists
    assert user.group == AnsibleDefaults["airflow_group"]


def test_airflow_version(PipPackage, AnsibleDefaults):
    expected_version = AnsibleDefaults["airflow_version"]
    installed_version = PipPackage.get_packages()["apache-airflow"]["version"]

    assert installed_version == expected_version


@retry(stop_max_delay=5000)
def test_airflow_services(Service, AnsibleDefaults):
    airflow_services = AnsibleDefaults["airflow_services"]

    for airflow_service in airflow_services:
        if airflow_services[airflow_service]["enabled"]:
            assert Service(airflow_service).is_enabled
            assert Service(airflow_service).is_running
