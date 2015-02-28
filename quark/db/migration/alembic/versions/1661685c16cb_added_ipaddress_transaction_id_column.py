"""Added IPAddress.transaction_id column

Revision ID: 1661685c16cb
Revises: 3a47813ce501
Create Date: 2015-02-28 10:35:44.586951

"""

# revision identifiers, used by Alembic.
revision = '1661685c16cb'
down_revision = '3a47813ce501'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column(
        'quark_ip_addresses',
        sa.Column('transaction_id', sa.String(length=36), nullable=True))
    op.create_index(
        op.f('ix_quark_ip_addresses_transaction_id'),
        'quark_ip_addresses',
        ['transaction_id'],
        unique=False)


def downgrade():
    op.drop_index(
        op.f('ix_quark_ip_addresses_transaction_id'),
        table_name='quark_ip_addresses')
    op.drop_column('quark_ip_addresses', 'transaction_id')
