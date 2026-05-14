from typing import Any

from pydantic import BaseModel, Field


class AgentAskRequest(BaseModel):
    system_id: str = Field(
        ...,
        description="The external system calling this Agentic RAG service.",
    )
    task_type: str = Field(
        ...,
        description="The type of task the agent should perform.",
    )
    question: str = Field(
        ...,
        description="The user or system question.",
    )
    context: dict[str, Any] = Field(
        default_factory=dict,
        description="Extra structured data needed for the task.",
    )