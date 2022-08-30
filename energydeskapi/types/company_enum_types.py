from enum import Enum


class CompanyTypeEnum(Enum):
    DOMESTIC = 1   # Mainly used for platform services in conjunction with demand side response
    INDUSTRIAL = 2
    UTILITY = 3
    GRID_OWNER = 4
    OPERATOR = 5
    BANK = 6
    TRADING_COMPANY = 7
    SERVICE_COMPANY = 8
    OTHER_TYPE = 9


class UserRoleEnum(Enum):
    ADMIN = 1
    TRADER = 2
    RISKMANAGER =3
    STAKEHOLDER = 4