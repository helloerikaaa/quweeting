from numpy import dtype
import torch


class Dataset:

    def read_data(self, dataset):
        labels = dataset['target'].unique().tolist()
        sentences = dataset['text'].tolist()

        return torch.as_tensor(labels, dtype=torch.float32), sentences
