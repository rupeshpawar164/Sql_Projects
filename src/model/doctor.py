from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped,mapped_column,relationship
from src.db_config.db import Base


class Doctor(Base):
    __tablename__ = "doctor"
    id:Mapped[int]=mapped_column(Integer,primary_key=True)
    name:Mapped[str]=mapped_column(String(100),nullable=False)
    specialization:Mapped[str]=mapped_column(String(100),nullable=False)

    appointments = relationship("Appointment",back_populates="doctor",cascade="all, delete")
    def __repr__(self):
        return f"Doctor(doctor id:{self.id}\n,doctor name:{self.name}\n,doctor speciality:{self.specialization})"

