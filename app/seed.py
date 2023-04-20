from ipdb import set_trace
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *
from rich.console import Console
import random

console = Console()


if __name__ == '__main__':

  print("Connecting to DB....")
  engine = create_engine('sqlite:///survivor.db')
  session = sessionmaker(bind=engine)()
  print("Session Created...")

  fake = Faker()
  
  
  print("Dropping DB...")
  session.query(Contestant).delete()
  session.query(Season).delete()
  session.query(Result).delete()
  session.commit()
  

  print("CREATING Models....")
  contestants = [Contestant(name=fake.name(), age=random.randint(20,65)) for i in range(14) ]
  session.add_all(contestants)
  session.commit()
    
  allstars = Season(name="All-Stars", location="Pearl Islands")
  worlds_apart = Season(name="Worlds Apart", location="San Juan del Sur")
  session.add_all([allstars,worlds_apart])
  session.commit()
  
  allstar_results = Result(
    season = allstars.id, 
    first = contestants[0].id,
    second = contestants[1].id,
    third = contestants[2].id,
    fourth =  contestants[3].id,
    fifth = contestants[4].id,
    sixth = contestants[5].id,
    winner = contestants[6].id,
    )
  
  worlds_apart_results = Result(
    season = worlds_apart.id, 
    first = contestants[7].id,
    second = contestants[8].id,
    third = contestants[9].id,
    fourth =  contestants[10].id,
    fifth = contestants[11].id,
    sixth = contestants[12].id,
    winner = contestants[13].id,
    )
  
  session.add_all([allstar_results,worlds_apart_results])
  session.commit()
  
  set_trace()
  

  print("DONE!")