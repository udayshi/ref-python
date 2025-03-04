from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
Base = declarative_base()
is_test = False

if is_test:
    SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"  # Replace with your DB URL
else:
    SQLALCHEMY_DATABASE_URL = "sqlite:///./fast-api-pydantic-sqlalchemy.db"  # Replace with your DB URL
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
