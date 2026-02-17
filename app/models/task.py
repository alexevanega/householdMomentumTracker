from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base, TimestampMixin
from app.models.enums import TaskDomain, TaskEffort, TaskStatus

class Task(Base, TimestampMixin):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)

    # Store enums as strings (stable, readable, and easy to debug)
    domain: Mapped[str] = mapped_column(String(30), nullable=False, default=TaskDomain.OTHER.value)
    effort: Mapped[str] = mapped_column(String(30), nullable=False, default=TaskEffort.SMALL.value)
    status: Mapped[str] = mapped_column(String(30), nullable=False, default=TaskStatus.BACKLOG.value)

    definition_of_done: Mapped[str] = mapped_column(Text, nullable=False)
    materials_needed: Mapped[str | None] = mapped_column(Text, nullable=False)
    owner_user_id: Mapped[int | None] = mapped_column(ForeignKey("users.id"), nullable=True)

    # Relationship is optional now but will help later
    owner = relationship("User",lazy="joined")