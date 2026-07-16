from pydantic import BaseModel, Field


class TransactionRequest(BaseModel):
    amount: float = Field(
        gt=0,
        description="Transaction amount"
    )

    merchant: str = Field(
        min_length=2,
        description="Merchant name"
    )

    country: str = Field(
        min_length=2,
        max_length=2,
        description="Transaction country code"
    )

    transaction_type: str = Field(
        description="Type of transaction"
    )