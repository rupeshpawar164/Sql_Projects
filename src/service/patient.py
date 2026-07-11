from src.repositry.patient import PatientDao


class PatientService:

    def __init__(self, session):
        self.patient_dao = PatientDao(session)

    async def add_patient(self, patient):
        return await self.patient_dao.add_patient(patient)

    async def view_patient(self):
        return await self.patient_dao.view_patient()

    async def view_by_id(self, patient_id):
        return await self.patient_dao.view_by_id(patient_id)

    async def delete_patient(self, patient_id):
        return await self.patient_dao.delete_patient(patient_id)

    async def update_patient(self, patient_id, patient):
        return await self.patient_dao.update_patient(
            patient_id,
            patient
        )