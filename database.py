from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime
engine = create_engine("mysql+sqlconnector://root:root@localhost/evento_musicale")