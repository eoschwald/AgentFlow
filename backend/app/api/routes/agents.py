from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_current_user, get_db
from app.schemas.agent import AgentCreate, AgentRead
from app.services.agent_service import (
    create_agent,
    delete_agent,
    get_agent_by_id,
    get_agents_for_user,
)

router = APIRouter(prefix="/agents", tags=["agents"])


@router.post("", response_model=AgentRead, status_code=status.HTTP_201_CREATED)
def create_new_agent(
    agent_in: AgentCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return create_agent(db, current_user.id, agent_in)


@router.get("", response_model=list[AgentRead])
def list_agents(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return get_agents_for_user(db, current_user.id)


@router.get("/{agent_id}", response_model=AgentRead)
def read_agent(
    agent_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    agent = get_agent_by_id(db, current_user.id, agent_id)
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    return agent


@router.delete("/{agent_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_agent(
    agent_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    deleted = delete_agent(db, current_user.id, agent_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Agent not found")
    return None