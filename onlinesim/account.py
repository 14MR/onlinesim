import requests
from typing import Union

from .exceptions import OnlineSimResponseException


class OnlineSimAccount:

    def __init__(self, api_key, api_endpoint = 'https://onlinesim.ru/api/'):

        self._api_key = api_key
        self._api_endpoint = api_endpoint

    @staticmethod
    def _process_response(response: dict) -> dict:

        if 'response' not in response:

            return response

        else:

            if str(response['response']) == '1':

                response.pop('response')

                return response

            else:

                raise OnlineSimResponseException(response['response'])

    @staticmethod
    def _get_kwargs():

        return locals()

    def _request(self, method, **kwargs) -> Union[dict, list]:

        kwargs['apikey'] = self._api_key

        response = requests.post('{}{}.php'.format(self._api_endpoint, method), data = kwargs)

        response.raise_for_status()

        return self._process_response(response.json())

    def get_numbers_stats(self, country: int = None) -> dict:

        kwargs = locals()
        del kwargs['self']

        return self._request('getNumbersStats', **kwargs)

    def get_state(self, tzid: int = None, message_to_code: int = None,
                  form: int = None, orderby: str = None, msg_list: int = None) -> list:

        kwargs = locals()
        del kwargs['self']

        return self._request('getState', **kwargs)

    def get_operations(self) -> list:

        return self._request('getOperations')

    def get_num(self, service: str = None, simoperator: int = None, region: int = None,
                country: int = None, reject: list = None, extension: int = None, dev_id: int = None) -> dict:

        kwargs = locals()
        del kwargs['self']

        return self._request('getNum', **kwargs)

    def get_num_repeat(self, service: str = None, number: int = None) -> dict:

        kwargs = locals()
        del kwargs['self']

        return self._request('getNumRepeat', **kwargs)

    def get_forward(self, forward_numbers: list = None,
                    service: str = None, region: int = None, reject: list = None) -> dict:

        kwargs = locals()
        del kwargs['self']

        return self._request('getNumRepeat', **kwargs)

    def set_operation_ok(self, tzid: int = None, ban: int = None) -> dict:

        kwargs = locals()
        del kwargs['self']

        return self._request('setOperationOk', **kwargs)

    def set_forward_status_enable(self, tzid: int = None) -> dict:

        kwargs = locals()
        del kwargs['self']

        return self._request('setForwardStatusEnable', **kwargs)

    def set_operation_revise(self, tzid: int = None) -> dict:

        kwargs = locals()
        del kwargs['self']

        return self._request('setOperationRevise', **kwargs)

    def get_balance(self, country: int = None) -> dict:

        kwargs = locals()
        del kwargs['self']

        return self._request('getBalance', **kwargs)

    def get_service(self) -> dict:

        return self._request('getService')

    def get_service_number(self, service: str = None) -> dict:

        kwargs = locals()
        del kwargs['self']

        return self._request('getServiceNumber', **kwargs)

    def forwarding_list(self, id: int = None, page: int = None, sort: str = None) -> dict:

        kwargs = locals()
        del kwargs['self']

        return self._request('forwardingList', **kwargs)

    def forwarding_save(self, id: int = None, minutes: int = None,
                        auto: bool = None, forward_number: int = None, max_minutes: int = None) -> dict:

        kwargs = locals()
        del kwargs['self']

        return self._request('forwardingSave', **kwargs)

    def forwarding_remove(self, id: int = None) -> dict:

        kwargs = locals()
        del kwargs['self']

        return self._request('forwardingRemove', **kwargs)

    def get_call_number_list(self, number: int = None, count: int = None,
                             page: int = None, order_by: str = None) -> dict:

        kwargs = locals()
        del kwargs['self']

        return self._request('getCallNumberList', **kwargs)

    def get_forward_payments_list(self, id: int = None) -> dict:

        kwargs = locals()
        del kwargs['self']

        return self._request('getForwardPaymentsList', **kwargs)

    def get_free_country_list(self) -> dict:

        return self._request('getFreeCountryList')

    def get_free_phone_list(self, country: int = None) -> dict:

        kwargs = locals()
        del kwargs['self']

        return self._request('getFreePhoneList', **kwargs)

    def get_free_message_list(self, phone: str = None, page: int = None) -> dict:

        kwargs = locals()
        del kwargs['self']

        return self._request('getFreeMessageList', **kwargs)
