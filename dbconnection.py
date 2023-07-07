import databases
import sqlalchemy
from config import settings

DATABASE_URL = f'postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.DATABASE_HOST}:{settings.DATABASE_PORT}/{settings.POSTGRES_DB}'

pdatabase = databases.Database(DATABASE_URL)

engine = sqlalchemy.create_engine(DATABASE_URL, pool_size=3, max_overflow=0)
if not sqlalchemy.inspect(engine).has_table(settings.SOURCE_TABLE):
    print("Table not present")
metadata = sqlalchemy.MetaData(engine)
sqlalchemy.MetaData.reflect(metadata)
sources = metadata.tables[settings.SOURCE_TABLE]
