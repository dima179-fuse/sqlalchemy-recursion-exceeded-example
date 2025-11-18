from __future__ import annotations

import typing

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, selectinload

from base import Base

if typing.TYPE_CHECKING:
    from transactions import Transaction

def lazy_transaction() -> type[Transaction]:
    from transactions import Transaction

    return Transaction


class Order(Base):
    __tablename__ = 'order'

    class LoadOptions:
        @classmethod
        def load_options(cls):
            return (
                selectinload(Order.payments).options(*OrderPayment.LoadOptions.load_options()),
            )

    id: Mapped[int] = mapped_column(primary_key=True)

    payments: Mapped[list[OrderPayment]] = relationship(back_populates="order")


class OrderPayment(Base):
    __tablename__ = 'order_payment'

    class LoadOptions:
        @classmethod
        def load_options(cls):
            return (
                selectinload(OrderPayment.transaction).options(*lazy_transaction().LoadOptions.load_options()),
            )

    id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey(Order.id))

    order: Mapped[Order] = relationship(Order, back_populates="payments")
    transaction_id: Mapped[int] = mapped_column(ForeignKey("transaction.id"))
    transaction: Mapped[Transaction] = relationship(lazy_transaction)
