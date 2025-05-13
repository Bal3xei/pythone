from typing import List, Optional
from sqlalchemy import ForeignKey,String
from sqlalchemy.orm import DeclarativeBase, relationship ,Mapped, mapped_column
from sqlalchemy import create_engine
engine = create_engine("mysql://root:root@localhost/province")

class Base(DeclarativeBase):
    pass

class Provincia(Base):
    __tablename__ = 'provincia'
    id: Mapped[str] = mapped_column(String(30),primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column(String(30), nullable=True)
    residenti: Mapped[int] = mapped_column(nullable=True)
    kmq: Mapped[int] = mapped_column(nullable=True)
    regione_id:Mapped[int] = mapped_column(ForeignKey("regione.id"), nullable=True)
    regione:Mapped["Regione"] = relationship(back_populates="provincia")

class Regione(Base):
    __tablename__ = 'regione'
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column(String(30), nullable=True)
    province: Mapped[List["Provincia"]] = relationship(back_populates="regione", cascade="all, delete-orphan")

# province = Table('province', MetaData_obj,
#     Column('sigla', String(2), primary_key=True),
#     Column('nome', String(50)),
#     Column('residenti', Integer),
#     Column('Kmq', Integer),

# )

# regioni = Table('regioni', MetaData_obj,
#     Column('id', Integer, primary_key=True),
#     Column('nome', String(50)),
# )


Base.metadata.create_all(engine)