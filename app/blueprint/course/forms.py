from pydantic import BaseModel, field_validator


class ValidationBase(BaseModel):
    title: str
    description: str

    @field_validator('title')
    def title(cls, v):
        if len(v) > 60:
            raise ValueError("Maximum 60 characters for title")
        return v


def validation_forms(data: dict):
    title = None
    description = None
    release_date = None

    try:
        title = data['title']
        description = data['description']
    except:
        raise ValueError("Key not found")

    ValidationBase(title=title, description=description)
