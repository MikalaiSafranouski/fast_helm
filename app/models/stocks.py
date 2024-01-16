from sqlalchemy import ForeignKey, func, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.database import Base
from uuid import UUID


class Ticker(Base):
    """Ticker Model"""
    __tablename__ = "ticker"

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=func.now())
    updated_at: Mapped[datetime] = mapped_column(onupdate=func.utc_timestamp())

    stocks: Mapped["Stock"] = relationship(back_populates="ticker")

class Company(Base):
    """Ticker Model"""
    __tablename__ = "company"

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    industry: Mapped[str | None]
    website: Mapped[str | None]

    created_at: Mapped[datetime] = mapped_column(default=func.now())
    updated_at: Mapped[datetime] = mapped_column(onupdate=func.utc_timestamp())

    stocks: Mapped["Stock"] = relationship(back_populates="company")


class Stock(Base):
    """1"""
    __tablename__ = "stock"

    id: Mapped[UUID] = mapped_column(primary_key=True)

    open = mapped_column(DECIMAL, nullable=False)
    previous_close = mapped_column(DECIMAL, nullable=False)
    dayLow = mapped_column(DECIMAL, nullable=False)
    dayHigh = mapped_column(DECIMAL, nullable=False)
    currentPrice = mapped_column(DECIMAL, nullable=False)

    created_at: Mapped[datetime] = mapped_column(default=func.now())
    updated_at: Mapped[datetime] = mapped_column(onupdate=func.utc_timestamp())


    ticker_id = mapped_column(ForeignKey("ticker.id"))
    ticker: Mapped["Ticker"] = relationship(back_populates="stocks")

    company_id = mapped_column(ForeignKey("company.id"))
    company: Mapped["Company"] = relationship(back_populates="stocks")
