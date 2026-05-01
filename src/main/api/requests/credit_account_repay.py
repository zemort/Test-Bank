import requests
from requests import Response

from src.main.api.models.repay_user_request import RepayUserRequest
from src.main.api.models.repay_user_response import RepayUserResponse
from src.main.api.requests.requester import Requester


class RepayUserRequester(Requester):
    def post(self, repay_user_request: RepayUserRequest) -> RepayUserResponse | Response:
        url=f"{self.base_url}/credit/repay"
        response = requests.post(
            url=url,
            json=repay_user_request.model_dump(),
            headers=self.headers
        )
        self.response_spec(response)
        return RepayUserResponse(**response.json())