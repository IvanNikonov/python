class Utils:

    @staticmethod
    def combine_lists(keys, values):
        return dict({keys[i]: values[i] for i in range(len(values))})