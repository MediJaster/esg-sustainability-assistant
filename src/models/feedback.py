from pydantic import BaseModel, Field


class FeedbackData(BaseModel):
    trace_id: str
    rating: int = Field(..., ge=1, le=5, description="Rating between 1 and 5")
    feedback_text: str | None = Field(None, description="Optional textual feedback")
