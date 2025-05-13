from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime
engine = create_engine("mysql://root:root@localhost/province")

MetaData_obj= MetaData()


province = Table('province', MetaData_obj,
    Column('sigla', String(2), primary_key=True),
    Column('nome', String(30)),
    Column('residenti', Integer),
    Column('Kmq', Integer),

)

regioni = Table('regioni', MetaData_obj,
    Column('id', Integer, primary_key=True),
    Column('nome', String(50)),
)
                
MetaData_obj.create_all(engine)