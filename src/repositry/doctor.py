from unittest import result

from sqlalchemy.orm import session
from sqlalchemy.util import await_only

from src.model.doctor import Doctor
from sqlalchemy import select
class DoctoDao:
    def __init__(self,session):
        self.session = session

    async def add_doctor(self, doc):
        self.session.add(doc)
        await self.session.flush()
        return doc

    async def view_doctor(self):
        state=select(Doctor)
        docs=await self.session.execute(state)
        return docs.scalars().all()

    async def delete_doctor(self,id):
        state=select(Doctor).where(Doctor.id==id)
        result=await self.session.execute(state)
        doctor=result.scalar_one_or_none()
        if not doctor:
            return None
        else:
            await self.session.delete(doctor)
            await self.session.flush()
            return doctor

    async def view_by_id(self,doctor_id):
       return await self.session.get(Doctor,doctor_id)

    async def update_doctor(self, doctor_id,doc):
        state=select(Doctor).where (Doctor.id==doctor_id)
        result=await self.session.execute(state)
        doctor=result.scalar_one_or_none()
        if not doctor:
            return None
        doctor.name=doc.name
        doctor.specialization=doc.specialization
        await self.session.flush()
        return doctor





