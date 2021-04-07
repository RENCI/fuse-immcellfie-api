# ImmCellFIE Project Quality Control (QC) plan

## Overview

For quality control, we use a combination of peer-reviewed acceptance testing for manual systems and automated regression testing for containerized appliances and dashboard.
We use [pytest](https://docs.pytest.org/en/stable/) and [dockerhub](https://hub.docker.com) auto builds for automated testing, and failed tests are flagged directly on the 
github repositories using [shields.io](https://shields.io/category/build) to generate dockerhub build status badges.

## Automated Regression Testing

Each docker-containerized appliance comprizing this framework is added as a submodule to this repo. Each submodule has unit tests installed under `<main>/tests`. 
The bash script, `<main>/tests/test.sh` can be used to kick-off the tests. Tests are run automatically by dockerhub through pytest which picks up tests named `def test_<some test` in a file called `<main>/tests/test_<some-file>.py`. The `test.sh` shell script sets all the variables found in `<main>/.env` and kicks off the docker container builds using docker-compose. 
Subsequently, pytest will look for any files matching the following regular expression: `<main>/tests/test_*.py`. Within those files, pytest will run and report the 
results of any tests matching the regular expression: `def test_*():`.

## System Testing

Currently we  manually system test via peer review. Upon completion of each milestone, the accountable developer presents a demo of the implemented functionality to a 
pre-assigned  acceptance tester (AT). The milestone can be marked as complete only after the demo has met the AT's approval. AT's and approvals are tracked alongside
the [project plan](https://drive.google.com/file/d/1H5ocHVMpFI9Ju3CdT_NVYG4yHXoR-jz9/view).
