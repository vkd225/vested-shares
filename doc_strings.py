#!/usr/bin/python3

from modules.helper import File, TotalShare, PreciseNumber
from modules.validator import Validate
from modules.default import DefaultVestedShare

print ('---- Class: File----')
print(File.__doc__)
print('get_csv_data: ', File.get_csv_data.__doc__)
print('close_file: ', File.close_file.__doc__)
print('write_data_to_csv: ', File.write_data_to_csv.__doc__)

print ('---- Class: TotalShare----')
print(TotalShare.__doc__)
print('calulate_vested_shares: ', TotalShare.calulate_vested_shares.__doc__)

print ('---- Class: PreciseNumber----')
print(PreciseNumber.__doc__)
print('truncate: ', PreciseNumber.truncate.__doc__)
print('get_precise_number: ', PreciseNumber.get_precise_number.__doc__)

print ('---- Class: Validate----')
print(Validate.__doc__)
print('precision: ', Validate.precision.__doc__)
print('check_date: ', Validate.check_date.__doc__)
print('vesting_events: ', Validate.vesting_events.__doc__)

print ('---- Class: DefaultVestedShare----')
print(DefaultVestedShare.__doc__)
print('set_default_values: ', DefaultVestedShare.set_default_values.__doc__)
