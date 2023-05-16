import typing

from sqlalchemy.ext.asyncio import AsyncSession as SQLAlchemyAsyncSession

from backend.db.database import async_db


async def get_async_session() -> typing.AsyncGenerator[SQLAlchemyAsyncSession, None]:
    try:
        yield async_db.async_session
    except Exception as exc:  # except all errors, pylint: disable=broad-except
        print(exc)
        await async_db.async_session.rollback()
    finally:
        await async_db.async_session.close()
