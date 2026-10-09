from fastapi import APIRouter, Depends

from .models import AnswerRequest, GenericRequest, GenericResponse, HealthResponse, StructuredAnswer
from .repository import InMemoryRepository
from .service import AnswerService, ExerciseService, HealthService

router = APIRouter()
repository = InMemoryRepository()
exercise_service = ExerciseService(repository)
health_service = HealthService()
answer_service = AnswerService()


def get_exercise_service() -> ExerciseService:
    return exercise_service


def get_health_service() -> HealthService:
    return health_service


def get_answer_service() -> AnswerService:
    return answer_service


@router.get("/health", response_model=HealthResponse)
def health(service: HealthService = Depends(get_health_service)) -> dict[str, str]:
    return service.check()


@router.post("/items", response_model=GenericResponse, status_code=201)
def create_item(
    request: GenericRequest,
    service: ExerciseService = Depends(get_exercise_service),
) -> GenericResponse:
    return service.create_item(request)


@router.post("/answer", response_model=StructuredAnswer)
async def answer(
    request: AnswerRequest,
    service: AnswerService = Depends(get_answer_service),
) -> StructuredAnswer:
    return await service.answer(request)
