# Change Log

All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/) and [Keep a changelog](https://github.com/olivierlacan/keep-a-changelog).

## [Unreleased](https://github.com/idealista/airflow-role/tree/develop)

## [3.0.1](https://github.com/idealista/airflow-role/tree/3.0.1)

[Full Changelog](https://github.com/idealista/airflow-role/compare/3.0.0...3.0.1)

### Fixed

- `base_log_folder` is fixed in default config due to wrong `log_folder` named var

## [3.0.0](https://github.com/idealista/airflow-role/tree/3.0.0)

[Full Changelog](https://github.com/idealista/airflow-role/compare/2.0.7...3.0.0)

### Updated

- Updated Python dependencies and Airflow packages.
- Improvements in the configuration of Airflow services.

### Fixed

- Minor bug fixes in installation and configuration tasks.
- Documentation improvements and updates to the `README.md`.

### Added

- Support for fully qualified collection names (FQCN) in Ansible modules.
- Added support for installing specific versions of `pip` and `virtualenv`.

### Changed

- Updated installation tasks to use FQCN instead of abbreviated modules.
- Improved configuration for `virtualenv` and `pip` to ensure compatibility with different Python versions.

## [2.0.7](https://github.com/idealista/airflow-role/tree/2.0.7)

[Full Changelog](https://github.com/idealista/airflow-role/compare/2.0.6...2.0.7)

### Fixed

- #114 The "-n" option might not be needed

## [2.0.6](https://github.com/idealista/airflow-role/tree/2.0.6)

[Full Changelog](https://github.com/idealista/airflow-role/compare/2.0.5...2.0.6)

### Fixed

- :hammer_and_wrench: Allow intalling only some services
- :hammer_and_wrench: Updating travis environment

### Changed

- :arrows_clockwise: Moving copy tasks of services to service.yml

## [2.0.5](https://github.com/idealista/airflow-role/tree/2.0.5)

[Full Changelog](https://github.com/idealista/airflow-role/compare/2.0.4...2.0.5)

### Fixed

- :hammer_and_wrench: change psycopg2 to use the binary option to fix broken build
- :hammer_and_wrench: Fix typos

### Added

- :heavy_plus_sign: Add anisble-lint config file

### Changed

- :arrows_clockwise: Update Readme

## [2.0.4](https://github.com/idealista/airflow-role/tree/2.0.4)

[Full Changelog](https://github.com/idealista/airflow-role/compare/2.0.3...2.0.4)

### Fixed

- :hammer_and_wrench: Wrong webserver.pid path in template gunicorn-logrotate.j2 [#110](https://github.com/idealista/airflow-role/issues/110) @ginolegigot

## [2.0.3](https://github.com/idealista/airflow-role/tree/2.0.3)

[Full Changelog](https://github.com/idealista/airflow-role/compare/2.0.2...2.0.3)

### Changed

- :arrows_clockwise: Bump default airflow version to 2.1.1
- :arrows_clockwise: Bump requirements versions
- :arrows_clockwise: Some default values has been updated

### Added

- :heavy_plus_sign: Add regular users task
- :heavy_plus_sign: molecule config flower port exposed
- :heavy_plus_sign: molecule default scenario create admin and regular users
- :heavy_plus_sign: create home options

### Fixed

- :hammer_and_wrench: become configured user when check for admin users

## [2.0.2](https://github.com/idealista/airflow-role/tree/2.0.2)

[Full Changelog](https://github.com/idealista/airflow-role/compare/2.0.1...2.0.2)

### Fixed

- :hammer_and_wrench: Fix notify handler typo in task ➡️ [#99](https://github.com/idealista/airflow-role/issues/99) [BUG] notify restart airflow services not found when installing DAG dependencies

## [2.0.1](https://github.com/idealista/airflow-role/tree/2.0.1)

### Changed

- :arrows_clockwise: Update missing vars in cfg (v2) template
- :arrows_clockwise: Update conditionally vars missing or unnecessary in cfg (v2) template

### Fixed

- :hammer_and_wrench: Fix environment template PATH ➡️ [#96](https://github.com/idealista/airflow-role/issues/96) [BUG] Servie PATH environment not working as expected
- :hammer_and_wrench: Fix wrong typed and escaped log options in airflow-cfg.yaml group_vars ➡️ [#95](https://github.com/idealista/airflow-role/issues/95) [BUG] Tasks Log view is broken

### Added

- :heavy_plus_sign: tags for config files related
- :broom: Clean airflow-cfg.yml with bad format values and unnecessary quotation

## [2.0.0](https://github.com/idealista/airflow-role/tree/2.0.0)

[Full Changelog](https://github.com/idealista/airflow-role/compare/1.8.4...2.0.0)

### Added

- Support for new Apache Airflow 2.0 and its new configs files
- New templates and new group_vars files to fit better with new Apache Airflow 2.0
- New user related tasks
- [#82](https://github.com/idealista/airflow-role/issues/82) Add support to 2.0 airflow version @lorientedev

### Changed

- Project cleaning
- Updated ansible and molecule test requirements
- Updated molecule tests
- Updated travis file
- Updated yamllint
- Updated service templates
- Updated config and install tasks
- Updated [`README.md`](./README.md) to give more information about the role and advice some stuff
- [#54](https://github.com/idealista/airflow-role/issues/54) Install tasks fail when run without escalated privileges

### Fixed

- [#61](https://github.com/idealista/airflow-role/issues/61) Better worker restarts
- [#85](https://github.com/idealista/airflow-role/issues/85) Add extra args in pip install to allow different repositories @lorientedev

## [1.8.4](https://github.com/idealista/airflow-role/tree/1.8.4)

- [#82](https://github.com/idealista/airflow-role/issues/82) Add support to airflow 2.0 version. @lorientedev

## [1.8.3](https://github.com/idealista/airflow-role/tree/1.8.3)

- [#78](https://github.com/idealista/airflow-role/issues/78) Add path for services templates to allow overwrite from playbook @lorientedev

## [1.8.2](https://github.com/idealista/airflow-role/tree/1.8.2)

- [#75](https://github.com/idealista/airflow-role/issues/75) Added variable to change private_tmp value in service config @lorientedev

## [1.8.1](https://github.com/idealista/airflow-role/tree/1.8.1)

- [#68](https://github.com/idealista/airflow-role/issues/68) Update dependencies versions and solve some lint errors @lorientedev

## [1.8.0](https://github.com/idealista/airflow-role/tree/1.8.0)

[Full Changelog](https://github.com/idealista/airflow-role/compare/1.7.3...1.8.0)

### Added

- [#61](https://github.com/idealista/airflow-role/issues/61) Add KillSignal=SIGINT to workers service file @jnogol

### Fixed

- [#50](https://github.com/idealista/airflow-role/issues/50) Fix deprecation warning from jinja templates @adrimarteau @jnogol

## [1.7.3](https://github.com/idealista/airflow-role/tree/1.7.3)

[Full Changelog](https://github.com/idealista/airflow-role/compare/1.7.2...1.7.3)

### Fixed

- *[#55](https://github.com/idealista/airflow-role/pull/55) Use `{{ airflow_home }}` to set the default `airflow_database_conn` in defaults/main.yml* @davestern

## [1.7.2](https://github.com/idealista/airflow-role/tree/1.7.2)

[Full Changelog](https://github.com/idealista/airflow-role/compare/1.7.1...1.7.2)

### Fixed

- *[#47](https://github.com/idealista/airflow-role/issues/47) Fix web UI when using LDAP and Airflow>=1.10* @jnogol

## [1.7.1](https://github.com/idealista/airflow-role/tree/1.7.1)

[Full Changelog](https://github.com/idealista/airflow-role/compare/1.7.0...1.7.1)

### Changed

- *[#44](https://github.com/idealista/airflow-role/issues/44) Make role compatible with Airflow 1.10.0* @jnogol
- *Update Goss version to 0.3.6* @jnogol

## [1.7.0](https://github.com/idealista/airflow-role/tree/1.7.0)

[Full Changelog](https://github.com/idealista/airflow-role/compare/1.6.0...1.7.0)

### Changed

- *Update default version to 1.9.0* @jnogol
- *Ability to provide `airflow.cfg` template via playbooks* @jnogol
- *[#41](https://github.com/idealista/airflow-role/issues/41) Update `airflow.cfg` template with 1.9.0 features* @jnogol

### Added

- *Add sample DAG in tests to avoid scheduler issues* @jnogol
- *Add `airflow_` tags in `main.yml`* @jnogol

## [1.6.0](https://github.com/idealista/airflow-role/tree/1.6.0)

[Full Changelog](https://github.com/idealista/airflow-role/compare/1.5.0...1.6.0)

### Changed

- *[#38](https://github.com/idealista/airflow-role/pull/38) Parametrized PID files location, and create it on startup if it doesn't already exist.* @fhalim

## [1.5.0](https://github.com/idealista/airflow-role/tree/1.5.0)

[Full Changelog](https://github.com/idealista/airflow-role/compare/1.4.0...1.5.0)

### Added

- *[#36](https://github.com/idealista/airflow-role/issues/32) Add tasks in config to create variables and connections used in Airflow DAGs.* @deytao

## [1.4.0](https://github.com/idealista/airflow-role/tree/1.4.0)

[Full Changelog](https://github.com/idealista/airflow-role/compare/1.3.2...1.4.0)

### Added

- *[#32](https://github.com/idealista/airflow-role/issues/32) Use Goss instead of Testinfra* @jnogol

### Fixed

- *[#33](https://github.com/idealista/airflow-role/pull/33) Travis working* @jnogol

### Changed

- *[#31](https://github.com/idealista/airflow-role/pull/31) Using import_tasks instead of include and avoiding pip cache* @sschaetz
- *[#34](https://github.com/idealista/airflow-role/pull/34) Add config to have customizable pip and airflow executables* @deytao

## [1.3.2](https://github.com/idealista/airflow-role/tree/1.3.2)

[Full Changelog](https://github.com/idealista/airflow-role/compare/1.3.1...1.3.2)

### Fixed

- *[#28](https://github.com/idealista/airflow-role/issues/28) Fix Init DB task hang* @jnogol

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
