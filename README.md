# Page Object Model - Automated Testing Repository

## Overview

This repository implements the **Page Object Model (POM)** design pattern for automating the testing of web applications using Python testing frameworks like pytest. The POM pattern promotes maintainability and scalability by separating the test logic from the user interface elements, making it easier to extend and update tests as the application evolves.

## Repository Structure

- **Config/**  
  Stores configuration files for the tests, such as environment settings and test data.

- **Pages/**  
  Contains the page objects representing different views of the web application:
  - `base_pages.py`: Base class for all page objects, containing shared logic and helper methods.
  - `elements.py`: Defines web elements used across multiple pages.
  - `homePage.py`: Page object representing the application's homepage.
  - `loginPage.py`: Page object representing the login page.
  - `text.py`: Stores common text or messages used in tests.

- **Test/**  
  This directory contains automated tests for various functionalities:
  - `test_parametrize.py`: Parameterized tests to run the same tests with different data sets.
  - `test_homePage.py`: Tests related to interactions on the homepage.
  - `test_loginPage.py`: Tests for the login page functionality.
  - `test_fixtures.py`: Contains configuration and data used across tests (fixtures).

- **Test_YT/**  
  Includes tests created for YouTube tutorials or example cases.

- **assets/**  
  Additional resources, such as files or data used during tests.

## Project Status

The project is currently **in progress**. While the basic structure is in place, several tests are still under development, including those for `homePage.py`, `loginPage.py`, and parameterized test cases. Some core features, such as test logic and fixtures, need to be fully implemented.

## Future Plans

- Complete test implementations for `homePage` and `loginPage`.
- Add comprehensive test coverage for various user interactions and edge cases.
- Implement more advanced test parametrization and integration with CI/CD pipelines.
- Further optimize and refactor the code for maintainability.

## Requirements

- Python 3.x
- Pytest
- Selenium/WebDriver (for web testing)
