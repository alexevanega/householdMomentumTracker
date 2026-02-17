from datetime import date as dt, datetime
from sqlalchemy import Date, DateTime, ForeignKey, String, Text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base, TimestampMixin
from app.models.enums import DailyWinStatus

class DailyWin(Base, TimestampMixin):
    __tablename__ = "daily_wins"

    __table_args__ = (
        UniqueConstraint("date", name="uq_daily_win_date")
    )

    id: Mapped[int] = mapped_column(primary_key=True)

    # One record per calendar day
    date: Mapped[dt] = mapped_column(Date, nullable=False)
    task_id: Mapped[int] = mapped_column(ForeignKey("tasks.id"), nullable=False)

    # Stored as string for stability/debuggability
    status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default=DailyWinStatus.ACTIVE.value
    )

    # Notes enforced in Phase 2
    note: Mapped[str | None] = mapped_column(Text, nullable=True)
    selected_by_user_id: Mapped[int | None] = mapped_column(ForeignKey("users.id"), nullable=True)
    completed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    
    task = relationship("Task", lazy="joined")
    selected_by = relationship("User", lazy="joined")