from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref





Base = declarative_base()



########################################################################
class User(Base):
    """"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

class Link(Base):
    """"""

    __tablename__ = "link"

    id = Column(Integer, primary_key=True)
    link = Column(String)
    content = Column(String)

# ----------------------------------------------------------------------
#def __init__(self, username, password):
#    """"""
#    self.username = username
#    self.password = password
engine = create_engine('sqlite:///securityHubDB.db', echo=True)
    # create tables
Base.metadata.create_all(engine)