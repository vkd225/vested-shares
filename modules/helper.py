'''
Helper classes and methods to manipulate data.
'''

import csv
import math


class File:
    '''
    Class to operate and handle input csv files.
    '''

    def get_csv_data(self, filename):
        '''
        Read a given file and return the csv data.

        Args:
          param1: filepath of the input csv.
            Can enter filename only if the input file exists in the same directory.

        Returns:
          csv data of the input file.
          csv file. Use it later to close the file.
        '''

        try:
            csv_file = open(filename, 'r')
            csv_reader = csv.reader(csv_file, delimiter=',')
            return csv_reader, csv_file

        except:
            raise ValueError(f'{filename} file not found')

    def write_data_to_csv(self, data):
        '''
        Create a csv file and write data.

        Args:
          param1: list of csv data to write to a file

        Returns:
          Newly created csv file named 'output.csv' inside tests folder.
        '''

        for i in range(len(data)):
            data[i] = [data[i]]

        file = open('tests/output.csv', 'w+')

        with file:
            write = csv.writer(file)
            write.writerows(data)

    def close_file(self, file):
        '''
        Close csv file.

        Args:
          param1: filepath of the input csv.

        Returns:
          None
        '''

        file.close()


class TotalShare:
    '''
    Class to change total shares.
    '''

    def calulate_vested_shares(self, vesting_event, prev_total, quantity):
        '''
        Calculate  total quantity based on the vesting event type.

        Args:
          param1: vesting event. can be VEST or CANCEL
          param2: previous total shares vested
          param3: row's quantity

        Returns:
          Total vested shares after including current share quantity.
        '''

        if vesting_event == 'VEST':
            return prev_total + quantity
        elif vesting_event == 'CANCEL':
            return prev_total - quantity


class PreciseNumber:
    '''
    Number with a precsion point.
    '''

    def truncate(self, val, p):
        '''
        Truncate a float without rounding off

        Args:
          param1: floating point number
          param2: precision point

        Returns:
          Truncated floating point number upto the given precsion point
        '''

        return math.floor(val * 10 ** p) / 10 ** p

    def get_precise_number(self, quantity, precision):
        '''
        Convert a string number to a precise value.

        Args:
          param1: input number
          param2: number of precision points

        Returns:
          Float value of the input quantity.
        '''

        try:
            if precision == 0:
                return int(float(quantity))
            else:
                return self.truncate(float(quantity), precision)
        except ValueError as e:
            print(f'Error converting quantity {quantity} into number, {e}')
