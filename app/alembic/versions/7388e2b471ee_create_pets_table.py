"""create pets table

Revision ID: 7388e2b471ee
Revises: 
Create Date: 2023-04-24 18:26:32.535969

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7388e2b471ee'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Pet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Pet')
    # ### end Alembic commands ###