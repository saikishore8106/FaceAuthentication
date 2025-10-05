from sqlalchemy import create_engine, Column, Integer, String, Date, Time, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# PostgreSQL connection details
DB_USER = "postgres"
DB_PASSWORD = "1234"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "authticationdb"

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# SQLAlchemy setup
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Table definition
class AuthenticationLog(Base):
    __tablename__ = "authentication_logs"
    id = Column(Integer, primary_key=True, index=True)
    person_name = Column(String(255))
    date = Column(Date)
    time = Column(Time)
    captured_image_path = Column(Text)
    auth_image_path = Column(Text)

# Create table if not exists
Base.metadata.create_all(bind=engine)

def save_auth_log(person_name, captured_image_path, auth_image_path=None):
    """Save authentication log to PostgreSQL"""
    session = SessionLocal()
    try:
        now = datetime.now()
        log = AuthenticationLog(
            person_name=person_name if person_name else "Unknown",
            date=now.date(),
            time=now.time(),
            captured_image_path=captured_image_path,
            auth_image_path=auth_image_path
        )
        session.add(log)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()
