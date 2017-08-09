# Change Log
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/) and [Keep a changelog](https://github.com/olivierlacan/keep-a-changelog).

## [Unreleased](https://github.com/idealista/airflow-role/tree/develop)

## [1.3.1](https://github.com/idealista/airflow-role/tree/1.3.1)
[Full Changelog](https://github.com/idealista/airflow-role/compare/1.3.0...1.3.1)
### Fixed
- *Deleted DAGs automatic managent: better do it with CI tools* @jnogol
- *Deleted port bindings in molecule.yml: they weren't necessary* @jnogol
- *Better and more understandable format for dags_dependencies variable* @jnogol

## [1.3.0](https://github.com/idealista/airflow-role/tree/1.3.0)
[Full Changelog](https://github.com/idealista/airflow-role/compare/1.2.0...1.3.0)
### Added
- *Testinfra tests in Travis CI* @jnogol
- *DAGs and plugins automatic management via repositories and cron job* @jnogol
- *Docker environment in Molecule* @jnogol

### Fixed
- *Test if service is running in test_ansible.py now working* @jnogol

## [1.2.0](https://github.com/idealista/airflow-role/tree/1.2.0)
[Full Changelog](https://github.com/idealista/airflow-role/compare/1.1.0...1.2.0)
### Added
- *Travis CI integration added* @jnogol

### Fixed
- *Authentication via LDAP now working* @jnogol
- *Tiny bugs in tasks/install.yml fixed* @jnogol

## [1.1.0](https://github.com/idealista/airflow-role/tree/1.1.0)
[Full Changelog](https://github.com/idealista/airflow-role/compare/1.0.0...1.1.0)
### Added
- *Added Celery Worker optional installation* @jnogol
- *Added Celery Flower service configuration* @jnogol

## [1.0.0](https://github.com/idealista/airflow-role/tree/1.0.0)
### Added
- *First release*
