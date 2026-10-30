import json

from datetime import datetime, timezone

from src.task_status import TaskStatus
from src.utils import validate_type


class Task:
    _id: int
    _description: str
    _status: TaskStatus
    _created_at: datetime
    _updated_at: datetime

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int):
        validate_type('Id', value, int)
        
        if value <= 0:
            raise ValueError('Id must be a positive integer.')

        self._id = value

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value: str):
        validate_type('Description', value, str)

        if len(value) == 0:
            raise ValueError('No description provided.')
        
        self._description = value

    @property
    def status(self) -> TaskStatus:
        return self._status

    @status.setter
    def status(self, value: TaskStatus):
        validate_type('Status', value, TaskStatus)

        self._status = value

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @created_at.setter
    def __created_at(self, value: datetime):
        validate_type('Created At', value, datetime)  
        self._created_at = value

    @property
    def updated_at(self) -> datetime:
        return self._updated_at

    @updated_at.setter
    def __updated_at(self, value: datetime):
        validate_type('Updated At', value, datetime)

        if value < self.created_at:
            raise ValueError('Invalid value for Updated At')

        self._updated_at = value

    def __init__(self, id: int, description: str) -> None: 
        self.id = id
        self.description = description
        self.status = TaskStatus.TODO

        utc_now: datetime = datetime.now(timezone.utc)
        self.__created_at = utc_now
        self._updated_at = utc_now

    @classmethod
    def from_json(cls, json_string: str) -> Task:
        dict_obj: dict = json.loads(json_string)
        task = Task(
            dict_obj['id'], 
            dict_obj['description']
        )
        task.status = TaskStatus(dict_obj['status'])
        task.__created_at = datetime.fromtimestamp(dict_obj['created_at'], timezone.utc)
        task.__updated_at = datetime.fromtimestamp(dict_obj['updated_at'], timezone.utc)

        return task

    def __to_dict(self) -> dict:
        return {
            'id': self.id,
            'description': self.description,
            'status': self.status.value,
            'created_at': self.created_at.timestamp(),
            'updated_at': self.updated_at.timestamp()
        }