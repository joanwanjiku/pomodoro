"""Added column password

Revision ID: e3b563d4347c
Revises: cc6e10806647
Create Date: 2020-07-16 12:46:08.645760

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3b563d4347c'
down_revision = 'cc6e10806647'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('hash_password', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'hash_password')
    # ### end Alembic commands ###
