from typing import Annotated

from src.main.api.generators.creation_rule import CreationRule
from src.main.api.models.create_user_request import CreateUserRequest


class CreateUserRequestCredit(CreateUserRequest):
    role: Annotated[str, CreationRule(regex=r"^ROLE_CREDIT_SECRET")]