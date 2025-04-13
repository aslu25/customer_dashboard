from sqlalchemy import Column, Integer, String, Float, Date
from app.database import Base

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    vc_id = Column(String, unique=True)
    cust_id = Column(String)

class CustomerTransaction(Base):
    __tablename__ = "cust_trans"
    id = Column(Integer, primary_key=True, index=True)
    vc_id = Column(String)
    transaction_date = Column(Date)
    base_price = Column(Float)