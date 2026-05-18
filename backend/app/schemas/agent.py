from pydantic import BaseModel, ConfigDict


class AgentCreate(BaseModel):
    name: str
    system_prompt: str


class AgentRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    name: str
    system_prompt: str