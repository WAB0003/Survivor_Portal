# Import Any Additional sqlalchemy types here
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///survivor.db')
session = sessionmaker(bind=engine)()

Base = declarative_base()

# Models:
class Season(Base):
  __tablename__ = "seasons"
  
  id = Column(Integer(), primary_key=True)
  name = Column(String())
  location = Column(String())
  
  @property
  def results(self):
      return session.query(Result).filter(Result.id == self.id).first()
  


  def __repr__(self):
    return f'Season {self.id}: {self.name}'



class Contestant(Base):
    __tablename__ = "contestants"
  
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    age = Column(Integer())

    def __repr__(self):
        return f"""
        Player ID:\t{self.id}
        Name:\t{self.name}
        age:\t{self.age}
    """
    
class Result(Base):
    __tablename__ = "results"
    id = Column(Integer(), primary_key=True)
    season = Column(Integer(), ForeignKey("seasons.id"))
    first = Column(Integer(), ForeignKey("contestants.id"))
    second = Column(Integer(), ForeignKey("contestants.id"))
    third = Column(Integer(), ForeignKey("contestants.id"))
    fourth = Column(Integer(), ForeignKey("contestants.id"))
    fifth = Column(Integer(), ForeignKey("contestants.id"))
    sixth = Column(Integer(), ForeignKey("contestants.id"))
    winner = Column(Integer(), ForeignKey("contestants.id"))

    def __repr__(self):
        return f"""
        Result: {self.id}
        Season: {self.season}
        Order of Dropouts:
                {self.first}
                {self.second}
                {self.third}
                {self.fourth} 
                {self.fifth}
                {self.sixth}
        Winner: {self.winner}
    """