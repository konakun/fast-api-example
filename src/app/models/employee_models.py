from typing import Optional
from sqlmodel import SQLModel, Field

from src.utils.db_functions import DBModel

class Employee(DBModel, table=True):
    __tablename__: str = "employees"
    
    pk_employee: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(..., max_length=50)
    last_name: str = Field(..., max_length=50)
    age: int = Field(..., ge=1)
    salary: float
