import asyncio
import easypost_aiohttp as easypost
easypost.api_key = 'cueqNZUb3ldeWTNX7MU3Mel8UXtaAMUi'

@asyncio.coroutine
def test():
    report = yield from easypost.Report.create(
        start_date="2012-12-01",
        end_date="2013-01-01",
        type="shipment"
    )
    print(report.id)

    report1 = yield from easypost.Report.retrieve(report.id)

    print(report1.id)

    report2 = yield from easypost.Report.create(
        start_date="2013-12-02",
        end_date="2014-01-01",
        type="shipment"
    )

    print(report2)

    reports3 = yield from easypost.Report.all(type="shipment")

    print(reports3)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test())
