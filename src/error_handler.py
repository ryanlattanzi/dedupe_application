

class WrongDFAmountError(Exception):
    def __init__(self):
            self.message = 'Please provide only one DataFrame to dedupe.'
            super().__init__(self.message)

class ServiceNotFoundError(Exception):
    def __init__(self, service_name):
            self.message = 'Service {} is not available. Please choose either get_new_rows or dedupe_single_df.'.format(service_name)
            super().__init__(self.message)