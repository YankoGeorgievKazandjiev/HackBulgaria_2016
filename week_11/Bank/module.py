from settings import DB_NAME
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

class BankUser(Base):

    __tablename__ = 'client'
    id = Column(Integer, primary_key = True)
    username = Column(String(250), nullable = False)
    password = Column(String(250), nullable = False)
    balance = Column(Float, nullable = False)
    message = Column(String(250), nullable = False)
    email = Column(String(50), nullable = False)

    def __str__(self):
        return 'Client: {}'.format(self.username)

    def __repr__(self):
        return self.__str__()

class TanCode(Base):

    __tablename__ = 'tan_codes'

    id = Column('id', Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('client.id'))
    tan_code = Column(String(250), nullable=False)

    _ = relationship('BankUser', backref='tan_codes')

engine = create_engine(DB_NAME)
Base.metadata.create_all(engine)
b =BankUser()
