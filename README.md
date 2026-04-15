# ParaBank API Testing with CI/CD using GitHub Actions

![CI](https://github.com/YOUR_GITHUB_USERNAME/parabank-api-ci/actions/workflows/api_test.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.11-blue)
![pytest](https://img.shields.io/badge/tested%20with-pytest-green)
![CI/CD](https://img.shields.io/badge/CI-CD%20Pipeline-orange)

---

## Project Objective

This project demonstrates **API automation testing** of ParaBank services and integration with **CI/CD pipeline using GitHub Actions**.

The pipeline automatically executes API tests whenever code is pushed to GitHub.

---

## Tech Stack

- Python
- Pytest
- Requests
- GitHub Actions
- REST API Testing

---

## Project Structure

parabank-api-ci
│
├── test_parabank_api.py
├── requirements.txt
│
└── .github
└── workflows
└── api_test.yml

---

## APIs Covered

Base URL:https://parabank.parasoft.com/parabank/services/bank


### Get Customer Accounts
GET /customers/{customerId}/accounts

### Get Account Details
GET /accounts/{accountId}

### Get Transactions
GET /accounts/{accountId}/transactions

---

## How Tests Work

Python scripts send requests to ParaBank APIs and validate:

- Status Code = 200
- API response received
- Endpoint working correctly

Example:
assert response.status_code == 200 

---

## CI/CD Pipeline

GitHub Actions automatically runs tests:

Trigger:
- push to main branch
- pull request

Steps:
1. Checkout code
2. Setup Python
3. Install dependencies
4. Run pytest
5. Show results

---

## Run Locally

Install dependencies:

pip install -r requirements.txt


---

## Learning Outcome

- API testing using Python
- pytest automation
- CI/CD pipeline implementation
- GitHub Actions integration
- Backend testing basics

---

## Author

Nitish Shukla
