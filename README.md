# Learning Python for Application Integration and Security

This project contains a Python simple script for grading assignments and accompanying unit tests. The purpose is to practice unit testing with Python, covering aspects like Statement Coverage, Functional Coverage, Conditional Coverage, and Branch Coverage.

## Usage

- Run the script: `npm main`
- Run tests: `npm test`

## Components

- **testGrader.py**: Contains unit tests using `unittest` framework to evaluate `grader.py`.
- **grader.py**: Main script with the Grader class for assignment evaluation.
- **grader_mock.py**: Provides mock data for unit tests.

## Logging

Test results are logged in `testlog.log`, indicating pass or fail for each test case.

## How it Works

1. **Unit Testing**: `testGrader.py` contains unit tests covering various aspects of the grader functionality.
2. **Mock Data**: `grader_mock.py` provides mock data used in the unit tests to simulate different scenarios.
3. **Logging**: Test results are logged in `testlog.log`, indicating whether each test case passed or failed.
