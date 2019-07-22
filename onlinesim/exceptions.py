class OnlineSimException(Exception):

    pass


class OnlineSimResponseException(OnlineSimException):

    def __init__(self, response_code):

        self.response_code = response_code

        super().__init__('Server returned error response code: {}.'.format(self.response_code))
