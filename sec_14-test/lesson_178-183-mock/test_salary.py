import unittest
from unittest.mock import MagicMock
from unittest import mock

import salary


class TestSalary(unittest.TestCase):
    def test_calculation_salary(self):
        s = salary.Salary(year=2017)
        s.bonus_api.bonus_price = MagicMock(return_value=1)
        self.assertEqual(s.calcuration_salary(), 101)

        # 処理内で関数がコールされたか
        s.bonus_api.bonus_price.assert_called()
        # 処理内で関数が1回だけコールされたか
        s.bonus_api.bonus_price.assert_called_once()
        # 処理内で関数が指定したパラメータでコールされたか
        s.bonus_api.bonus_price.assert_called_with(year=2017)
        # 処理内で関数が1回だけ指定したパラメータでコールされたか
        s.bonus_api.bonus_price.assert_called_once_with(year=2017)
        # 処理内で関数がコールされた回数
        self.assertEqual(s.bonus_api.bonus_price.call_count, 1)

    def test_calculation_no_salary(self):
        s = salary.Salary(year=2050)
        s.bonus_api.bonus_price = MagicMock(return_value=0)
        self.assertEqual(s.calcuration_salary(), 100)
        # 処理内で関数がコールされていないか
        s.bonus_api.bonus_price.assert_not_called()

    @mock.patch('salary.ThirdPartyBounusRestApi.bonus_price')
    def test_calculation_salary_patch(self, mock_bonus):
        mock_bonus.return_value = 1

        s = salary.Salary(year=2017)
        salary_price = s.calcuration_salary()

        self.assertEqual(salary_price, 101)
        mock_bonus.assert_called()

    def test_calculation_salary_patch_with(self):
        # withステートメントにすればテスト内でも限られた部分のみモックを使用することができる
        with mock.patch('salary.ThirdPartyBounusRestApi.bonus_price') as mock_bonus:
            mock_bonus.return_value = 1

            s = salary.Salary(year=2017)
            salary_price = s.calcuration_salary()

            self.assertEqual(salary_price, 101)
            mock_bonus.assert_called()

    # patcherにすることでテストクラス全体でモックが使用できるようになる
    def setUp(self):
        self.patcher = mock.patch('salary.ThirdPartyBounusRestApi.bonus_price')
        self.mock_bonus = self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_calculation_salary_patcher(self):
        self.mock_bonus.return_value = 1

        s = salary.Salary(year=2017)
        salary_price = s.calcuration_salary()

        self.assertEqual(salary_price, 101)
        self.mock_bonus.assert_called()


if __name__ == '__main__':
    unittest.main()