from fastapi import status
from typing import Optional, Any, TypeVar, Generic
from pydantic import BaseModel, field_validator

T = TypeVar("T")

class ApiResponse(BaseModel, Generic[T]):
    message: Optional[str]
    code: Optional[int] = status.HTTP_200_OK
    data: Optional[T] = None