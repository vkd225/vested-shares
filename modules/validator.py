from datetime import datetime

VALID_VESTING_EVENTS = ['VEST', 'CANCEL']


class Validate:
    def precision(self, p):
        '''
        Check if the given precision point is valid precision point or not.

        Args:
          param1: precision point

        Returns:
          Raises valueerror if precision point is not between 0 and 6.
        '''

        if p < 0 or p > 6:
            raise ValueError('Precision should be between 0 and 6')


    def check_date(self, date_string):
        '''
        Check if the given string is a valid date or not.

        Args:
          param1: input date

        Returns:
          Boolean value. True if input string is a valid date.
        '''

        try:
            datetime.strptime(date_string, '%Y-%m-%d')
            return True
        except Exception as e:
            print(
                f'It should be YYYY-MM-DD, got {date_string}. {e}')

            return False

    def vesting_events(self, vesting_event, awarded_date, quantity):
        '''
        Input validation. Validate a given input row.

        Args:
          param1: vesting_event, it can be VEST or CANCEL
          param2: date on which the share was awarded
          param3: quantity of the awarded share

        Returns:
          Boolean. True if all the row values are valid inputs.
        '''

        valid_vesting_event = True if vesting_event.upper() in VALID_VESTING_EVENTS else False
        valid_date = self.check_date(awarded_date)
        valid_quantity = True if float(quantity) >= 0 else False

        if valid_vesting_event and valid_quantity and valid_date:
            return True
