from src.app.models.employee_models import Employee

from src.utils.singleton import singleton


@singleton
class EmployeeService:
    def insert(self, db, data):
        saved = data.save(db)
        if not saved:
            return None
        return self.retrieve(db, data.pk_employee)
    
    def fetch(self, db):
        return db.query(Employee).all()
    
    def retrieve(self, db, pk_employee):
        return db.query(Employee).filter(Employee.pk_employee == pk_employee).first()
    
    def modify(self, db, pk_employee, data):
        base_item = self.retrieve(db, pk_employee)
        result = base_item.update(data, db)
        if result:
            db.refresh(base_item)
            return base_item
        return None
    
    def delete(self, db, pk_employee):
        employee_to_delete = self.retrieve(db, pk_employee)
        if not employee_to_delete:
            return False
        return employee_to_delete.delete(db)

employee_service = EmployeeService()