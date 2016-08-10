import asyncio
import easypost_aiohttp as easypost
easypost.api_key = 'cueqNZUb3ldeWTNX7MU3Mel8UXtaAMUi'

loop = asyncio.get_event_loop()

def test():

    # retrieve a shipment by tracking_code
    shipment = yield from easypost.Shipment.retrieve("LN123456789US")

    print(shipment.id)

    yield from shipment.refresh()

    print(shipment.id)

    print((yield from shipment.label(file_format='PDF')))


loop.run_until_complete(test())