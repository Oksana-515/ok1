import unittest
from task4 import convert_date_format  # Замініть на ім'я вашого модуля

class TestConvertDateFormat(unittest.TestCase):

    def test_valid_date_conversion(self):
        self.assertEqual(convert_date_format("2024-02-11"), "11-02-2024")
        self.assertEqual(convert_date_format("1999-12-31"), "31-12-1999")
        self.assertEqual(convert_date_format("2000-01-01"), "01-01-2000")

    def test_invalid_dates(self):
        # Неправильні формати
        self.assertEqual(convert_date_format("2024/02/11"), "2024/02/11")
        self.assertEqual(convert_date_format("11-02-2024"), "11-02-2024")
        self.assertEqual(convert_date_format("2024-2-11"), "2024-2-11")  # Пропущений 0
        self.assertEqual(convert_date_format("24-02-11"), "24-02-11")  # Короткий рік

    def test_edge_cases(self):
        self.assertEqual(convert_date_format(""), "")  # Порожній рядок
        self.assertEqual(convert_date_format("not-a-date"), "not-a-date")  # Текст
        self.assertEqual(convert_date_format("2024-02-11T12:00:00"), "2024-02-11T12:00:00")  # Дата з часом

    def test_partial_matches(self):
        self.assertEqual(convert_date_format("2024-02-11extra"), "2024-02-11extra")  # Додатковий текст
        self.assertEqual(convert_date_format("prefix2024-02-11"), "prefix2024-02-11")  # Префікс

    def test_leap_year(self):
        self.assertEqual(convert_date_format("2020-02-29"), "29-02-2020")  # Високосний рік

if __name__ == '__main__':
    unittest.main()