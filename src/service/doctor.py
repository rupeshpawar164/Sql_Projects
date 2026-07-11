from sqlalchemy.util import await_only

from src.repositry.doctor import DoctoDao
class DoctorService:
    def __init__(self,session):
        self.doctor_dao = DoctoDao(session)

    async def add_doctor(self,doc):
        return await self.doctor_dao.add_doctor(doc)

    async def view_doctor(self):
        return await self.doctor_dao.view_doctor()

    async def delete_doctor(self,id):
        return await self.doctor_dao.delete_doctor(id)

    async def view_by_id(self,doctor_id):
        return await self.doctor_dao.view_by_id(doctor_id)

    async def update_doctor(self,doctor_id,doc):
        return  await self.doctor_dao.update_doctor(doctor_id,doc)






