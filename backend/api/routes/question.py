import aiohttp

from fastapi import status, APIRouter, Depends

from backend.models.db import QuestionModel
from backend.models.schemas import QuestionInCreateSchema, QuestionOutResponse, QuestionInRequest
from backend.db.crud import QuestionCRUDRepository
from backend.utils.exceptions.http.exc_400 import http_400_question_request_details
from backend.requests import QuestionWebSession

from ..dependencies.repository import get_repository


router = APIRouter(prefix="/question", tags=["question"])


async def http_request_get_new_question_and_check_exists_data_in_the_db(
    session: aiohttp.ClientSession,
    question_repo: QuestionCRUDRepository,
) -> QuestionInCreateSchema:
    while True:
        async with session.get('https://jservice.io/api/random?count=1') as resp:
            response_json = await resp.json()
            count_obj = len(response_json)

            if count_obj != 1:  # check count data in the response
                raise await http_400_question_request_details()
            question = QuestionInCreateSchema(**response_json[0])

            # check exists obj by question_id
            if not await question_repo.check_object_exists(question_id=question.question_id):
                return question


@router.post(
    path="",
    status_code=status.HTTP_200_OK,
)
async def create_question(
    body: QuestionInRequest,  # pylint: disable=unused-argument
    question_repo: QuestionCRUDRepository = Depends(get_repository(repo_type=QuestionCRUDRepository)),
):

    last_question: QuestionModel = await question_repo.get_last_question()

    response = {} if last_question is None else QuestionOutResponse(
        id=last_question.id,
        question_id=last_question.question_id,
        text=last_question.text,
        answer=last_question.answer,
        created_at=last_question.created_at,
        updated_at=last_question.updated_at,
    ).dict()

    question_web_session: QuestionWebSession = QuestionWebSession()

    question: QuestionInCreateSchema = await question_web_session.create_session(
        func=http_request_get_new_question_and_check_exists_data_in_the_db,
        question_repo=question_repo
    )

    await question_repo.create_question(question=question)

    return response
