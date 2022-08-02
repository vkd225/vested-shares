#!/usr/bin/python3

import unittest
from vesting_program import VestingProgram


class TestVestedShare(unittest.TestCase):
    def test_without_precision_input(self):
        '''
        Test csv data with floating point in quantity but with 0 precision input
        '''

        vesting_program = VestingProgram(
            'tests/example_with_precision.csv', '2021-01-01', 0)
        data = vesting_program.main()
        result = ['E001,Alice Smith,ISO-001,1000']

        self.assertEqual(data, result)

    def test_with_vest_events_only(self):
        '''
        Test csv data which has only VEST events
        '''

        vesting_program = VestingProgram(
            'tests/example_with_vest_events_only.csv', '2020-04-01', 0)
        data = vesting_program.main()
        result = [
            'E001,Alice Smith,ISO-001,1000',
            'E001,Alice Smith,ISO-002,800',
            'E002,Bobby Jones,NSO-001,600',
            'E003,Cat Helms,NSO-002,0'
        ]

        self.assertEqual(data, result)

    def test_with_cancel_events(self):
        '''
        Test csv data which also has CANCEL events
        '''

        vesting_program = VestingProgram(
            'tests/example_with_cancel_events.csv', '2021-01-01', 0)
        data = vesting_program.main()
        result = ['E001,Alice Smith,ISO-001,300']

        self.assertEqual(data, result)

    def test_with_precision_input(self):
        '''
        Test csv data with precision = 1 and also have CANCEL events
        '''

        vesting_program = VestingProgram(
            'tests/example_with_precision_and_cancel.csv', '2021-01-01', 1)
        data = vesting_program.main()
        result = ['E001,Alice Smith,ISO-001,299.8',
                  'E002,Bobby Jones,ISO-002,234.0']

        self.assertEqual(data, result)

    def test_outerbound_precision(self):
        '''
        Test error when precision is more than the outerbound i.e. 6
        '''

        filename = 'tests/example_with_precision_and_cancel.csv'
        target_date = '2021-01-01'

        self.assertRaises(ValueError, VestingProgram,
                          filename, target_date, 10)

    def test_negative_precision(self):
        '''
        Test error when precision is less than 0
        '''

        filename = 'tests/example_with_precision_and_cancel.csv'
        target_date = '2021-01-01'

        self.assertRaises(ValueError, VestingProgram,
                          filename, target_date, -1)

    def test_invalid_date(self):
        '''
        Test error when input date is an invalid date
        '''

        filename = 'tests/example_with_precision_and_cancel.csv'
        target_date = '99999-99-99'

        self.assertRaises(ValueError, VestingProgram, filename, target_date, 3)

    def test_invalid_filename(self):
        '''
        Test when the file is not found.
        '''

        filename = 'invalid_filename.csv'
        target_date = '2021-01-01'

        self.assertRaises(TypeError, VestingProgram, filename, target_date, 0)

    def test_with_spaces_and_empty_lines(self):
        '''
        Test csv data with spaces in between and empty lines
        '''

        vesting_program = VestingProgram(
            'tests/example_with_spaces_and_empty_lines.csv', '2021-01-01', 1)
        data = vesting_program.main()
        result = ['E001,Alice Smith,ISO-001,299.8',
                  'E002,Bobby Jones,ISO-002,234.0']

        self.assertEqual(data, result)

    def test_invalid_row_event(self):
        '''
        Test if the event is anything except 'VEST' and 'CANCEL'
        Vesting events are case insensitive
        '''

        vesting_program = VestingProgram(
            'tests/example_with_invalid_row_event.csv', '2021-01-01', 1)
        data = vesting_program.main()

        result = 'Invalid input row at line 1'

        self.assertEqual(data, result)

    def test_invalid_row_date(self):
        '''
        Test the input row date is a valid date
        '''

        vesting_program = VestingProgram(
            'tests/example_with_invalid_row_date.csv', '2021-01-01', 1)
        data = vesting_program.main()

        result = 'Invalid input row at line 1'

        self.assertEqual(data, result)

    def test_random_vesting_order(self):
        '''
        Test the input file with random order and
        output should be sorted by EmployeeID, AwardID
        '''

        vesting_program = VestingProgram(
            'tests/example_with_random_order.csv', '2021-01-01', 2)
        data = vesting_program.main()

        result = ['E001,Alice Smith,ISO-001,799.11',
                  'E001,Alice Smith,ISO-002,800.67',
                  'E002,Bobby Jones,NSO-001,200.00',
                  'E003,Cat Helms,NSO-002,100.00']

        self.assertEqual(data, result)


if __name__ == '__main__':
    unittest.main()
