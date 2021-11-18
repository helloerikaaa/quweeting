import re
import string
import unicodedata

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

STOPWORDS = stopwords.words('english')
PUNCTUATIONS = str.maketrans({key: None for key in string.punctuation+"¿¡?!"})


class Preprocess:

    def clean_dataset(self, dataset):
        for index, row in dataset.iterrows():
            clean_text = " "
            lower_text = row.text.lower()
            tweet_tokens = [
                word for word in lower_text if word not in STOPWORDS]
            tweet_tokens = [self._preprocess(txt) for txt in tweet_tokens]
            clean_text = clean_text.join(tweet_tokens)
            dataset.at[index, 'text'] = clean_text

            return dataset

    def _preprocess(self, sentence):
        st = sentence.lower()
        # url
        st = re.sub(r"http\S+", "", st)
        # hashtag
        st = re.sub(
            r"\B#([a-z0-9]{2,})(?![~!@#$%^&*()=+_`\-\|\/'\[\]\{\}]|[?.,]*\w)", "", st)
        # @username
        st = re.sub(r"@[a-zA-Z]+", "", st)
        st = st.translate(PUNCTUATIONS)
        st = unicodedata.normalize('NFKD', st).encode(
            'ASCII', 'ignore').decode()
        return st
