from src.repositry.appointment import AppointmentDao
class AppointmentService:
    def __init__(self, session):
        self.appointment_dao = AppointmentDao(session)

    async def add_appointment(self, appointment):
        return await self.appointment_dao.add_appointment(appointment)

    async def view_appointment(self):
        return await self.appointment_dao.view_appointment()

    async def view_by_id(self, appointment_id):
        return await self.appointment_dao.view_by_id(appointment_id)

    async def delete_appointment(self, appointment_id):
        return await self.appointment_dao.delete_appointment(appointment_id)

    async def update_appointment(self,appointment_id,appointment):
        return await self.appointment_dao.update_appointment(appointment_id, appointment)