"""Renaming students to scholars

Revision ID: 78920c5e2f82
Revises: 791279dd0760
Create Date: 2025-05-25 17:37:05.737890

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78920c5e2f82'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')
    
def downgrade() -> None:
    op.rename_table('scholars', 'students')
