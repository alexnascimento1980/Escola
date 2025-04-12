from rest_framework.throttling import AnonRateThrottle
from rest_framework.throttling import UserRateThrottle


class MatriculaAnonRateThrottle(AnonRateThrottle):
    rate ='5/day'