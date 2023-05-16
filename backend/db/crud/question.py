import sqlalchemy

from backend.models.db.question import QuestionModel
from backend.models.schemas.question import QuestionInCreateSchema

from .base import BaseCRUDRepository


__all__ = ["QuestionCRUDRepository"]


class QuestionCRUDRepository(BaseCRUDRepository):

    async def create_question(self, question: QuestionInCreateSchema) -> QuestionModel:
        new_question: QuestionModel = QuestionModel(
            question_id=question.question_id,
            text=question.text,
            answer=question.answer
        )

        self.async_session.add(new_question)

        await self.async_session.commit()
        await self.async_session.refresh(instance=new_question)

        return new_question

    async def get_last_question(self) -> QuestionModel:
        stmt = sqlalchemy.select(QuestionModel).order_by(QuestionModel.id.desc())
        query = await self.async_session.execute(statement=stmt)

        # stmt = sqlalchemy.select(QuestionModel).order_by(sqlalchemy.desc(QuestionModel.id))
        # query = await self.async_session.execute(statement=stmt)

        return query.scalar()

    async def check_object_exists(self, question_id: int) -> bool:
        stmt = sqlalchemy.select(sqlalchemy.exists().where(QuestionModel.question_id == question_id))
        query = await self.async_session.execute(statement=stmt)

        return query.scalar()
