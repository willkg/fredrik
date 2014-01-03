=======
Read me
=======

Command line for generating Flask app scaffolding suitable for
fast-and-furious hack-days.

:Code:          https://github.com/willkg/fredrik/
:Issues:        https://github.com/willkg/fredrik/issues
:License:       BSD 3-clause
:Documentation: http://fredrik.rtfd.org/


Status
======

There are better Flask project templates and this one suffers from poor
decisions.

Ergo, this project is dead for now.


Install
=======

Install it with pip::

    $ pip install fredrik


Install it with pip from git::

    $ pip install https://github.com/willkg/fredrik/zipball/master#egg=fredrik


Install it from source::

    $ git clone git://github.com/willkg/fredrik/
    $ cd fredrik
    $ python setup.py install


Run
===

To create a Flask project using fredrik::

    $ fredrik-cmd create <PROJECTNAME>


That will create the project directory with all the files for the skeleton
with items marked TODO that need to be done.
