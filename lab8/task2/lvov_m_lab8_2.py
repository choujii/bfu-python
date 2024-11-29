from sqlalchemy import create_engine, Column, Integer, String, Date, Time, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker


engine = create_engine("sqlite:///delivery_service.db")
Base = declarative_base()


class Courier(Base):
    __tablename__ = 'Courier'
    courier_id = Column(Integer, primary_key=True)
    last_name = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    middle_name = Column(String)
    passport_number = Column(String)
    birth_date = Column(Date)
    hire_date = Column(Date)
    work_start_time = Column(Time)
    work_end_time = Column(Time)
    city = Column(String)
    street = Column(String)
    house = Column(Integer)
    apartment = Column(Integer)
    phone = Column(String)

class Transport(Base):
    __tablename__ = 'Transport'
    vehicle_id = Column(Integer, primary_key=True)
    brand = Column(String, nullable=False)
    registration_date = Column(Date)
    color = Column(String)

class Sender(Base):
    __tablename__ = 'Sender'
    sender_id = Column(Integer, primary_key=True)
    last_name = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    middle_name = Column(String)
    birth_date = Column(Date)
    postal_code = Column(String)
    city = Column(String)
    street = Column(String)
    house = Column(Integer)
    apartment = Column(Integer)
    phone = Column(String)

class Receiver(Base):
    __tablename__ = 'Receiver'
    receiver_id = Column(Integer, primary_key=True)
    last_name = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    middle_name = Column(String)
    birth_date = Column(Date)
    postal_code = Column(String)
    city = Column(String)
    street = Column(String)
    house = Column(Integer)
    apartment = Column(Integer)
    phone = Column(String)

class Order(Base):
    __tablename__ = 'Order'
    order_id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, ForeignKey('Sender.sender_id'), nullable=False)
    receiver_id = Column(Integer, ForeignKey('Receiver.receiver_id'), nullable=False)
    order_date = Column(Date)
    delivery_date = Column(Date)
    delivery_price = Column(Integer)
    courier_id = Column(Integer, ForeignKey('Courier.courier_id'))
    vehicle_id = Column(Integer, ForeignKey('Transport.vehicle_id'))

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

print("Таблицы успешно созданы!")
