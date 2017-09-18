"""add wrapuptime to queue_members

Revision ID: 8b85c32f5750
Revises: 2da192dbbc65
Create Date: 2017-09-18 20:02:34.138260

"""

# revision identifiers, used by Alembic.
revision = '8b85c32f5750'
down_revision = '2da192dbbc65'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('queue_members', sa.Column('wrapuptime', sa.Integer))


def downgrade():
    op.drop_column('queue_members', 'wrapuptime')
