import datetime

from sqlalchemy import Column, BIGINT, String, Boolean, DateTime

from utils import Base


class Project(Base):
    __tablename__ = "jira_project"
    id = Column("project_id", BIGINT, primary_key=True, autoincrement=True, nullable=False, unique=True)
    key = Column("project_key", String(50), nullable=False)
    name = Column("project_name", String(50), nullable=False)
    is_active = Column("is_active", Boolean, nullable=False, default=False)
    create_time = Column("create_time", DateTime, nullable=False, default=datetime.datetime.now())
    update_time = Column("update_time", DateTime, nullable=False, default=datetime.datetime.now(),
                         onupdate=datetime.datetime.now())
    last_grab_time = Column("last_grab_time", DateTime)
    grab_status = Column("grab_status", String(2))
    last_grab_success_time = Column("last_grab_success_time", DateTime)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id})"
