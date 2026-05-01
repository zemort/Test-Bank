import requests
from requests import Response

from src.main.api.models.credit_user_response import CreditUserResponse
from src.main.api.models.credit_user_request import CreditUserRequest
from src.main.api.requests.requester import Requester


class CreditUserRequester(Requester):
    def post(self, credit_user_request: CreditUserRequest) -> CreditUserResponse | Response:
        url=f"{self.base_url}/credit/request"
        response = requests.post(
            url=url,
            json=credit_user_request.model_dump(),
            headers=self.headers
        )
        self.response_spec(response)
        return CreditUserResponse(**response.json())
