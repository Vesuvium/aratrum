Aratrum
#######
|Pypi| |Build Status| |Code Climate|

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


.. |Build Status| image:: https://img.shields.io/travis/Vesuvium/aratrum.svg?maxAge=3600&style=flat-square
   :target: https://travis-ci.org/Vesuvium/aratrum
.. |Pypi| image:: https://img.shields.io/pypi/v/aratrum.svg?maxAge=3600&style=flat-square
   :target: https://pypi.python.org/pypi/efesto
.. |Code Climate| image:: https://img.shields.io/codeclimate/github/Vesuvium/aratrum.svg?maxAge=3600&style=flat-square
   :target: https://codeclimate.com/github/Vesuvium/aratrum
