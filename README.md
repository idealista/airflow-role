![Logo](https://raw.githubusercontent.com/idealista/airflow-role/master/logo.gif)

[![Build Status](https://travis-ci.org/idealista/airflow-role.png)](https://travis-ci.org/idealista/airflow-role)

# Apache Airflow Ansible role

This ansible role installs a Apache Airflow server in a debian environment.

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

These instructions will get you a copy of the role for your ansible playbook. Once launched, it will install a [Apache Airflow](https://airflow.incubator.apache.org/) server in a Debian system.

### Prerequisities

Ansible 2.2.1.0 version installed.
Inventory destination should be a Debian environment.

For testing purposes, [Molecule](https://molecule.readthedocs.io/) with [Vagrant](https://www.vagrantup.com/) as driver (with [landrush](https://github.com/vagrant-landrush/landrush) plugin) and [VirtualBox](https://www.virtualbox.org/) as provider.

### Installing

Create or add to your roles dependency file (e.g requirements.yml) from GitHub:

```
- src: http://github.com/idealista/airflow-role.git
  scm: git
  version: 1.0.0
  name: airflow
```

or using [Ansible Galaxy](https://galaxy.ansible.com/idealista/airflow-role/) as origin if you prefer:

```
- src: idealista.airflow-role
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

## Testing

```
molecule test --platform=Debian9
```

See molecule.yml to check possible testing platforms.

## Built With

![Ansible](https://img.shields.io/badge/ansible-2.2.1.0-green.svg)

## Versioning

For the versions available, see the [tags on this repository](https://github.com/idealista/airflow-role/tags).

Additionaly you can see what change in each version in the [CHANGELOG.md](CHANGELOG.md) file.

## Authors

* **Idealista** - *Work with* - [idealista](https://github.com/idealista)

See also the list of [contributors](https://github.com/idealista/airflow-role/contributors) who participated in this project.

## License

![Apache 2.0 Licence](https://img.shields.io/hexpm/l/plug.svg)

This project is licensed under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license - see the [LICENSE.txt](LICENSE.txt) file for details.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.
