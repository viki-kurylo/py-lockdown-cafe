import datetime
from app.errors import (OutdatedVaccineError,
                        NotWearingMaskError,
                        NotVaccinatedError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None | str:
        try:
            if visitor["vaccine"]["expiration_date"] < datetime.date.today():
                raise OutdatedVaccineError
            if not visitor["wearing_a_mask"]:
                raise NotWearingMaskError
        except KeyError:
            raise NotVaccinatedError
        else:
            return f"Welcome to {self.name}"
