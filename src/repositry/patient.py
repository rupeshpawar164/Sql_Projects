from sqlalchemy import select
from src.model.patient import Patient

class PatientDao:
    def __init__(self, session):
        self.session = session

    async def add_patient(self,patient):
        self.session.add(patient)
        await self.session.flush()
        return patient

    async def view_patient(self):
        state=select(Patient)
        result = await self.session.execute(state)
        return result.scalars().all()

    async def view_by_id(self, patient_id):
        return await self.session.get(Patient, patient_id)

    async def delete_patient(self, patient_id):
        state = select(Patient).where(
            Patient.id == patient_id
        )
        result = await self.session.execute(state)
        patient = result.scalar_one_or_none()
        if not patient:
            return None
        await self.session.delete(patient)
        await self.session.flush()
        return patient

    async def update_patient(self, patient_id, patient_data):
        state = select(Patient).where(
            Patient.id == patient_id
        )
        result = await self.session.execute(state)
        patient = result.scalar_one_or_none()
        if not patient:
            return None
        patient.name = patient_data.name
        patient.age = patient_data.age
        patient.gender = patient_data.gender
        await self.session.flush()
        return patient