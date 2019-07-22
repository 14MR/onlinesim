from unittest import TestCase

from onlinesim.account import OnlineSimAccount
from onlinesim.exceptions import OnlineSimResponseException


class TestOnlineSimAccount(TestCase):

    @staticmethod
    def _get_api_key():

        if not hasattr(TestOnlineSimAccount, 'api_key'):

            TestOnlineSimAccount.api_key = input('Enter api key: ')

        return TestOnlineSimAccount.api_key

    def test_initialization(self):

        onlinesim = OnlineSimAccount(self._get_api_key())

        self.assertEqual(onlinesim._api_key, self._get_api_key())
        self.assertIsInstance(onlinesim._api_endpoint, str)

    def test_process_response(self):

        self.assertDictEqual(OnlineSimAccount._process_response({'response': '1', 'key': 'value'}), {'key': 'value'})
        self.assertRaises(OnlineSimResponseException, OnlineSimAccount._process_response, {'response': 'ERROR'})

    def test_request(self):

        response = OnlineSimAccount(self._get_api_key())._request('getBalance')

        self.assertIsInstance(response, dict)
        self.assertIn('balance', response)

        self.assertRaises(OnlineSimResponseException, OnlineSimAccount('')._request, 'getBalance')
        self.assertRaises(OnlineSimResponseException, OnlineSimAccount(self._get_api_key())._request, '')
