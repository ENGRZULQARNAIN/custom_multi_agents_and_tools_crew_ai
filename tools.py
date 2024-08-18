from crewai_tools import BaseTool

class SearchDocters(BaseTool):
    name: str = "Doctors Finder"
    description: str = "you are helpful when need to search a doctors for the patient, according to the patient provided requirements."

    def _run(self) -> list:
        # Your tool's logic here
        doctors=[
    {
        "name": "Dr Ali Muhammad",
        "specialization": "Cardiology",
        "fee": "1000",
        "city": "Mardan",
        "gender": "Male"
    },
    {
        "name": "Dr Sara Khan",
        "specialization": "Dermatology",
        "fee": "1500",
        "city": "Karachi",
        "gender": "Female"
    },
    {
        "name": "Dr Ahmed Raza",
        "specialization": "Orthopedics",
        "fee": "1200",
        "city": "Lahore",
        "gender": "Male"
    },
    {
        "name": "Dr Ayesha Ahmed",
        "specialization": "Pediatrics",
        "fee": "1100",
        "city": "Islamabad",
        "gender": "Female"
    },
    {
        "name": "Dr Hassan Ali",
        "specialization": "Neurology",
        "fee": "2000",
        "city": "Peshawar",
        "gender": "Male"
    },
    {
        "name": "Dr Farah Javed",
        "specialization": "Gynecology",
        "fee": "1800",
        "city": "Quetta",
        "gender": "Female"
    },
    {
        "name": "Dr Imran Haider",
        "specialization": "Ophthalmology",
        "fee": "1300",
        "city": "Multan",
        "gender": "Male"
    },
    {
        "name": "Dr Hina Shahid",
        "specialization": "Psychiatry",
        "fee": "1600",
        "city": "Rawalpindi",
        "gender": "Female"
    },
    {
        "name": "Dr Asad Mehmood",
        "specialization": "Urology",
        "fee": "1700",
        "city": "Faisalabad",
        "gender": "Male"
    },
    {
        "name": "Dr Saira Bano",
        "specialization": "Oncology",
        "fee": "2100",
        "city": "Hyderabad",
        "gender": "Female"
    }
]

        return  doctors
    

obj = SearchDocters()

print(obj._run())
