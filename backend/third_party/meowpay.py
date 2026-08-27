"""
MeowPay - Third-party payment processor SDK.

This is a simulated third-party payment library. In a real project,
this would be installed via pip (e.g., `pip install meowpay-sdk`).

API Docs: https://docs.meowpay.io/v2/charges
"""

import uuid
from datetime import datetime


class MeowPayError(Exception):
    """Raised when MeowPay API returns an error."""

    def __init__(self, code: str, message: str):
        self.code = code
        self.message = message
        super().__init__(f"MeowPay error [{code}]: {message}")


class MeowPayClient:
    """Client for the MeowPay payment processing API."""

    def __init__(self, api_key: str, merchant_id: str):
        self.api_key = api_key
        self.merchant_id = merchant_id
        self._base_url = "https://api.meowpay.io/v2"

    def create_charge(self, amount: float, currency: str, description: str) -> dict:
        """
        Creates a charge against the customer's payment method.

        In production this would make an HTTP request to MeowPay's API.
        For this demo, it simulates a successful response.
        """
        if amount <= 0:
            raise MeowPayError("invalid_amount", "Amount must be positive")

        # Simulate API response
        return {
            "charge_id": f"ch_{uuid.uuid4().hex[:16]}",
            "merchant_id": self.merchant_id,
            "amount": amount,
            "currency": currency,
            "description": description,
            "status": "succeeded",
            "created_at": datetime.utcnow().isoformat(),
            "api_version": "2024-01-15",
            "internal_trace_id": f"trace_{uuid.uuid4().hex}",
            "risk_score": 0.12,
            "processor_response_code": "00",
            "merchant_secret_ref": self.api_key[:8] + "...",
        }

    def refund_charge(self, charge_id: str) -> dict:
        """Refunds a previously created charge."""
        return {
            "refund_id": f"rf_{uuid.uuid4().hex[:16]}",
            "charge_id": charge_id,
            "status": "refunded",
            "created_at": datetime.utcnow().isoformat(),
        }
