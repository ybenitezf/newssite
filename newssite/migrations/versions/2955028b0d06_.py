"""empty message

Revision ID: 2955028b0d06
Revises: c86a5a63b04b
Create Date: 2021-07-02 13:31:10.926522

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2955028b0d06'
down_revision = 'c86a5a63b04b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('photo', sa.Column('store_data', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('photo', 'store_data')
    # ### end Alembic commands ###
