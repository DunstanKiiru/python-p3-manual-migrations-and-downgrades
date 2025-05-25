"""Renamed name to full_name

Revision ID: fcf3bd0a4100
Revises: 6dee9468372a
Create Date: 2025-05-25 17:53:12.875417

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fcf3bd0a4100'
down_revision = '6dee9468372a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('scholars', 'name', new_column_name='full_name')


def downgrade() -> None:
    op.alter_column('scholars', 'full_name', new_column_name='name')
