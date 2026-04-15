import requests

BASE_URL = "https://parabank.parasoft.com/parabank/services/bank"

def test_get_accounts():
    response = requests.get(f"{BASE_URL}/customers/12212/accounts")
    assert response.status_code == 200

def test_account_details():
    response = requests.get(f"{BASE_URL}/accounts/13344")
    assert response.status_code == 200

def test_transactions():
    response = requests.get(f"{BASE_URL}/accounts/13344/transactions")
    assert response.status_code == 200