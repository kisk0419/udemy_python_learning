import os

import pytest

import calculartion

is_release = False

"""
> pytest -s [display print]
> pytest -rs [display skip reason]
> pytest -v [deiplay detail]

coverage (install)
> pip install pytest-cov pytest-xdist

coverage (test)
> pytest --cov=test_calculation --cov-report term-missing

"""

class TestCal(object):
    @classmethod
    def setup_class(cls):
        print('start')
        cls.cal = calculartion.Cal()
        cls.file_name = "test.txt"

    @classmethod
    def teardown_class(cls):
        print('end')
        del cls.cal


    def setup_method(self, method):
        print(f'test={method.__name__}')
        #self.cal = calculartion.Cal()

    def teardown_method(self, method):
        print(f'cleanup={method.__name__}')
        #del self.cal

    #@pytest.mark.skip(reason='skip!')
    #@pytest.mark.skipif(is_release==True, reason='skip!')
    def test_add_num_and_double(self, request):
        os_name = request.config.getoption('--os-name')
        print(os_name)
        if os_name == 'mac':
            print('ls')
        elif os_name == 'windows':
            print('dir')

        assert self.cal.add_num_and_double(1, 1) == 4

    def test_add_num_and_double_raise(self, csv_file):
        print(csv_file)
        with pytest.raises(ValueError):
            self.cal.add_num_and_double('1', '1')

    def test_save(self, tmpdir):
        self.cal.save(tmpdir, self.file_name)
        test_file_path = os.path.join(tmpdir, self.file_name)
        assert os.path.exists(test_file_path) is True
