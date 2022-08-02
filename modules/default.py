class DefaultVestedShare:
    '''
    A default vested share class for an employee
    '''

    def set_default_values(self, employee_id, name, award_id):
        '''
        Get default values for an employee's vested share.

        Args:
          param1: employee id
          param2: name of the employee
          param3: award_id of the vested share

        Returns:
          Default values in a dictionary.
        '''

        return {
            'employee_id': employee_id,
            'name': name,
            'award_id': award_id,
            'quantity': 0
        }
