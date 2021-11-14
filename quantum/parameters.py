import torch
import tensornetwork as tn
from sympy import default_sort_key


class Parameters:

    def make_pred_fn(self, circuits):
        parameters = sorted(
            {s for circ in circuits for s in circ.free_symbols},
            key=default_sort_key)

        def predict(params):
            return torch.stack(
                [c.lambdify(*parameters)(*params).eval(contractor=tn.contractors.auto).array
                 for c in circuits])
        return predict
