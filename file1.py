import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tables import Base
from tables import User

engine = create_engine('sqlite:///test.db', echo = True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
session.add(ed_user)

session.commit()
session.close()
