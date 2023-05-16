from enum import Enum

class DiasSemanaEnum(Enum):
    MONDAY = 'MO'
    TUESDAY = 'TU'
    WEDNESDAY = 'WE'
    THURSDAY = 'TH'
    FRIDAY = 'FR'
    SATURDAY = 'SA'
    SUNDAY = 'SU'

    LABORALES = [MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY]
    NO_LABORALES = [SATURDAY, SUNDAY]