import torch
import pandas as pd

from train.train import Train
from consts.paths import Paths
from dataset.dataset import Dataset
from quantum.circuits import Circuit
from quantum.diagrams import Diagram
from quantum.parameters import Parameter
from dataset.preprocess import Preprocess


dataset = pd.read_csv(Paths.train_dataset_path)
dev_dataset = pd.read_csv(Paths.test_dataset_path)

clean_dataset = Preprocess().clean_dataset(dataset)
clean_dev_dataset = Preprocess().clean_dataset(dev_dataset)

train_labels, train_data = Dataset().read_data(clean_dataset)
dev_labels, dev_data = Dataset().read_data(clean_dev_dataset)

train_diagrams = Diagram().create_diagram(train_data)
dev_diagrams = Diagram().create_diagram(dev_data)

train_circuits = Circuit().create_circuit(train_diagrams)
dev_circuits = Circuit().create_circuit(dev_diagrams)

train_pred_fn = Parameter(train_circuits).make_pred_fn()
dev_pred_fn = Parameter(dev_circuits).make_pred_fn()

train_cost_fn, train_costs, train_accs = Train(
).make_cost_fn(train_pred_fn, train_labels)
dev_cost_fn, dev_costs, dev_accs = Train().make_cost_fn(dev_pred_fn, dev_labels)

x0 = [torch.nn.init.uniform_(torch.empty(p.size))
      for p in Parameter(train_circuits).get_parameters()]


result = Train().train(train_cost_fn, x0, niter=20, callback=dev_cost_fn,
                       optimizer_fn=torch.optim.AdamW, lr=0.1)
