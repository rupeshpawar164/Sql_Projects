import asyncio
from sqlalchemy.exc import SQLAlchemyError
from src.db_config.db import sessionLocal
from src.model.doctor import Doctor
from src.model.patient import Patient
from src.service.doctor import DoctorService
from src.service.patient import PatientService

from datetime import datetime
from src.model.appointment import Appointment
from src.service.appointment import AppointmentService


async def add_doctor():
   try:
       name = input("Enter your name: ")
       specialization = input("Enter your specialization: ")
       async with sessionLocal() as session:
           async with session.begin():
                doc=Doctor(
                   name=name,
                   specialization=specialization
                )
                doctor_service=DoctorService(session)
                result=await doctor_service.add_doctor(doc)
                await session.refresh(result)
                print("doctor added")

   except SQLAlchemyError as e:
       print(e)

async def view_doctor():
    try:
        async with sessionLocal() as session:
            doctor_service=DoctorService(session)
            result=await doctor_service.view_doctor()
            for doctor in result:
                print(doctor)
    except SQLAlchemyError as e:
        print(e)

async def delete_doctor():
    try:
        id=int (input("enter id for delete"))
        async with sessionLocal() as session:
            async with session.begin():
                doctor_service=DoctorService(session)
                result=await doctor_service.delete_doctor(id)
                if result:
                    print("doctor deleted succefully")
                else:
                    print("doctor not found")
    except SQLAlchemyError as e :
        print (e)

async def view_by_id():
    try:
        doctor_id=input("search doctor by id")
        async with  sessionLocal() as session:
            doctor_service=DoctorService(session)
            result=await doctor_service.view_by_id(doctor_id)
            print(result)

    except SQLAlchemyError as e:
        print(e)

async def update_doctor():
    try:
        doctor_id=int(input("enter id for update"))
        async with sessionLocal() as session:
            async with session.begin():
                name=input("enter new name ")
                specialization=input("enter speciality")
                doc=Doctor(name=name,specialization=specialization)
                doctor_service=DoctorService(session)
                result=await doctor_service.update_doctor(doctor_id,doc)
                if result:
                    print("updated succesfully")
                else:
                    print("updation failed")

    except SQLAlchemyError as e:
        print(e)



async def add_patient():
    try:
        name = input("enter patient name : ")
        age = int(input("enter age : "))
        gender = input("enter gender : ")
        async with sessionLocal() as session:
            async with session.begin():
                patient = Patient(
                    name=name,
                    age=age,
                    gender=gender
                )
                patient_service = PatientService(session)
                result = await patient_service.add_patient(
                    patient
                )
                await session.refresh(result)
                print("patient added successfully")
    except SQLAlchemyError as e:
        print(e)

async def view_patient():
    try:
        async with sessionLocal() as session:
            patient_service = PatientService(session)
            result = await patient_service.view_patient()
            for patient in result:
                print(patient)
    except SQLAlchemyError as e:
        print(e)

async def patient_by_id():
    try:
        patient_id = int(input("enter patient id : "))
        async with sessionLocal() as session:
            patient_service = PatientService(session)
            result = await patient_service.view_by_id(
                patient_id
            )
            print(result)
    except SQLAlchemyError as e:
        print(e)


async def delete_patient():
    try:
        patient_id = int(input("enter patient id : "))
        async with sessionLocal() as session:
            async with session.begin():
                patient_service = PatientService(session)
                result = await patient_service.delete_patient(
                    patient_id
                )
                if result:
                    print("patient deleted")
                else:
                    print("patient not found")
    except SQLAlchemyError as e:
        print(e)

async def update_patient():
    try:
        patient_id = int(input("enter patient id : "))
        name = input("enter new name : ")
        age = int(input("enter new age : "))
        gender = input("enter gender : ")
        async with sessionLocal() as session:
            async with session.begin():
                patient = Patient(
                    name=name,
                    age=age,
                    gender=gender
                )
                patient_service = PatientService(session)
                result = await patient_service.update_patient(
                    patient_id,
                    patient
                )
                if result:
                    print("patient updated")
                else:
                    print("patient not found")
    except SQLAlchemyError as e:
        print(e)


async def add_appointment():
    try:
        patient_id = int(input("enter patient id : "))
        doctor_id = int(input("enter doctor id : "))
        date = input("enter appointment date (YYYY-MM-DD) : ")
        appointment_date = datetime.strptime(date,"%Y-%m-%d").date()
        async with sessionLocal() as session:
            async with session.begin():
                appointment = Appointment(
                    patient_id=patient_id,
                    doctor_id=doctor_id,
                    appointment_date=appointment_date
                )
                appointment_service = AppointmentService(session)
                result = await (appointment_service.add_appointment(appointment))
                await session.refresh(result)
                print("appointment booked")

    except SQLAlchemyError as e:
        print(e)

async def view_appointment():
    try:
        async with sessionLocal() as session:
            appointment_service = AppointmentService(session)
            result = await (appointment_service.view_appointment())
            for appointment in result:
                print(f"\nappointment id : {appointment.id}")
                print(f"patient name : " f"{appointment.patient.name}")
                print(f"doctor name : " f"{appointment.doctor.name}")
                print(f"appointment date : " f"{appointment.appointment_date}")
    except SQLAlchemyError as e:
        print(e)


async def delete_appointment():
    try:
        appointment_id = int(input("enter appointment id : "))
        async with sessionLocal() as session:
            async with session.begin():
                appointment_service=(AppointmentService(session))
                result = await (appointment_service.delete_appointment(appointment_id))
                if result:
                    print("appointment deleted")
                else:
                    print("appointment not found")
    except SQLAlchemyError as e:
        print(e)


async def update_appointment():
    try:
        appointment_id = int(input("enter appointment id : "))
        patient_id = int(input("enter new patient id : "))
        doctor_id = int(input("enter new doctor id : "))
        date = input("enter new appointment date ""(YYYY-MM-DD) : ")
        appointment_date = datetime.strptime(date,"%Y-%m-%d").date()
        async with sessionLocal() as session:
            async with session.begin():
                appointment = Appointment(
                    patient_id=patient_id,
                    doctor_id=doctor_id,
                    appointment_date=appointment_date
                )
                appointment_service=(AppointmentService(session))
                result = await (appointment_service.update_appointment(appointment_id,appointment))
                if result:
                    print("appointment updated")
                else:
                    print("appointment not found")
    except SQLAlchemyError as e:
        print(e)

async def main():
    while True:
        print("1 for doctor")
        print("2 for patient")
        print("3 for appointment")
        print("4 for exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            while True:
                print("1 for add doctor")
                print("2 for view doctor")
                print("3 for delete doctor")
                print("4 for view by ID doctor")
                print("5 for update doctor")
                print("6 for exit")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    await add_doctor()
                elif choice == 2:
                    await view_doctor()
                elif choice==3:
                    await delete_doctor()
                elif choice==4:
                    await view_by_id()
                elif choice==5:
                    await update_doctor()
                elif choice==6:
                    break


        elif choice == 2:
            while True:
                print("1 for add patient")
                print("2 for view patient")
                print("3 for patient by id")
                print("4 for delete patient")
                print("5 for update patient")
                print("6 for back")
                choice = int(input("enter choice : "))
                if choice == 1:
                    await add_patient()

                elif choice == 2:
                    await view_patient()

                elif choice == 3:
                    await patient_by_id()

                elif choice == 4:
                    await delete_patient()

                elif choice == 5:
                    await update_patient()

                elif choice == 6:
                    break

        elif choice == 3:
            while True:
                print("1 for add appointment")
                print("2 for view appointment")
                print("3 for delete appointment")
                print("4 for update appointment")
                print("5 for back")

                choice = int(input("enter choice : "))

                if choice == 1:
                    await add_appointment()

                elif choice == 2:
                    await view_appointment()

                elif choice == 3:
                    await delete_appointment()

                elif choice == 4:
                    await update_appointment()

                elif choice == 5:
                    break

        if choice == 4:
            break
asyncio.run(main())