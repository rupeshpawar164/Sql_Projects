from sqlalchemy import select
from sqlalchemy.orm import selectinload
from src.model.appointment import Appointment

class AppointmentDao:
    def __init__(self, session):
        self.session = session

    async def add_appointment(self, appointment):
        self.session.add(appointment)
        await self.session.flush()
        return appointment

    async def view_appointment(self):
        state = select(Appointment).options(
            selectinload(Appointment.doctor),
            selectinload(Appointment.patient)
        )
        result = await self.session.execute(state)
        return result.scalars().all()

    async def view_by_id(self, appointment_id):
        return await self.session.get(
            Appointment,
            appointment_id
        )

    async def delete_appointment(self, appointment_id):
        state = select(Appointment).where( Appointment.id == appointment_id )
        result = await self.session.execute(state)
        appointment = result.scalar_one_or_none()
        if not appointment:
            return None
        await self.session.delete(appointment)
        await self.session.flush()
        return appointment

    async def update_appointment(self,appointment_id,appointment_data):
        state = select(Appointment).where(Appointment.id == appointment_id)
        result = await self.session.execute(state)
        appointment = result.scalar_one_or_none()
        if not appointment:
            return None
        appointment.patient_id = appointment_data.patient_id
        appointment.doctor_id = appointment_data.doctor_id
        appointment.appointment_date = (appointment_data.appointment_date)
        await self.session.flush()
        return appointment