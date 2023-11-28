from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.settings import settings

# engine = create_engine("postgresql://USUARIO:PASSWORD@HOST/NOMBRE_DB") (echo=True) (connect_args={"options": "-c timezone=utc"})
engine = create_engine(f"postgresql://{settings.DB_US}:{settings.DB_PASS}@{settings.DB_HOST}/{settings.DB_NAME}", echo=True)

SessionLocal = sessionmaker(engine)