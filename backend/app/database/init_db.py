from backend.app.database.base import Base
from backend.app.database.database import engine

# Import models để SQLAlchemy biết các table
import backend.app.models


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
    print("SafeSTEM database tables created successfully.")