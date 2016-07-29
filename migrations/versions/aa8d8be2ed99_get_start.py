"""get start

Revision ID: aa8d8be2ed99
Revises: ba02073fb6f1
Create Date: 2016-07-29 11:14:49.307990

"""

# revision identifiers, used by Alembic.
revision = 'aa8d8be2ed99'
down_revision = 'ba02073fb6f1'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post2')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post2',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('body', sa.VARCHAR(length=140), nullable=True),
    sa.Column('timestamp', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###
