"""bcsQuestion table create

Revision ID: 4d10fc3dcae7
Revises: 42a97b2bae3e
Create Date: 2022-10-19 23:03:27.396280

"""
from alembic import op
import sqlalchemy as sa
from datetime import date

# revision identifiers, used by Alembic.
revision = '4d10fc3dcae7'
down_revision = '42a97b2bae3e'
branch_labels = None
depends_on = None



def upgrade() -> None:
    op.create_table("bcs_questions",
    sa.Column("id",sa.Integer,primary_key=True),

    sa.Column("question",sa.String,nullable=False),
    sa.Column("option_a",sa.String,nullable=False),
    sa.Column("option_b",sa.String,nullable=False),
    sa.Column("option_c",sa.String,nullable=False),    
    sa.Column("option_d",sa.String,nullable=False),
    sa.Column("answer",sa.String(1),nullable=False),
    sa.Column("note",sa.String,nullable=True),
    sa.Column("explanation",sa.String,nullable=True),
    sa.Column("created_at",sa.Date,default=date.today),

    sa.Column("topic_id",sa.Integer,sa.ForeignKey("topics.id"),nullable=False),
    sa.Column("bcs",sa.Integer,sa.ForeignKey("bcs.ordinal"),nullable=False),
    
    )


def downgrade() -> None:
     op.drop_table("bcs_questions")
