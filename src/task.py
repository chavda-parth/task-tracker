from datetime import datetime, timezone

from src.task_status import TaskStatus
from src.utils import validate_type


class Task:
    _id: int
    _description: str
    status: TaskStatus
    created_at: datetime
    updated_at: datetime

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int):
        validate_type('id', value, int)
        
        if value <= 0:
            raise ValueError('id must be a positive integer.')

        self._id = value

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value: str):
        validate_type('description', value, str)

        if len(value) == 0:
            raise ValueError('No description provided.')
        
        self._description = value

    def __init__(self: Task, id: int, description: str): 
        self.id = id
        self.description = description
        self.status = TaskStatus.TODO

        utc_now: datetime = datetime.now(timezone.utc)
        self.created_at = utc_now
        self.updated_at = utc_now