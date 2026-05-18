from pydantic import BaseModel, ConfigDict


class ChatRequest(BaseModel):
    agent_id: int
    message: str


class ChatResponse(BaseModel):
    response: str


class MessageRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    role: str
    content: str