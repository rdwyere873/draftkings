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
    
    
class TeamLocation(Base):
    __tablename__ = 'team_location'
    # Here we define the city and state of every NFL orginazation
    id = Column(Integer, primary_key= True)
    city = Column(String(20), nullable=False)
    state = Column(String(20), nullable=False)
    time_zone = Column(String(3), nullable=False)

class NflTeam(Base):
    __tablename__ = 'nfl_team'
    # Here we define columns for the table nfl team names.
    id = Column(Integer, primary_key = True)
    team_name = Column(String(30), nullable = False)
    abbr = Column(String(20), nullable=False)
    location_id = Column(Integer, ForeignKey('team_location.id'))

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
    team_id = Column(Integer, ForeignKey('nfl_team.id'))
    opponent_id = Column(Integer, ForeignKey('nfl_team.id'))
    season_id = Column(Integer, ForeignKey('nfl_season.id'))
    week= Column(Integer)
    position_id = Column(String(3), ForeignKey('position.id'))
    rank = Column(Integer)
    player_name = Column(String(50), ForeignKey('player.player_name'))
    comp = Column(Float)
    att = Column(Float)
    yds = Column(Float)
    tds = Column(Integer)
    picks = Column(Integer)
    ruatt = Column(Float)
    ruyds = Column(Float)
    rutds = Column(Integer)
    targets = Column(Integer)
    rec = Column(Integer)
    recyds = Column(Float)
    rectds = Column(Integer)
    
    
    
    
    
    
    
    
# Create an engine that stores data in the local directory's
# nfl_fanatsy.db file.
engine = create_engine('sqlite:///nfl_fantasy.db')
 
# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)