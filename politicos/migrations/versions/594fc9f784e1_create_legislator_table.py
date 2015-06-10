"""create legislator table

Revision ID: 594fc9f784e1
Revises: 3ba5c639daba
Create Date: 2015-06-09 22:41:37.358193

"""

# revision identifiers, used by Alembic.
revision = '594fc9f784e1'
down_revision = '3ba5c639daba'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'legislator',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('picture', sa.String(2048), nullable=True),
        sa.Column('website', sa.String(2048), nullable=True),
        sa.Column('email', sa.String(2048), nullable=True),
        sa.Column('gender', sa.String(1), nullable=True),
        sa.Column('date_of_birth', sa.Date, nullable=True),
        sa.Column('about', sa.Text(), nullable=True),
    )


def downgrade():
    op.drop_table('legislator')
