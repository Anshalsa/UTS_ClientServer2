"""Initial migration.

Revision ID: 3d59fda53fef
Revises: 
Create Date: 2020-04-19 11:59:16.748441

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d59fda53fef'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('person',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nim', sa.CHAR(length=10), nullable=False),
    sa.Column('nama', sa.CHAR(length=100), nullable=False),
    sa.Column('alamat', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nim')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('person')
    # ### end Alembic commands ###
