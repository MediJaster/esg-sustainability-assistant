from pydantic import BaseModel


class CompanyInfo(BaseModel):
    name: str
    industry_sector: str
