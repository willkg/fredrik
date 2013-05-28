import os
import shutil
from tempfile import mkdtemp
from unittest import TestCase

from nose.tools import eq_

from fredrik.cmdline import clean_project_module, cmdline_handler


class TestFredrikCmd(TestCase):
    def setUp(self):
        super(TestFredrikCmd, self).setUp()
        self.tempd = mkdtemp(prefix='fredrik')
        self._oldcwd = os.getcwd()

    def tearDown(self):
        super(TestFredrikCmd, self).tearDown()
        if os.path.exists(self.tempd):
            shutil.rmtree(self.tempd)
        os.chdir(self._oldcwd)

    def test_create(self):
        """'fredrik-cmd create' should create project directories"""
        os.chdir(self.tempd)
        cmdline_handler('fredrik-cmd', ['create', '--noinput', 'foo'])
        assert os.path.exists(os.path.join(self.tempd, 'foo'))


class TestUtilities(TestCase):
    def test_clean_project_module(self):
        """clean_project_module should generate valid Python module names"""
        tests = [
            ('foo', 'foo'),
            ('Foo', 'foo'),
            ('Foo Foo', 'foofoo'),
            ('FOO FOO', 'foofoo'),
            ('ou812', 'ou812'),
            ('8675309', 'eight675309'),
            ('asdf!@#$%^&*()_+', 'asdf'),
            ('asdf\xde\xb4', 'asdf')
        ]

        for text, expected in tests:
            eq_(clean_project_module(text), expected)
