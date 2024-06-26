"""rename department

Revision ID: 826ab2b44f64
Revises: 93c041d8b704
Create Date: 2024-06-26 08:55:10.367266

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '826ab2b44f64'
down_revision = '93c041d8b704'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('department', 'departments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('departments', 'department')
    # ### end Alembic commands ###
