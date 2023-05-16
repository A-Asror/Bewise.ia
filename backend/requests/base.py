import typing
import aiohttp

__all__ = ["BaseSession"]


class BaseSession:
    conn_timeout: float | None = None
    session: aiohttp.ClientSession | None = None

    def __int__(self, session: aiohttp.ClientSession | None = None, conn_timeout: float | None = None):
        self.session = conn_timeout
        self.conn_timeout = conn_timeout

    async def create_session(self, func: typing.Callable, *args, **kwargs) -> typing.Any:
        async with aiohttp.ClientSession(
                conn_timeout=self.conn_timeout
        ) as http_session:
            response = await func(session=http_session, *args, **kwargs)
            return response
