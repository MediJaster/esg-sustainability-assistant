from pydantic import BaseModel


class ESGInfo(BaseModel):
    company_name: str
    industry_sector: str
