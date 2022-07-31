from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel

class IdGeneratorModel(BaseModel):
    id : Optional[UUID] = uuid4()


class PersonalInfoBase(IdGeneratorModel):
    first_name : str
    last_name : str
    age : int

class AddressTypes(BaseModel):
    home : str
    work : str


class AddressBase(IdGeneratorModel):
    type : List[AddressTypes]
    street_address : str
    city : str
    state : str
    country : str
    zip_code : str
    


class ContactBase(IdGeneratorModel):
    addresses : List[AddressBase]
    email : str
    _phone_number : str
    country_code : str


class LocationBase(IdGeneratorModel):
    lat : str
    lng : str




class AddressBook(IdGeneratorModel):
    personal_info : PersonalInfoBase
    contacts : ContactBase
    location : LocationBase


    
    


