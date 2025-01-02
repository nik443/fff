from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr

from app.utils.case_converter import camel_to_snake_case


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> cls:
        return f"{camel_to_snake_case(cls.__name__)}s"

    id: Mapped[int] = mapped_column(primary_key=True)


