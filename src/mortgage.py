from typing import Optional

import numpy as np

from src.flow import Flow


class MortgageFlow(Flow):

    @classmethod
    def fixed_rate(cls,
                   prepayment: int,
                   number_of_period: int,
                   monthly_payment: int,
                   costs: Optional[Flow] = None
                   ):
        initial_payment = np.array([prepayment * -1])
        monthly_payments = np.full((number_of_period,), monthly_payment * -1)
        payments = np.concatenate(
            [initial_payment,
             monthly_payments]
        )
        mortgage_flow = MortgageFlow(payments)
        assert mortgage_flow.is_negative(include_zero=True), "MortgageFlow should have non-positive payments"
        return mortgage_flow
