import requests

from helper.config import *


# inisiasi hit api ke qase
def push_result(test_case_id, status):
    payload = {
        "case_id": test_case_id,
        "status": status
    }

    head = {
        "accept": "application/json",
        "content-type": "application/json",
        "Token": TOKEN_QASE
    }

    resp = requests.post(f"{api_result_qase_io}{PROJECT_CODE_QASE_IO}/{PROJECT_ID_QASE_IO}", json=payload, headers=head)