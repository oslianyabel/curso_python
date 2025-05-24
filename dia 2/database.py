import os
from typing import Dict, Optional

from dotenv import load_dotenv

load_dotenv()

from sqlalchemy import (
    TIMESTAMP,
    BigInteger,
    Boolean,
    Column,
    ForeignKey,
    Integer,
    MetaData,
    String,
    Table,
    Text,
    create_engine,
    delete,
    insert,
    update,
)
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.sql import func


class DatabaseManager:
    def __init__(self, database_url: str):
        self.database_url = database_url
        self.metadata = MetaData()
        self.engine = create_engine(database_url)
        self.Session = scoped_session(sessionmaker(bind=self.engine))

        self.users = Table("users", self.metadata, *self._get_user_columns())
        self.reminders = Table(
            "reminders", self.metadata, *self._get_reminder_columns()
        )

        self.metadata.create_all(self.engine)

    def _get_user_columns(self):
        return [
            Column("id", BigInteger, primary_key=True),
            Column("username", String(100)),
            Column("first_name", String(100), nullable=False),
            Column("last_name", String(100)),
            Column("time_zone", String(50)),
            Column("default_reminder_minutes", Integer, default=60),
            Column("is_active", Boolean, nullable=False, default="true"),
        ]

    def _get_reminder_columns(self):
        return [
            Column("id", BigInteger, primary_key=True),
            Column("user_id", ForeignKey("users.id"), nullable=False),
            Column("title", String(255), nullable=False),
            Column("description", Text),
            Column("date", TIMESTAMP()),
            Column("reminder_time", TIMESTAMP(), nullable=False),
            Column("status", String(100), default="pending"),
            Column("created_at", TIMESTAMP(), default=func.now()),
            Column("updated_at", TIMESTAMP()),
        ]

    def connect(self):
        self.session = self.Session()
        print("Connected to database")

    def disconnect(self):
        if hasattr(self, "session"):
            self.session.close()
            print("Disconnected from database")

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    # Generic CRUD
    def create_model(self, data: Dict, table: Table, debug_info: str = None) -> int:
        if debug_info:
            print(debug_info)

        query = insert(table).values(data)
        result = self.session.execute(query)
        self.session.commit()
        return result.inserted_primary_key[0]

    def get_model(
        self, id: int, table: Table, debug_info: str = None
    ) -> Optional[Dict]:
        if debug_info:
            print(debug_info)

        query = table.select().where(table.c.id == id)
        result = self.session.execute(query)
        return result.fetchone()._asdict() if result.rowcount else None

    def update_model(
        self, id: int, data: Dict, table: Table, debug_info: str = None
    ) -> bool:
        if debug_info:
            print(debug_info)

        query = update(table).where(table.c.id == id).values(data)
        result = self.session.execute(query)
        self.session.commit()
        return result.rowcount > 0

    def delete_model(self, id: int, table: Table, debug_info: str = None) -> bool:
        if debug_info:
            print(debug_info)

        query = delete(table).where(table.c.id == id)
        result = self.session.execute(query)
        self.session.commit()
        return result.rowcount > 0


db = DatabaseManager(os.getenv("DATABASE_URL"))
