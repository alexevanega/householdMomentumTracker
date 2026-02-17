from app.models.base import Base, TimestampMixin

# Import models so SQLAlchemy registers them before create_all()
from app.models.user import User
from app.models.task import Task
from app.models.daily_win import DailyWin