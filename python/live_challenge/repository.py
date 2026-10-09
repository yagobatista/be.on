from threading import Lock

from .models import GenericRequest, GenericResponse


class InMemoryRepository:
    """Replaceable persistence boundary for the exercise."""

    def __init__(self) -> None:
        self._items: list[GenericResponse] = []
        self._lock = Lock()

    def create(self, request: GenericRequest) -> GenericResponse:
        with self._lock:
            item = GenericResponse(id=len(self._items) + 1, data=request.data)
            self._items.append(item)
            return item
