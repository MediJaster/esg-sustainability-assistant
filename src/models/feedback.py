from pydantic import BaseModel, Field


class FeedbackData(BaseModel):
    """
    Feedback data for ESG report evaluation.

    Parameters
    ----------
    trace_id : str
        Unique identifier for the ESG report feedback.
    rating : int
        Rating between 1 and 5 (unitless), inclusive.
        Range
            [1, 5]
    feedback_text : str or None
        Optional textual feedback.

    Returns
    -------
    FeedbackData
        Instance of feedback data.

    Examples
    --------
    >>> FeedbackData(trace_id="abc123", rating=5)
    FeedbackData(trace_id='abc123', rating=5, feedback_text=None)

    Notes
    -----
    All fields are required except `feedback_text`.
    """

    trace_id: str
    rating: int = Field(..., ge=1, le=5, description="Rating between 1 and 5")
    feedback_text: str | None = Field(None, description="Optional textual feedback")
