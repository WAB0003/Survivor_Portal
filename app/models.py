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
        Name:\t\t{self.name}
        age:\t\t{self.age}
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
    
    
    
    def get_first_name(self):
        return session.query(Contestant.name).filter(Contestant.id == self.first)
        

    def __repr__(self):
        return f"""
        Results for Season: {self.season}
        Order of Contestant Dropouts:
            first:  {session.query(Contestant.name).filter_by(id=self.first).first()[0]}
                    {session.query(Contestant.name).filter_by(id=self.second).first()[0]}
                    {session.query(Contestant.name).filter_by(id=self.third).first()[0]}
                    {session.query(Contestant.name).filter_by(id=self.fourth).first()[0]}
                    {session.query(Contestant.name).filter_by(id=self.fifth).first()[0]}
                    {session.query(Contestant.name).filter_by(id=self.sixth).first()[0]}
            Winner: {session.query(Contestant.name).filter_by(id=self.winner).first()[0]}
    """