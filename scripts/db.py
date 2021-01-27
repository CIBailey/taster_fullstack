from uuid import uuid4
from random import randint, choice
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Enum,
    DateTime,
    Float,
    ForeignKey,
)
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy_utils import EmailType
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from faker import Faker

fake = Faker()

Base = declarative_base()
engine = create_engine(
    "postgresql+psycopg2://user:secret@localhost:5432/customer", echo=True
)

## Tables creation
class Customer(Base):
    __tablename__ = "customers"

    uuid = Column(UUID, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(EmailType, nullable=False)
    country = Column(
        Enum("FR", "UK", name="country_enum", create_type=False),
        nullable=False,
    )
    city = Column(
        Enum("Paris", "London", name="city_enum", create_type=False),
        nullable=False,
    )
    orders = relationship("Order")


class Order(Base):
    __tablename__ = "orders"

    uuid = Column(UUID, primary_key=True)
    date = Column(DateTime, nullable=False)
    price = Column(Float, nullable=False)
    nb_of_articles = Column(Integer, nullable=False)
    shift = Column(
        Enum("dinner", "lunch", name="shift_enum", create_type=False),
        nullable=False,
    )
    customer_uuid = Column(UUID, ForeignKey("customers.uuid"))


Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


## Data creation
Session = sessionmaker(bind=engine)

session = Session()
for i in range(0, 100):
    country = choice([("UK", "London"), ("FR", "Paris")])
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = f"{first_name}.{last_name}@taster.com"
    customer = Customer(
        uuid=str(uuid4()),
        first_name=first_name,
        last_name=last_name,
        email=email,
        country=country[0],
        city=country[1],
    )
    session.add(customer)
    for i in range(0, randint(1, 4)):
        session.add(
            Order(
                uuid=str(uuid4()),
                date=fake.past_date(),
                price=round(
                    fake.pyfloat(positive=True, min_value=10, max_value=150), ndigits=2
                ),
                nb_of_articles=fake.pyint(min_value=1, max_value=10),
                shift=choice(["dinner", "lunch"]),
                customer_uuid=customer.uuid,
            )
        )
session.commit()
