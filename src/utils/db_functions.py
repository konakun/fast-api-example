from sqlalchemy.exc import SQLAlchemyError
from sqlmodel import SQLModel


class DBModel(SQLModel):
    def save(self, db):
        try:
            db.add(self)
            db.commit()
            db.refresh(self)
            return True
        except SQLAlchemyError as e:
            db.rollback()
            return False

    def update(self, dict_changes, db):
        try:
            obj = self
            
            for key, value in dict_changes.items():
                setattr(obj, key, value)
            
            db.commit()
            return True
        except SQLAlchemyError as e:
            db.rollback()
            return False

    def delete(self, db):
        db.delete(self)
        return db.commit()

