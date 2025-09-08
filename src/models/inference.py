from pydantic import BaseModel


class ESGResponse(BaseModel):
    trace_id: str
    final_report: str
