"""topics table create

Revision ID: 1c6e9186e8cc
Revises: 
Create Date: 2022-10-19 22:59:37.962122

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c6e9186e8cc'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table(
        "topics",
        sa.Column("id",sa.Integer,primary_key=True),
        sa.Column("name",sa.String,nullable=False,unique=True),
    )


def downgrade() -> None:
    op.drop_table("topics")