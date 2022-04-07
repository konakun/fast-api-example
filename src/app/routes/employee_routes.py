from fastapi import APIRouter, Depends, Path, status, HTTPException
from sqlmodel import Session

from src.app.models.employee_models import Employee

from src.app.services.employee_services import (
    employee_service
)

from src.config.database import get_db


employee_router = APIRouter(
    prefix='/employees',
    tags=['employees'],
    dependencies=[]
    )

@employee_router.get('', response_model=list[Employee])
async def get_employees(db: Session = Depends(get_db)):
    data = employee_service.fetch(db)
    if not data:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail='No se encontraron empleados.'
        )
    return data


@employee_router.get('/{pk_employee}')
async def get_employee(pk_employee: int = Path(..., gt=0), db: Session = Depends(get_db)):
    data = employee_service.retrieve(db, pk_employee)
    if not data:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail='No se encontro al empleado.'
        )
    return data

@employee_router.post('', status_code=status.HTTP_201_CREATED, response_model=Employee)
async def add_employee(employee: Employee, db: Session = Depends(get_db)):
    data = employee_service.insert(db, employee)
    if not data:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            detail='No se pudo crear el empleado.'
        )
    return data

@employee_router.put('/{pk_employee}', status_code=status.HTTP_200_OK, response_model=Employee)
async def update_employee(employee: dict, pk_employee: int = Path(..., gt=0), 
                          db: Session = Depends(get_db)):
    data = employee_service.modify(db, pk_employee, employee)
    if not data:
        raise HTTPException(
            status.HTTP_406_NOT_ACCEPTABLE,
            detail='No se pudo editar el empleado.'
        )
    return data

@employee_router.delete('/{pk_employee}', status_code=status.HTTP_202_ACCEPTED)
async def delete_employee(pk_employee: int = Path(..., gt=0), db: Session = Depends(get_db)):
    return employee_service.delete(db, pk_employee)
