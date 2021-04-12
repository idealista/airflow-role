# Apache Airflow Ansible role [![Build Status](https://travis-ci.org/idealista/airflow-role.png)](https://travis-ci.org/idealista/airflow-role)

![Logo](https://raw.githubusercontent.com/idealista/airflow-role/master/logo.gif)

This ansible role installs a Apache Airflow server in a Debian/Ubuntu environment.

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites-ballot_box_with_check)
  - [Installing](#Installing-inbox_tray )
- [Usage](#usage-runner)
- [Testing](#testing-test_tube)
- [Built With](#built-with-building_construction)
- [Versioning](#versioning-card_file_box)
- [Authors](#authors-superhero)
- [License](#license-spiral_notepad)
- [Contributing](#contributing-construction_worker)

## Getting Started

These instructions will get you a copy of the role for your ansible playbook. Once launched, it will install [Apache Airflow](https://airflow.apache.org/) in a Debian or Ubuntu system.

### Prerequisites :ballot_box_with_check:

Ansible 2.9.9 version installed.
Inventory destination should be a Debian (preferable Debian 10 Buster ) or Ubuntu environment.

ℹ️ This role should work with older versions of Debian but you need to know that due to Airflow minimum requirements you should check that 🐍 Python 3.6 (or higher) is installed before (👉 See: [Airflow prerequisites](https://airflow.apache.org/docs/apache-airflow/stable/installation.html#prerequisites)).

ℹ️ By default this role use the predefined installation of Python that comes with the distro.

For testing purposes, [Molecule](https://molecule.readthedocs.io/) with [Docker](https://www.docker.com/) as driver.

### Installing :inbox_tray:

Create or add to your roles dependency file (e.g requirements.yml) from GitHub:

```yml
- src: http://github.com/idealista/airflow-role.git
  scm: git
  version: 2.0.0
  name: airflow
```

or using [Ansible Galaxy](https://galaxy.ansible.com/idealista/airflow-role/) as origin if you prefer:

```yml
- src: idealista.airflow-role
  version: 2.0.0
  name: airflow
```

Install the role with ansible-galaxy command:

```shell
ansible-galaxy install -p roles -r requirements.yml -f
```

Use in a playbook:

```yml
---
- hosts: someserver
  roles:
    - { role: airflow }
```

## Usage :runner:

Look to the defaults properties files to see the possible configuration properties, take a look for them:

- [`main.yml`](./defaults/main/main.yml) for airflow general purpose.
- [`airflow-cfg.yml`](./defaults/main/airflow-cfg.yml) for all the related airflow.cfg config parameters.
- [`webserver-config-py.yml`](./defaults/main/webserver-config-py.yml) for all the related webserver_config.py config parameters.

👉 Don't forget :

- 🦸 To set your Admin user.
- 🔑 To set Fernet key.
- 🔑 To set webserver secret key.
- 📝 To set your AIRFLOW_HOME and AIRFLOW_CONFIG at your own discretion.
- 📝 To set your installation and config skelton paths at your own discretion.
  - 👉 See `airflow_skeleton_paths` in [`main.yml`](./defaults/main/main.yml)
- 🐍 Python and pip version.
- 📦 [Extra packages](#package-Extra-packages) if you need additional operators, hooks, sensors...
- 📦 [Required Python packages](#package-Required-Python-packages) with version specific like SQLAlchemy for example (to avoid known Airflow bugs❗️) like below or because are necessary
- ⚠️ With Airflow v1.10.0, PyPi package `pyasn1` v0.4.4 is needed. See examples below

### :package: Required Python packages

[`airflow_required_python_packages`](./defaults/main/main.yml) should be a list following this format:

```yml
airflow_required_python_packages:
  - { name: SQLAlchemy, version: 1.3.23 }
  - { name: psycopg2 }
  - {name: pyasn1, version: 0.4.4}
```

### :package: Extra packages

[`airflow_extra_packages`](./defaults/main/main.yml) should be a list following this format:

```yml
airflow_extra_packages:
  - apache.atlas
  - celery
  - ssh
```

👉 For more info about this extra packages see: [Airflow extra packages](https://airflow.apache.org/docs/apache-airflow/stable/extra-packages-ref.html)

## Testing :test_tube:

```shell
pipenv install -r test-requirements.txt --python 3.7
pipenv run molecule test
```

## Built With :building_construction:

![Ansible](https://img.shields.io/badge/ansible-2.9.9-green.svg)

## Versioning :card_file_box:

For the versions available, see the [tags on this repository](https://github.com/idealista/airflow-role/tags).

Additionally you can see what change in each version in the [CHANGELOG.md](CHANGELOG.md) file.

## Authors :superhero:

- **Idealista** - *Work with* - [idealista](https://github.com/idealista)

See also the list of [contributors](https://github.com/idealista/airflow-role/contributors) who participated in this project.

## License :spiral_notepad:

![Apache 2.0 License](https://img.shields.io/hexpm/l/plug.svg)

This project is licensed under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license - see the [LICENSE](LICENSE) file for details.

## Contributing :construction_worker:

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.
