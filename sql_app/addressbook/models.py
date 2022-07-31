
from sqlalchemy import Column, ForeignKey, Integer, String, Unicode, orm
from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType,ChoiceType,PhoneNumber
from ..database import Base



class AddressBook(Base):
    __tablename__ = "address_book"

    id = Column(Integer, primary_key=True, index=True)
    personal_info = relationship("PersonalInfo", back_populates="parent", uselist=False)
    contacts = relationship("Contact", back_populates="parent", uselist=False)
    location = relationship("Location", back_populates="parent", uselist=False)


class PersonalInfo(Base):
    __tablename__ = "personal_information"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

    addressbook_id = Column(Integer, ForeignKey("address_book.id"))
    for_addressbook = relationship("Addrssbook", back_populates="personal_information")


class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    addresses = relationship("Address",back_populates="contacts")
    email = Column(EmailType)
    _phone_number = Column(Unicode(20),unique=True)
    country_code = Column(Unicode(8))

    phone_number = orm.composite(
        PhoneNumber,
        _phone_number,
        country_code
    )
    
    addressbook_id = Column(Integer, ForeignKey("address_book.id"))
    for_addressbook = relationship("Addrssbook", back_populates="contacts")


class Address(Base):
    __tablename__ = "addresses"
    
    TYPES = [
        ('home', 'Home'),
        ('work', 'Work')
    ]
    id = Column(Integer, primary_key=True, index=True)
    type = Column(ChoiceType(TYPES))
    street_address = Column(String)
    city = Column(String)
    state = Column(String)
    country = Column(String)
    zip_code = Column(String)
    contact_id = Column(Integer, ForeignKey("contacts.id"))
    for_contact = relationship("Contact", back_populates="addresses")


class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    lat = Column(String)
    lng = Column(String)

    addressbook_id = Column(Integer, ForeignKey("address_book.id"))
    for_addressbook = relationship("Addrssbook", back_populates="locations")
    






    






