from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Engine = create_engine('sqlite:///students.db')
Session = sessionmaker(bind=Engine)
