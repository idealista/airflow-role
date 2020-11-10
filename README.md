![Logo](https://raw.githubusercontent.com/idealista/airflow-role/master/logo.gif)

[![Build Status](https://travis-ci.org/idealista/airflow-role.png)](https://travis-ci.org/idealista/airflow-role)

# Apache Airflow Ansible role

This ansible role installs a Apache Airflow server in a Debian/Ubuntu environment.

- [Getting Started](#getting-started)
	- [Prerequisities](#prerequisities)
	- [Installing](#installing)
- [Usage](#usage)
- [Testing](#testing)
- [Built With](#built-with)
- [Versioning](#versioning)
- [Authors](#authors)
- [License](#license)
- [Contributing](#contributing)

## Getting Started

These instructions will get you a copy of the role for your ansible playbook. Once launched, it will install a [Apache Airflow](https://airflow.apache.org/) server in a Debian or Ubuntu system.

### Prerequisities

Ansible 2.8.8 version installed.
Inventory destination should be a Debian or Ubuntu environment.

For testing purposes, [Molecule](https://molecule.readthedocs.io/) with [Docker](https://www.docker.com/) as driver.

### Installing

Create or add to your roles dependency file (e.g requirements.yml) from GitHub:

```
- src: http://github.com/idealista/airflow-role.git
  scm: git
  version: 1.7.3
  name: airflow
```

or using [Ansible Galaxy](https://galaxy.ansible.com/idealista/airflow-role/) as origin if you prefer:

```
- src: idealista.airflow-role
  version: 1.7.3
  name: airflow
```

Install the role with ansible-galaxy command:

```
ansible-galaxy install -p roles -r requirements.yml -f
```

Use in a playbook:

```
---
- hosts: someserver
  roles:
    - { role: airflow }
```

## Usage

Look to the defaults properties file to see the possible configuration properties.

Bear in mind that, starting with Airflow v1.10.0, PyPi package `pyasn1` v0.4.4 is needed. To install it:
``` yml
airflow_required_python_packages:
  - {name: pyasn1, version: 0.4.4}
```

`airflow_extra_packages` (available at: https://airflow.apache.org/installation.html#extra-packages) should be a list following this format:
``` yml
airflow_extra_packages:
  - celery
  - mysql
```
## Testing

```
pipenv install -r test-requirements.txt --python 3.8
pipenv run molecule test
```

## Built With

![Ansible](https://img.shields.io/badge/ansible-2.4.5.0-green.svg)

## Versioning

For the versions available, see the [tags on this repository](https://github.com/idealista/airflow-role/tags).

Additionaly you can see what change in each version in the [CHANGELOG.md](CHANGELOG.md) file.

## Authors

* **Idealista** - *Work with* - [idealista](https://github.com/idealista)

See also the list of [contributors](https://github.com/idealista/airflow-role/contributors) who participated in this project.

## License

![Apache 2.0 License](https://img.shields.io/hexpm/l/plug.svg)

This project is licensed under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license - see the [LICENSE](LICENSE) file for details.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.
