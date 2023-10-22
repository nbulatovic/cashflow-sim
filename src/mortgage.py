import numpy as np

from src.flow import Flow


class MortgageFlow(Flow):
    @classmethod
    def fixed_rate(cls,
                   prepayment: int,
                   number_of_period: int,
                   monthly_payment: int
                   ):
        initial_payment = np.array([prepayment * -1])
        monthly_payments = np.full((number_of_period,), monthly_payment * -1)
        payments = np.concatenate(
            [initial_payment,
             monthly_payments]
        )
        assert np.all(payments <= 0), "Mortgage cashflow should be non-positive trough the lifetime"
        return MortgageFlow(payments)
