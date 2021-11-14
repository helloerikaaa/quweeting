import torch
import numpy as np


class Train:

    def train(self, func, x0, niter, callback, optimizer_fn, lr):
        x = [t.detach().requires_grad() for t in x0]
        optimizer = optimizer_fn(x, lr=lr)
        for _ in range(niter):
            loss = func(x)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            with torch.no_grad():
                callback(x)

        return x

    def make_cost_fn(self, pred_fn, labels):
        def cost_fn(params, **kwargs):
            costs = []
            accuracies = []
            predictions = pred_fn(params)

            logits = predictions[:, 1] - predictions[:, 0]
            loss_fn = torch.nn.BCEWithLogitsLoss()
            cost = loss_fn(logits, labels)
            costs.append(cost.item())

            with torch.no_grad():
                acc = np.sum((logits > 0) == labels) / len(labels)
                accuracies.append(acc.item())

            return cost
