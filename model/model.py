from torch import nn


class SpeechToTextModel:

    def __init__(self):
        self.model = None

    def build_model(self):
        """
        Builds and compiles speech to text model

        :return: None
        """
        pass

    def train(self):
        """
        Build and compile model if it hasn't already been, and train

        TODO: some params for data

        :return: None
        """
        if self.model is None:
            self.build_model()

        pass

    def save(self, path):
        """
        Save trained model

        :param path: path to save model to
        :return: None
        """
        pass

    def load(self, path):
        """
        Load model from path

        :param path: path to load model from
        :return: None
        """
        pass
