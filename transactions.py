from typing import Any, Mapping

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, selectinload, selectin_polymorphic

from base import Base
from shop import Order


class Offer(Base):
    __tablename__ = 'offer'

    class LoadOptions:
        @classmethod
        def load_options(cls):
            return [selectin_polymorphic(Offer, [Shop_Offer, Other_Offer])]

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column()

    __mapper_args__: Mapping[str, Any] = {"polymorphic_on": type, "polymorphic_abstract": True}


class Shop_Offer(Offer):
    __mapper_args__: Mapping[str, Any] = {"polymorphic_identity": "shop"}
    order_id: Mapped[int] = mapped_column(ForeignKey(Order.id))

class Other_Offer(Offer):
    __mapper_args__: Mapping[str, Any] = {"polymorphic_identity": "other"}
    other_id: Mapped[int] = mapped_column()


class Transaction(Base):
    __tablename__ = 'transaction'

    class LoadOptions:
        @classmethod
        def load_options(cls):
            return (
                selectinload(Transaction.offer).options(*Shop_Offer.LoadOptions.load_options()),
            )

    id: Mapped[int] = mapped_column(primary_key=True)
    offer_id: Mapped[int] = mapped_column(ForeignKey(Offer.id))
    offer: Mapped[Offer] = relationship()