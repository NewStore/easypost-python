import asyncio
import easypost_aiohttp as easypost
easypost.api_key = 'cueqNZUb3ldeWTNX7MU3Mel8UXtaAMUi'

loop = asyncio.get_event_loop()

def test():
    # unicode
    state = u'DELEGACI\xf3N BENITO JU\xe1REZ'

    address = yield from easypost.Address.create(state=state)

    assert address.state == state

    # bytestring
    address = yield from easypost.Address.create(state=state.encode('utf-8'))
    assert address.state == state

loop.run_until_complete(test())
