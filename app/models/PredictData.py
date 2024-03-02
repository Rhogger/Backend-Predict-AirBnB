from pydantic import BaseModel


class PredictData(BaseModel):
    neighbourhood_cleansed: str
    property_type: str
    room_type: str
    accommodates: int
    bathrooms: int
    bedrooms: int
    beds: int
