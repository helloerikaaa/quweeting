from lambeq.ccg2discocat import DepCCGParser


class Diagram:
    reader = DepCCGParser(possible_root_cats=['S[dcl]'])

    def create_diagram(self, dataset):
        diagrams = self.reader.sentences2diagrams(dataset)

        return diagrams
