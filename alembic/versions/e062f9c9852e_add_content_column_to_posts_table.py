"""add content column to posts table

Revision ID: e062f9c9852e
Revises: 67b066371858
Create Date: 2024-07-30 04:42:15.777314

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e062f9c9852e'
down_revision: Union[str, None] = '67b066371858'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
