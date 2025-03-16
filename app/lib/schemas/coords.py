from .abc import BaseSchema


class MessageSchema(BaseSchema):
    listener: list[list[int]]
    sender: list[list[int]]
    price: list[list[float]]
    status: str
