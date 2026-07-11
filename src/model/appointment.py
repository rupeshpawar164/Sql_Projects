from datetime import date
from sqlalchemy import Integer, ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.db_config.db import Base

class Appointment(Base):
    __tablename__ = "appointment"
    id: Mapped[int] = mapped_column( Integer,primary_key=True )
    patient_id: Mapped[int] = mapped_column(ForeignKey("patient.id"),nullable=False)
    doctor_id: Mapped[int] = mapped_column(ForeignKey("doctor.id"),nullable=False)
    appointment_date: Mapped[date] = mapped_column(Date,nullable=False)

    patient = relationship("Patient",back_populates="appointments")

    doctor = relationship("Doctor",back_populates="appointments")

    def __repr__(self):
        return   f"Appointment(id={self.id},patient_id={self.patient_id},doctor_id={self.doctor_id},appointment_date={self.appointment_date}"