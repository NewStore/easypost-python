import asyncio
import easypost_aiohttp as easypost
easypost.api_key = 'cueqNZUb3ldeWTNX7MU3Mel8UXtaAMUi'

loop = asyncio.get_event_loop()

def test():
    # create address
    address = yield from easypost.Address.create(
        company="EasyPost",
        street1="118 2nd St",
        street2="4th Fl",
        city="San Francisco",
        state="CA",
        zip="94105",
        phone="415-456-7890"
    )

    verified_address = yield from address.verify()

    print(verified_address)

loop.run_until_complete(test())
