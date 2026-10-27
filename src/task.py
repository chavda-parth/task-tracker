from task_status import TaskStatus
from datetime import datetime, timezone


class Task:
    task_id: int
    description: str
    status: TaskStatus
    createdAt: datetime
    updatedAt: datetime

    def __init__(self: Task, description: str):
        self.description = description
        self.status = TaskStatus.TODO

        utc_now: datetime = datetime.now(timezone.utc)
        created_at = utc_now
        updatedAt = utc_now
        