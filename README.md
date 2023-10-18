# api_project

Test API in Python for petstore.swagger.io.

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)

## Description

This project leverages several tools and libraries to facilitate API testing:

- **Pytest**: Pytest is a built-in Python testing framework that simplifies writing and running tests for your Python code.

- **Selenium**: Selenium is a popular web testing framework that enables browser automation for testing web applications.

- **Pydantic**: Pydantic is used for data validation.

- **Requests Library**: We utilize Python's built-in `requests` library for making API calls.

## Installation

To install all project dependencies, navigate to the root project path and execute the following command:

```shell
pip install -r requirements.txt
```

## Usage

in the root path run the next command to run all tests from test_main:
```shell
pytest
```

in the root path run the next command to run tests using marker:
```shell
pytest -m MyMarker
```
