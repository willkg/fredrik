==================
Hacking on Fredrik
==================

This chapter covers hacking on fredrik---not hacking on projects
created with fredrik.


Hack!
=====

Do this:

1. create a `Python virtual environment
   <https://pypi.python.org/pypi/virtualenv>`_
2. (optional) go to https://github.com/willkg/fredrik and fork it
3. get the source code::

       $ git clone git://github.com/willkg/fredrik.git

   (or use your fork)
4. install fredrik for hacking::

       $ python setup.py develop

5. install other dev requirements::

       $ pip install -r requirements-dev.txt


Test!
=====

Tests are located in ``fredrik/tests/``. We use `nose
<https://nose.readthedocs.org/en/latest/>`_.

To run the tests::

    $ nosetests


Document!
=========

Documentation is located in ``docs/``. We use `Sphinx
<http://sphinx-doc.org/>`_.

To build the docs in html::

    $ cd docs
    $ make html
