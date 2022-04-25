from decimal import Decimal
from typing import List, Optional


def calculate(
    current_timestamp: Decimal, last_timestamp: Optional[Decimal]
) -> Decimal:
    """Calculate the tempo based on the last timestamp and the current one."""
    if not last_timestamp:
        return Decimal('60')
    elapsed = current_timestamp - last_timestamp
    return Decimal('60') / elapsed if elapsed != 0 else Decimal('60')
