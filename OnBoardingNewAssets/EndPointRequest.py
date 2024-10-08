import requests
import os
import json

# Fetching credentials from environment variables
def get_credentials():
    username = os.getenv('DC_USERNAME')
    password = os.getenv('DC_PASSWORD')
    if not username or not password:
        raise ValueError("Missing DC_USERNAME or DC_PASSWORD environment variables")
    return {'username': username, 'password': password}

def _get_token() -> dict:
    try:
        dc_login = 'https://2a4p5ipvl9.execute-api.us-east-1.amazonaws.com/prod/login'
        credentials = get_credentials()
        dc_conn = requests.post(dc_login, json=credentials)
        dc_conn.raise_for_status()  # Raises an exception for 4xx/5xx errors
        return {"Authorization": "Bearer " + dc_conn.json().get("token", "")}
    except requests.exceptions.RequestException as e:
        print(f"Error getting token: {e}")
        return {}

def dc_request_params(cust_name, cust_id):
    url = "https://41j4w5l516.execute-api.us-east-1.amazonaws.com/prod/validate"
    payload = {'comprehensiveSync': "true", 'customerId': cust_id, "customerIdentifier": cust_name}
    return url, payload

def make_endpoint_call(cname, cid):
    try:
        s = requests.Session()
        token = _get_token()
        if not token:
            raise ValueError("Token retrieval failed")
        s.headers.update(token)
        url, payload = dc_request_params(cname, cid)
        response = s.post(url, json=payload)
        response.raise_for_status()  # Ensure the request was successful
        return response.json()  # Assuming JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error making API call: {e}")
        return {}

if __name__ == "__main__":
    #cust_name = "LIBERTY"
    cust_name = "SHELLONSHORE"
    #cust_id = "a0bb259b-7f1a-5567-82a9-c0b15c35aa61"
    cust_id = "a4a73091-caad-5ede-8ef1-df6c97d67b21"
    sol = make_endpoint_call(cust_name, cust_id)
    print(sol)
