from typing import Optional

import numpy as np

from src.flow import Flow


class MortgageFlow(Flow):
    @classmethod
    def from_flow(cls, flow: Flow):
        return MortgageFlow.merge_all([flow])

    @classmethod
    def fixed_rate(cls,
                   prepayment: int,
                   number_of_period: int,
                   monthly_payment: int,
                   costs: Optional[Flow] = None
                   ):
        cost_flow = costs if costs else Flow.empty()

        initial_payment_flow = Flow([prepayment * -1])

        first_month_payment = np.array([0])
        rest_month_payment = np.full((number_of_period,), monthly_payment * -1)
        monthly_payments = np.concatenate([first_month_payment, rest_month_payment])
        monthly_payments_flow = Flow(monthly_payments)

        payments = [
            monthly_payments_flow,
            initial_payment_flow,
            cost_flow
        ]
        mortgage_flow = MortgageFlow.merge_all(payments)
        assert mortgage_flow.is_negative(include_zero=True), "MortgageFlow should have non-positive payments"
        return mortgage_flow
