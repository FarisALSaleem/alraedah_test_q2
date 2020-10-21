from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class Graduate(Base):
    __tablename__ = 'graduate'
    id = Column(Integer, primary_key=True)
    السنة_الدراسية = Column(DateTime)
    المرحلة_الدراسية = Column(String)
    المستوى_الدراسي = Column(String) #same thing
    نوع_المؤسسة_التعليمية = Column(String)
    المنطقة_الإدارية = Column(String)
    المحافظة = Column(String)
    نوع_الجهة = Column(String)
    الجهة_التعليمية = Column(String)
    المجال_الواسع = Column(String)
    المجال_الضيق = Column(String)
    المجال_التفصيلي = Column(String)
    نظام_الدراسة = Column(String)
    الجنس = Column(String)
    الجنسية = Column(String)
    العدد = Column(Integer)


# connect to db
db_url = 'postgresql://alraedah_user:plain_text@localhost/graduate'
engine = create_engine(db_url)

# create tables
Base.metadata.create_all(engine)
