"""Renaming students to scholars

Revision ID: 3c1e290cb322
Revises: 791279dd0760
Create Date: 2024-07-20 15:54:47.426753

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c1e290cb322'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
