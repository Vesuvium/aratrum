# -*- coding: utf-8 -*-
import ujson


class Aratrum:
    """
    Provides read/write access to the configuration.
    """

    def __init__(self, filename='config.json'):
        self.config = None
        self.filename = filename

    def get(self):
        """
        Loads the configuration and returns it as a dictionary
        """
        with open(self.filename, 'r') as f:
            self.config = ujson.load(f)
        return self.config

    def defaults(self):
        """
        Sets the configuration to default values
        """
        self.config = {}
        return self.config

    def set(self, option, value):
        """
        Sets an option to a value.
        """
        if self.config is None:
            self.config = {}
        self.config[option] = value

    def delete(self, option):
        """
        Deletes an option if exists
        """
        if self.config is not None:
            if option in self.config:
                del self.config[option]

    def save(self):
        """
        Saves the configuration
        """
        with open(self.filename, 'w') as f:
            ujson.dump(self.config, f, indent=4)
