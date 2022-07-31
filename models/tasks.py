from curses import meta
from xmlrpc.client import DateTime
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

tasks = Table("tasks", meta, Column(
    "id", Integer, primary_key=True),
        Column("user_id", Integer),
        Column("title", String(255)),
        Column("description", String(255)),
        Column("created_at", String(255)),
        Column("updated_at", String(255)))

deleted_tasks = Table("deleted_tasks", meta, Column(
    "id", Integer, primary_key=True),
        Column("user_id", Integer),
        Column("title", String(255)),
        Column("description", String(255)),
        Column("created_at", String(255)),
        Column("updated_at", String(255)),
        Column("deleted_at", String(255)))

meta.create_all(engine)