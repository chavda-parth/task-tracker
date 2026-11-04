from enum import StrEnum


class TaskStatus(StrEnum):
    TODO = 'to-do'
    IN_PROGRESS = 'in-progress'
    DONE = 'done'