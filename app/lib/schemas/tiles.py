from .abc import BaseSchema


class MessageSchema(BaseSchema):
    data: list[list[int]]


class TilesSchema(BaseSchema):
    message: MessageSchema
    status: str
