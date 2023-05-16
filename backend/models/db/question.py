import sqlalchemy

from sqlalchemy.orm import Mapped as SQLAlchemyMapped, mapped_column as column

from backend.db.table import Base


__all__ = ["QuestionModel"]


class QuestionModel(Base):
    __tablename__ = "question"

    question_id: SQLAlchemyMapped[str] = column(sqlalchemy.Integer, nullable=False)
    text: SQLAlchemyMapped[str] = column(sqlalchemy.Text, nullable=False)
    answer: SQLAlchemyMapped[str] = column(sqlalchemy.Text, nullable=False)

    mapper_args = {"eager_defaults": True}
