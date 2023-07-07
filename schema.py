from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class TimeSourceIn(BaseModel):
    last_update_date: Optional[datetime]
    from_date: Optional[datetime]
    to_date: Optional[datetime]


class SourceIn(BaseModel):
    source: str = Field(max_length=200)
    source_type: str = Field(max_length=10)
    source_tag: str = Field(max_length=10)
    frequency: str = Field(max_length=5)

    last_update_date: datetime
    from_date: datetime
    to_date: datetime

class Source(SourceIn):
    source_id: int