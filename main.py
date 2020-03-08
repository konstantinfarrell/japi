import asyncio

from routes import app
from settings import (
    app_host,
    app_port,
    app_workers,
)


async def main():
    app.run(host=app_host, port=app_port, workers=app_workers)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
