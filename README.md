## Wrapper for [onlinesim.ru](https://onlinesim.ru) service.

### Installation

    > pip install onlinesim
    
### Usage

#### Importing

    from onlinesim import OnlineSim
    
    onlinesim = OnlineSim('<your api key here>')

#### Simple API usage

Currently wrapper supports all methods specified on [official docs page](https://onlinesim.ru/docs/api/en). But not all of 
specified methods currently supports by server-side, some of them are described with errors or don't work for an unknown
reason. Therefore, over time, I'll remove unworked methods and improve the processing of worked methods.

    > onlinesim.get_num(country = 49, service = 'whatsapp')
    
    < {'tzid': <received tzid>}
    
    > onlinesim.get_state(tzid = <received tzid>, msg_list = 1)
    
    < [{tzid: <received tzid>, ..., number: '+49xxxxxxxx', msg: [{..., ...}], 'response': 'TZ_NUM_ANSWER'}]
    
    > onlinesim.set_operation_ok(tzid = <received tzid>)
    
    < {'tzid': <received tzid>}
    
For more information see [official docs](https://onlinesim.ru/docs/api/en).