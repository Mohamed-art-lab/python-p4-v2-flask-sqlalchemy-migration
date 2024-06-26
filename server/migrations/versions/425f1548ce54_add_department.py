"""add Department

Revision ID: 425f1548ce54
Revises: 3df9f64a2c8b
Create Date: 2024-04-16 17:34:43.370892

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '425f1548ce54'
down_revision = '3df9f64a2c8b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('departments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('location', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('departments')
    # ### end Alembic commands ###
