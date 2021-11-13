import os

PROJECT_PATH = os.path.abspath(os.path.join(__file__, *(os.path.pardir,) * 2))
DATA_PATH = os.path.join(PROJECT_PATH, 'data')


class Paths:
    dataset_path = os.path.join(DATA_PATH, 'tweets.csv')
    train_dataset_path = os.path.join(DATA_PATH, 'train_tweets.csv')
    test_dataset_path = os.path.join(DATA_PATH, 'test_tweets.csv')
    val_dataset_path = os.path.join(DATA_PATH, 'val_tweets.csv')
