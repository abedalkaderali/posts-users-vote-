"""add foreign-key to posts table

Revision ID: 4fc43147db34
Revises: da31737496fe
Create Date: 2024-07-30 04:55:00.471310

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4fc43147db34'
down_revision: Union[str, None] = 'da31737496fe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts",referent_table="users",local_cols=['owner_id'],remote_cols=['u_id'],ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk',table_name="posts")
    op.drop_column('posts','owner_id')
    pass
