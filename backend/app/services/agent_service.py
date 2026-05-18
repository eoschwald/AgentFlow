from typing import Optional

from sqlalchemy.orm import Session

from app.models.agent import Agent
from app.schemas.agent import AgentCreate


def create_agent(db: Session, user_id: int, agent_in: AgentCreate) -> Agent:
    agent = Agent(
        user_id=user_id,
        name=agent_in.name,
        system_prompt=agent_in.system_prompt,
    )
    db.add(agent)
    db.commit()
    db.refresh(agent)
    return agent


def get_agents_for_user(db: Session, user_id: int) -> list[Agent]:
    return db.query(Agent).filter(Agent.user_id == user_id).all()


def get_agent_by_id(db: Session, user_id: int, agent_id: int) -> Optional[Agent]:
    return (
        db.query(Agent)
        .filter(Agent.user_id == user_id, Agent.id == agent_id)
        .first()
    )


def delete_agent(db: Session, user_id: int, agent_id: int) -> bool:
    agent = get_agent_by_id(db, user_id, agent_id)
    if not agent:
        return False

    db.delete(agent)
    db.commit()
    return True