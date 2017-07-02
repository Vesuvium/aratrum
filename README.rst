Aratrum
#######

A simple configuration handler that reads a JSON config file and provides
methods to interact with it.

Was it really necessary to make a package for such a simple thing?
Maybe not, but I like the DRYness of it, since almost every app will
need a configuration reader.

Usage
#####

Load a configuration file::

    >>> from Aratrum import Aratrum
    >>> config = Aratrum('config.json')
    >>> options = config.get()
    >>> print(type(options))
    dict


Set a value in the config and save it::

    >>> config = Atratrum('config.json')
    >>> config.get()
    >>> config.config['server'] = 'somewhere'
    >>> config.save()
