from app.errors import (OutdatedVaccineError,
                        NotWearingMaskError,
                        NotVaccinatedError)
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    allowed_friends = 0
    masks_to_buy = 0
    for friend in friends:
        try:
            if cafe.visit_cafe(friend) == f"Welcome to {friend.name}":
                allowed_friends += 1
        except (NotVaccinatedError, OutdatedVaccineError):
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1
    if allowed_friends == len(friends):
        return f"Friends can go to {cafe.name}"
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
