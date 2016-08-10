import asyncio
import easypost_aiohttp as easypost
easypost.api_key = 'cueqNZUb3ldeWTNX7MU3Mel8UXtaAMUi'

loop = asyncio.get_event_loop()

def test():
    # this address will not be verified
    address = yield from easypost.Address.create(
        verify=["delivery"],
        street1="UNDELIEVRABLE ST",
        city="San Francisco",
        state="CA",
        zip="94105",
        country="US",
        company="EasyPost",
        phone="415-456-7890"
    )

    print(address.verifications)

loop.run_until_complete(test())
