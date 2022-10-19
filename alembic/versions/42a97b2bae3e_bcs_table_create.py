"""bcs table create

Revision ID: 42a97b2bae3e
Revises: 1c6e9186e8cc
Create Date: 2022-10-19 23:00:40.026835

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42a97b2bae3e'
down_revision = '1c6e9186e8cc'
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table("bcs",
    sa.Column("id",sa.Integer,primary_key=True),
    sa.Column("ordinal",sa.Integer,nullable=False,unique=True),
    sa.Column("total_marks",sa.Integer,nullable=False),
    sa.Column("duration",sa.Integer,nullable=False),
    sa.Column("special",sa.String,nullable=False),
    sa.Column("exam_year",sa.String(4),nullable=False)
    
    )


def downgrade() -> None:
    op.drop_table("bcs")

