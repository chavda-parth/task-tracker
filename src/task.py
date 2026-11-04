import json

from datetime import datetime, timezone
from typing import Self

from src.task_status import TaskStatus
from src.utils import validate_type


class Task:
    _task_id: int
    _description: str
    _status: TaskStatus
    _created_at: datetime
    _updated_at: datetime

    @property
    def task_id(self) -> int:
        return self._task_id

    @property
    def description(self) -> str:
        return self._description

    @property
    def status(self) -> TaskStatus:
        return self._status

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @property
    def updated_at(self) -> datetime:
        return self._updated_at

    def __init__(
        self, 
        task_id: int, 
        description: str,
        status: TaskStatus = TaskStatus.TODO,
        created_at: datetime | None = None,
        updated_at: datetime | None = None,
    ): 
        now: datetime = Task._get_utc_now()
        self._task_id = Task._validate_task_id(task_id)
        self._description = Task._validate_task_description(description) 
        self._status = status
        self._created_at = created_at or now
        self._updated_at = updated_at or self.created_at

    # @classmethod
    # def from_json(cls, json_string: str) -> Self:
    #     data = json.loads(json_string)
        
    #     required = {
    #         'task_id',
    #         'description',
    #         'status',
    #         'created_at',
    #         'updated_at'
    #     }

    #     if required - data.keys():
    #         raise ValueError('Corrupt or Invalid json.')

    #     task_created_at = datetime.fromisoformat(data['created_at'])
    #     task_updated_at = datetime.fromisoformat(data['updated_at'])

    #     if task_updated_at < task_created_at:
    #         raise ValueError('Invalid task metadata.')
        
    #     task = cls(
    #         data['id'], 
    #         data['description']
    #     )
    #     task._status = TaskStatus(data['status'])
    #     task._created_at = task_created_at
    #     task._updated_at = task_updated_at
    #     return task

    def to_json(self) -> str:
        return json.dumps({
            'task_id': self.task_id,
            'description': self.description,
            'status': self.status.value,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        })

    @staticmethod
    def _validate_task_id(value: int) -> int:
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f'Id must be of type int, got {type(value).__name__}')

        if value <= 0:
            raise ValueError('Id must be a positive integer.')

        return value

    @staticmethod
    def _validate_task_description(value: str) -> str:
        if not isinstance(value, str):
            raise TypeError(f'Description must be of type str, got {type(value).__name__}')

        if len(value) == 0 or value.isspace():
            raise ValueError('Description cannot be empty.')

        return value        

    @staticmethod
    def _get_utc_now() -> datetime:
        return datetime.now(timezone.utc)

    def update_description(self, value: str):
        new_value = Task._validate_task_description(value)
        self._description = new_value
        self._updated_at = Task._get_utc_now()

    def update_status(self, value: TaskStatus):
        # TODO: Add validation method to check value
        new_value = value
        if new_value != self._status:
            self._status = new_value
            self._updated_at = Task._get_utc_now()