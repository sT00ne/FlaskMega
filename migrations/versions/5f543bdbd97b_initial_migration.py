"""initial migration

Revision ID: 5f543bdbd97b
Revises: None
Create Date: 2016-07-29 11:11:16.138798

"""

# revision identifiers, used by Alembic.
revision = '5f543bdbd97b'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('test')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('test',
    sa.Column('id', sa.INTEGER(), nullable=True),
    sa.Column('uid', sa.INTEGER(), nullable=True)
    )
    ### end Alembic commands ###