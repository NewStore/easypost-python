import asyncio
import time

import easypost_aiohttp as easypost
easypost.api_key = 'cueqNZUb3ldeWTNX7MU3Mel8UXtaAMUi'

loop = asyncio.get_event_loop()

def test():
    shipments = [
        {
            'to_address': {
                'name': "Customer",
                'street1': "8308 Fenway Rd",
                'city': "Bethesda",
                'state': "MD",
                'zip': "20817",
                'country': "US"
            },
            'from_address': {
                'name': "Sawyer Bateman",
                'company': "EasyPost",
                'street1': "164 Townsend St",
                'city': "San Francisco",
                'state': "CA",
                'zip': "94107",
                'phone': "415-456-7890"
            },
            'parcel': {
                'weight': 21.2
            },
            'carrier': "UPS",
            'service': "NextDayAir"
        }, {
            'to_address': {
                'name': "Customer",
                'street1': "8308 Fenway Rd",
                'city': "Bethesda",
                'state': "MD",
                'zip': "20817",
                'country': "US"
            },
            'from_address': {
                'name': "Sawyer Bateman",
                'company': "EasyPost",
                'street1': "164 Townsend St",
                'city': "San Francisco",
                'state': "CA",
                'zip': "94107",
                'phone': "415-456-7890"
            },
            'parcel': {
                'weight': 21.2
            },
            'carrier': "UPS",
            'service': "NextDayAir"
        }
    ]

    batch = yield from easypost.Batch.create_and_buy(shipments=shipments)
    while batch.state in ("creating", "queued_for_purchase", "purchasing"):
        print(batch.state)
        yield from asyncio.sleep(1)
        yield from batch.refresh()

    # Insure the shipments after purchase
    if batch.state == "purchased":
        for shipment in batch.shipments:
            yield from shipment.insure(amount=100)

    pickup = yield from easypost.Pickup.create(
        address={
            'name': "Sawyer Bateman",
            'company': "EasyPost",
            'street1': "164 Townsend St",
            'city': "San Francisco",
            'state': "CA",
            'zip': "94107",
            'phone': "415-456-7890"
        },
        batch=batch,
        reference="internal_id_1234",
        min_datetime=time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()),
        max_datetime=time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()),  # this should be later than min
        is_account_address=True,
        instructions="Special pickup instructions"
    )
    yield from pickup.buy(carrier="UPS", service="Same-day Pickup")  # rates in pickup.pickup_rates

    print(pickup.confirmation)

loop.run_until_complete(test())
