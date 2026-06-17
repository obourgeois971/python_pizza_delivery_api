from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine(
    "mysql+pymysql://root:root@192.168.150.3:3306/learn_hibernate",
    echo=True
)
Base=declarative_base()
Session=sessionmaker()
