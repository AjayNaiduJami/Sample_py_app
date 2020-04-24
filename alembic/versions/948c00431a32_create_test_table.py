"""create test table

Revision ID: 948c00431a32
Revises: 
Create Date: 2017-04-12 15:48:24.051314

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '948c00431a32'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'test_table',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('value', sa.String(50), nullable=False)
    )


def downgrade():
    op.drop_table('test_table')
