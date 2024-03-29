"""create product table

Revision ID: 8ca7bff8f663
Revises: 
Create Date: 2023-05-31 19:33:44.876743

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "8ca7bff8f663"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "products",
        sa.Column("id", sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column("name", sa.Unicode(length=255), nullable=False),
        sa.Column("size", sa.Unicode(length=255), nullable=False),
        sa.Column("price", sa.Unicode(length=255), nullable=False),
        sa.Column("color", sa.Unicode(length=255), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("products")
    # ### end Alembic commands ###