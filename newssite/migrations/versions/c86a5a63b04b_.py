"""empty message

Revision ID: c86a5a63b04b
Revises: 
Create Date: 2021-07-02 13:23:19.391111

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c86a5a63b04b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('id', sa.String(length=32), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('nickname', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=254), nullable=True),
    sa.Column('author_type', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_author_email'), 'author', ['email'], unique=False)
    op.create_index(op.f('ix_author_nickname'), 'author', ['nickname'], unique=True)
    op.create_table('image',
    sa.Column('id', sa.String(length=32), nullable=False),
    sa.Column('filename', sa.Text(), nullable=True),
    sa.Column('width', sa.Integer(), nullable=True),
    sa.Column('height', sa.Integer(), nullable=True),
    sa.Column('orientation', sa.String(length=10), nullable=True),
    sa.Column('image_type', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('photographer',
    sa.Column('id', sa.String(length=32), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['author.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('writer',
    sa.Column('id', sa.String(length=32), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['author.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('photo',
    sa.Column('id', sa.String(length=32), nullable=False),
    sa.Column('author_id', sa.String(length=32), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['photographer.id'], ),
    sa.ForeignKeyConstraint(['id'], ['image.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('photo')
    op.drop_table('writer')
    op.drop_table('photographer')
    op.drop_table('image')
    op.drop_index(op.f('ix_author_nickname'), table_name='author')
    op.drop_index(op.f('ix_author_email'), table_name='author')
    op.drop_table('author')
    # ### end Alembic commands ###
