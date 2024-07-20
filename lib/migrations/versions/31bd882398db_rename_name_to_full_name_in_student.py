"""rename name to full_name in scholars

Revision ID: 31bd882398db
Revises: 3c1e290cb322
Create Date: <date>
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '31bd882398db'
down_revision = '3c1e290cb322'
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.alter_column('scholars', 'name', new_column_name='full_name')

def downgrade() -> None:
    op.alter_column('scholars', 'full_name', new_column_name='name')
