from pydantic import BaseModel


class ESGResponse(BaseModel):
    """
    ESG report response returned by the API.

    Parameters
    ----------
    trace_id : str
        Unique identifier for the ESG analysis run.
    final_report : str
        The generated ESG report text.

    Returns
    -------
    ESGResponse
        Instance of ESG report response.

    Examples
    --------
    >>> ESGResponse(trace_id="abc123", final_report="Report text")
    ESGResponse(trace_id='abc123', final_report='Report text')

    Notes
    -----
    All fields are required.
    """

    trace_id: str
    final_report: str
