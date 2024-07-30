"""add user table

Revision ID: da31737496fe
Revises: e062f9c9852e
Create Date: 2024-07-30 04:46:21.760513

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'da31737496fe'
down_revision: Union[str, None] = 'e062f9c9852e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('users',
                    sa.Column('u_id', sa.Integer(), nullable=False),
                    sa.Column('u_email', sa.String(), nullable=False),
                    sa.Column('u_password', sa.String(), nullable=False),
                    sa.Column('u_created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('u_id'),
                    sa.UniqueConstraint('u_email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass