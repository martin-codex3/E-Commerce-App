"""adding table name

Revision ID: 5c58ea432840
Revises: c09a6268d927
Create Date: 2025-12-12 09:56:20.024367

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '5c58ea432840'
down_revision: Union[str, Sequence[str], None] = 'c09a6268d927'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
