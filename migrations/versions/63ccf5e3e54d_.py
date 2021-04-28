"""empty message

Revision ID: 63ccf5e3e54d
Revises: f64f7cde9c6f
Create Date: 2021-04-27 21:52:40.166826

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63ccf5e3e54d'
down_revision = 'f64f7cde9c6f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tutorial',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=140), nullable=True),
    sa.Column('content', sa.UnicodeText(), nullable=True),
    sa.Column('img_url', sa.String(length=140), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tutorial')
    # ### end Alembic commands ###