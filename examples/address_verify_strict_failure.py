import asyncio
import easypost_aiohttp as easypost
easypost.api_key = 'cueqNZUb3ldeWTNX7MU3Mel8UXtaAMUi'

loop = asyncio.get_event_loop()

def test():
    try:
        # this request will raise an error
        address = yield from easypost.Address.create(
            verify_strict=["delivery"],
            street1="UNDELIEVRABLE ST",
            city="San Francisco",
            state="CA",
            zip="94105",
            country="US",
            company="EasyPost",
            phone="415-456-7890"
        )
    except easypost.Error as e:
        print(e.http_body)

loop.run_until_complete(test())
