import os
import sys
from sqlalchemy import Column, ForeignKey, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()
 
class NflSeason(Base):
    __tablename__ = 'nfl_season'
    # Here we define columns for the table nfl season
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    season = Column(String(4), nullable=False)
    
class NflWeek(Base):
    __tablename__ = 'nfl_week'
    # Here we define columns for the table nfl weeks.
    id = Column(Integer, primary_key = True)
    week = Column(String(2))

class NflTeam(Base):
    __tablename__ = 'nfl_team'
    # Here we define columns for the table nfl team names.
    id = Column(Integer, primary_key = True)
    city = Column(String(30), nullable = False)
    state = Column(String(2), nullable = False)
    team_name = Column(String(30), nullable = False)

class Position(Base):
    __tablename__ = 'position'
    # Here we define columns for the table nfl positions.
    id = Column(Integer, primary_key=True)
    position = Column(String(5), nullable=False)
    season_id = Column(Integer, ForeignKey('nfl_season.id'))
    
class Player(Base):
    __tablename__ = 'player'
    # Here we define columns for the table nfl players.
    id = Column(Integer, primary_key = True)
    player_name = Column(String(50), nullable = False)
    player_position = Column(String(5), ForeignKey('position.id'))
    
class PlayerStats(Base):
    __tablename__ = 'player_stats'
    # Here we define columns for the table nfl positions.
    player_id = Column(Integer, primary_key = True)
    player_name = Column(String(50), ForeignKey('player.player_name'))
    team_id = Column(Integer, ForeignKey('nfl_team.id'))
    season_id = Column(Integer, ForeignKey('nfl_season.id'))
    week_id = Column(Integer, ForeignKey('nfl_week.id'))
    position_id = Column(String(3), ForeignKey('position.id'))
    ffpts = Column(Float)
    patt = Column(Float)
    pcomp = Column(Float)
    pyds = Column(Float)
    ptds = Column(Integer)
    pint = Column(Integer)
    p2 = Column(Integer)
    ruatt = Column(Float)
    ruyds = Column(Float)
    rutds = Column(Integer)
    ru2 = Column(Integer)
    ruatt = Column(Integer)
    ruyds = Column(Float)
    rutds = Column(Integer)
    ru2 = Column(Integer)
    rec = Column(Integer)
    recyds = Column(Float)
    rectds = Column(Integer)
    rec2 = Column(Integer)
    
    
    
    
    
    
    
    
# Create an engine that stores data in the local directory's
# nfl_fanatsy.db file.
engine = create_engine('sqlite:///nfl_fantasy.db')
 
# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)