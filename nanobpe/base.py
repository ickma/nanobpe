
import json


class BaseTokenizer:
    def __init__(self, ):

        self.vocab = {}

    def train(self, text, round=1024):
        ids = list(text.encode())
        self.vocab = {i: i for i in set(ids)}
        self.ids_to_chars = {i: chr(i) for i in self.vocab}

        for i in range(round):
            counter = {}
            for id_left, id_right in zip(ids[:-1], ids[1:]):
                counter[(id_left, id_right)] = counter.get(
                    (id_left, id_right), 0)+1
            the_most_common = max(counter, key=counter.get)
            if counter[the_most_common] == 1:
                print('early stopping')
                break

            new_idx = max(self.vocab.keys())+1
            self.vocab[new_idx] = the_most_common
            self.ids_to_chars[new_idx] = f'{self.ids_to_chars[the_most_common[0]]}{self.ids_to_chars[the_most_common[1]]}'

            # merge the most common pair
            new_ids = []
            i = 0
            while i < len(ids):
                if i < len(ids)-1 and (ids[i], ids[i+1]) == the_most_common:
                    new_ids.append(new_idx)
                    i += 2
                else:
                    new_ids.append(ids[i])
                    i += 1
            ids = new_ids

    def encode(self, text):
        ids = list(text.encode())

        if len(ids) < 2:
            return ids

        for idx in sorted(self.vocab.keys()):
            new_ids = []

            v = self.vocab[idx]
            if isinstance(v, tuple):
                i = 0
                while i < len(ids):
                    if i < len(ids)-1 and ids[i] == v[0] and ids[i+1] == v[1]:
                        new_ids.append(idx)
                        i += 2
                    else:
                        new_ids.append(ids[i])
                        i += 1
                ids = new_ids
        return new_ids

    def decode(self, ids):
        return ''.join([self.vocab[id] for id in ids])

    def save(self, path):
        with open(path, 'w') as f:
            json.dump(self.vocab, f)

    def load(self, path):
        with open(path, 'r') as f:
            self.vocab = json.load(f)
