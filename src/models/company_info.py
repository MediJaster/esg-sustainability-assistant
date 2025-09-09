from pydantic import BaseModel


class CompanyInfo(BaseModel):
    """
    Company information for ESG analysis.

    Parameters
    ----------
    name : str
        Name of the company.
    industry_sector : str
        Industry sector of the company.

    Returns
    -------
    CompanyInfo
        Instance of company information.

    Examples
    --------
    >>> CompanyInfo(name="TestCo", industry_sector="Tech")
    CompanyInfo(name='TestCo', industry_sector='Tech')

    Notes
    -----
    All fields are required.
    """

    name: str
    industry_sector: str
