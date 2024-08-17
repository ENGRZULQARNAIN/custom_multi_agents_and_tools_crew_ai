from crewai_tools import BaseTool

class SearchDocters(BaseTool):
    name: str = "Doctors Finder"
    description: str = "you are helpful when need to search a doctors for the patient according to the patient requirements."

    def _run(self, city: str, specialist:str, price_range:int, gender_prefrences:str) -> str:
        # Your tool's logic here
        return "Tool's result"