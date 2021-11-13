import pandas as pd
from consts.paths import Paths

def split(dataset):
    print(f'Original dataset shape: {dataset.shape}')
    train_df = dataset.sample(frac=0.8)
    print(f'Train dataset shape: {train_df.shape}')
    train_df.to_csv(Paths.train_dataset_path, index=False)

    test_df = dataset.drop(train_df.index)
    test_df = test_df.sample(frac=0.5)
    print(f'Test dataset shape: {test_df.shape}')
    test_df.to_csv(Paths.test_dataset_path, index=False)

    val_df = dataset.drop(train_df.index)
    val_df = val_df.drop(test_df.index)
    print(f'Validation dataset shape: {val_df.shape}')
    val_df.to_csv(Paths.val_dataset_path, index=False)



if __name__ == "__main__":
    data = pd.read_csv(Paths.dataset_path)
    split(data)