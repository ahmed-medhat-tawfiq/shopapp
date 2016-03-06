"""create account table

Revision ID: 616bcd81b089
Revises: 
Create Date: 2016-03-05 18:18:23.673744

"""

# revision identifiers, used by Alembic.
revision = '616bcd81b089'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('code',
            sa.Column('ox', sa.Unicode(100)),
    )



def downgrade():
    pass