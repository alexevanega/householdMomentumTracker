from enum import StrEnum

class TaskDomain(StrEnum):
    CHORES = "CHORES"
    BILLS = "BILLS"
    FOOD = "FOOD"
    REPAIRS = "REPAIRS"
    OTHER = "OTHER"

class TaskEffort(StrEnum):
    TINY = "TINY"
    SMALL = "SMALL"
    MEDIUM = "MEDIUM"
    COMPLEX = "COMPLEX"

class TaskStatus(StrEnum):
    BACKLOG = "BACKLOG"
    ACTIVE = "ACTIVE"
    PAUSED = "PAUSED"
    BLOCKED = "BLOCKED"
    DONE = "DONE"
    ABANDONED = "ABANDONED"

class DailyWinStatus(StrEnum):
    ACTIVE = "ACTIVE"
    DONE = "DONE"
    PAUSED = "PAUSED"
    BLOCKED = "BLOCKED"