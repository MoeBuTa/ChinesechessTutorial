"""add columns to TutorialProgress

Revision ID: d8265ec587c8
Revises: eee5bc3faa7f
Create Date: 2021-05-15 16:47:41.521175

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd8265ec587c8'
down_revision = 'eee5bc3faa7f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tutorial_progress', schema=None) as batch_op:
        batch_op.add_column(sa.Column('last_tutorial_read_time', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('read_tutorial_num', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('time_duration', sa.Float(precision=10, decimal_return_scale=2), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tutorial_progress', schema=None) as batch_op:
        batch_op.drop_column('time_duration')
        batch_op.drop_column('read_tutorial_num')
        batch_op.drop_column('last_tutorial_read_time')

    # ### end Alembic commands ###
