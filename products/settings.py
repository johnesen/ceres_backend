class CurrencyType:
    USD = "USD"
    KGS = "KGS"
    RUS = "RUS"

    @classmethod
    def choices(cls):
        return (
            (cls.USD, cls.USD),
            (cls.KGS, cls.KGS),
            (cls.RUS, cls.RUS),
        )

    @classmethod
    def all(cls):
        return cls.USD, cls.KGS, cls.RUS

class OrderStatus:
    ON_REVIEW = "ON_REVIEW"
    ON_MY_WAY = "ON_MY_WAY"
    DELIVERED = "DELIVERED"

    @classmethod
    def choices(cls):
        return (
            (cls.ON_REVIEW, cls.ON_REVIEW),
            (cls.ON_MY_WAY, cls.ON_MY_WAY),
            (cls.DELIVERED, cls.DELIVERED),
        )

    @classmethod
    def all(cls):
        return cls.ON_REVIEW, cls.ON_MY_WAY, cls.DELIVERED
