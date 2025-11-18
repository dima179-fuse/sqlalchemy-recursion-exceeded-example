from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, selectinload, selectin_polymorphic

from base import Base


class Offer(Base):
    __tablename__ = 'offer'

    class LoadOptions:
        @classmethod
        def load_options(cls):
            return []

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column()


class Transaction(Base):
    __tablename__ = 'transaction'

    class LoadOptions:
        @classmethod
        def load_options(cls):
            return (
                selectinload(Transaction.offer),
            )

    id: Mapped[int] = mapped_column(primary_key=True)
    offer_id: Mapped[int] = mapped_column(ForeignKey(Offer.id))
    offer: Mapped[Offer] = relationship()
