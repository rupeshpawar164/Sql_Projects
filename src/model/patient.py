from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped,mapped_column,relationship

from src.db_config.db import Base
class Patient(Base):
    __tablename__ = "patient"
    id:Mapped[int]=mapped_column(Integer,primary_key=True)
    name:Mapped[str]=mapped_column(String(20),nullable=False)
    age:Mapped[int]=mapped_column(Integer,nullable=False)
    gender:Mapped[str]=mapped_column(String(10),nullable=False)

    appointments = relationship("Appointment", back_populates="patient", cascade="all, delete")

    def __repr__(self):
        return f"Patient({self.id},{self.name},{self.age},{self.gender})"
