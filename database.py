from sqlalchemy import create_engine, Column, String, Float, Integer, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import Config
from datetime import datetime
import os

Base = declarative_base()

class Material(Base):
    __tablename__ = 'materials'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    category = Column(String(100))
    unit = Column(String(50))
    price = Column(Float)
    quantity = Column(Float, default=0)
    supplier_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.now)

class Project(Base):
    __tablename__ = 'projects'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    dwg_file = Column(String(500))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)

class Supplier(Base):
    __tablename__ = 'suppliers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    contact = Column(String(255))
    email = Column(String(255))
    phone = Column(String(20))
    address = Column(Text)
    created_at = Column(DateTime, default=datetime.now)

class AuditLog(Base):
    __tablename__ = 'audit_logs'
    
    id = Column(Integer, primary_key=True)
    user = Column(String(255))
    action = Column(String(255))
    details = Column(Text)
    timestamp = Column(DateTime, default=datetime.now)

class Database:
    def __init__(self):
        db_path = Config.get_db_path()
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.engine = create_engine(f'sqlite:///{db_path}')
        self.Session = sessionmaker(bind=self.engine)
        Base.metadata.create_all(self.engine)
    
    def get_session(self):
        return self.Session()