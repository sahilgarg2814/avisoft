import sqlalchemy
#print(sqlalchemy.__version__)


engine = sqlalchemy.create_engine("mysql+pymysql://root:cHARIZOD100@@localhost/avisoft?host=localhost?port=3306")

with engine.connect() as conn:
    result = conn.execute(sqlalchemy.text("select * from jobs"))