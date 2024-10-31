import requests
import os
import json


def get_credentials():
    username = os.getenv('DC_USERNAME')
    password = os.getenv('DC_PASSWORD')
    if not username or not password:
        raise ValueError("Missing DC_USERNAME or DC_PASSWORD environment variables")
    return {'username': username, 'password': password}


def _get_token(endpoint_choice) -> dict:
    try:
        # Set the login endpoint based on the user's choice
        if endpoint_choice == 1:
            dc_login = 'https://2a4p5ipvl9.execute-api.us-east-1.amazonaws.com/prod/login'  # STG endpoint
        else:
            dc_login = 'https://mhsq5ujf0l.execute-api.us-east-1.amazonaws.com/prod/login'  # PROD endpoint

        credentials = get_credentials()
        dc_conn = requests.post(dc_login, json=credentials)
        dc_conn.raise_for_status()
        return {"Authorization": "Bearer " + dc_conn.json().get("token", "")}
    except requests.exceptions.RequestException as e:
        print(f"Error getting token: {e}")
        return {}


def dc_request_params(cust_name, cust_id, endpoint_choice):

    if endpoint_choice == 1:
        url = "https://41j4w5l516.execute-api.us-east-1.amazonaws.com/prod/validate" #stg
    else:
        url = "https://t75covfr4d.execute-api.us-east-1.amazonaws.com/prod/validate/" #prod

    payload = {'comprehensiveSync': "true", 'customerId': cust_id, "customerIdentifier": cust_name}
    return url, payload


def make_endpoint_call(cname, cid, endpoint_choice):
    try:
        s = requests.Session()
        token = _get_token(endpoint_choice)
        if not token:
            raise ValueError("Token retrieval failed")
        s.headers.update(token)
        url, payload = dc_request_params(cname, cid, endpoint_choice)
        response = s.post(url, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error making API call: {e}")
        return {}


if __name__ == "__main__":
    customers = {
        1: {"name": "LIBERTY", "id": "a0bb259b-7f1a-5567-82a9-c0b15c35aa61"},
        2: {"name": "SHELLONSHORE", "id": "a4a73091-caad-5ede-8ef1-df6c97d67b21"},
        3: {"name": "EXAMPLE", "id": "12345678-1234-1234-1234-123456789012"}
    }

    print("Select an endpoint:")
    print("1. STG (Staging)")
    print("2. PROD (Production)")

    endpoint_choice = int(input("Enter the number for the endpoint (1 for STG, 2 for PROD): "))

    if endpoint_choice not in [1, 2]:
        print("Invalid endpoint choice.")
        exit()

    print("Select a customer:")
    for key, customer in customers.items():
        print(f"{key}. {customer['name']}")

    choice = int(input("Enter the number of the customer: "))

    if choice in customers:
        cust_name = customers[choice]['name']
        cust_id = customers[choice]['id']
        sol = make_endpoint_call(cust_name, cust_id, endpoint_choice)
        print(sol)
    else:
        print("Invalid choice.")
