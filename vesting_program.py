#!/usr/bin/python3

'''
Calculate vested shares for employees of a company
'''

import argparse
from modules.validator import Validate
from modules.default import DefaultVestedShare
from modules.helper import File, TotalShare, PreciseNumber

class VestingProgram:
    def __init__(self, filename, target_date, precision):
        self.filename = filename
        self.target_date = target_date
        self.precision = precision

        # Test if input parameters are valid
        validate = Validate()
        validate.precision(self.precision)

        if not validate.check_date(self.target_date):
            raise ValueError('Invalid input date')

        f = File()
        self.vesting_data, self.file = f.get_csv_data(self.filename)


    def parse_calculated_vested_shares(self, vested_shares):
        sorted_shares = sorted(vested_shares.keys())
        vested_share_data = []

        for share in sorted_shares:
            employee_id = vested_shares[share]['employee_id']
            name = vested_shares[share]['name']
            award_id = vested_shares[share]['award_id']
            quantity = format(
                vested_shares[share]['quantity'], f'.{self.precision}f')

            # Assuming vested shares cannot be negative
            quantity = quantity if float(quantity) > 0 else 0
            vested_share_data.append(
                (f'{employee_id},{name},{award_id},{quantity}'))

        return vested_share_data


    def main(self):
        # Instantiate helper classes
        f = File()
        precise_number = PreciseNumber()
        total_share = TotalShare()

        vested_shares = {}

        for i, row in enumerate(self.vesting_data):
            if not (row):
                # skip empty lines
                continue

            vesting_event = row[0].strip()
            employee_id = row[1].strip()
            name = row[2].strip()
            award_id = row[3].strip()
            awarded_date = row[4].strip()
            quantity = row[5].strip()

            validate_row = Validate()
            row_valid = validate_row.vesting_events(
                vesting_event, awarded_date, quantity)

            if row_valid:
                if (employee_id, award_id) not in vested_shares:
                    default_share = DefaultVestedShare()
                    vested_shares[(employee_id, award_id)] = default_share.get_values(
                        employee_id, name, award_id)

                if awarded_date <= self.target_date:
                    current_total = vested_shares[(
                        employee_id, award_id)]['quantity']
                    vested_shares[(employee_id, award_id)]['quantity'] = total_share.calulate_vested_shares(
                        vesting_event, current_total, precise_number.get_precise_number(quantity, self.precision))

            else:
                f.close_file(self.file)
                return (f'Invalid input row at line {i+1}')

        f.close_file(self.file)
        return self.parse_calculated_vested_shares(vested_shares)


# entry point for the script
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='This script is going output vested shares for each employee.'
                                     )

    parser.add_argument('filename', type=str, help='csv filename with path')

    parser.add_argument('target_date', type=str,
                        help='Total number of shares vested before this date')

    parser.add_argument('precision', default=0, nargs='?',
                        type=int, help='Optional. Digits of precision to recognize from input csv')

    args = parser.parse_args()

    FILENAME: str = args.filename
    TARGET_DATE: str = args.target_date
    PRECISION: int = args.precision

    vesting_program = VestingProgram(FILENAME, TARGET_DATE, PRECISION)
    vested_share_data = vesting_program.main()

    if vested_share_data is not None and type(vested_share_data) == list:
        for data in vested_share_data:
            print(data)
    else:
        print (vested_share_data)

    # write to output.csv in tests folder
    # f = File()
    # f.write_data_to_csv(vested_share_data)
