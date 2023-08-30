from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URL = "mysql+pymysql://db_user:db_password@db_host:db_port/db_name"
engine = create_engine(DB_URL, echo=False)
Base = declarative_base(engine)
Session = sessionmaker(engine)
