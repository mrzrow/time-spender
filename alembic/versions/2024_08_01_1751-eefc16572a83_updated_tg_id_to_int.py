"""updated tg_id to int

Revision ID: eefc16572a83
Revises: b242b1ec30f0
Create Date: 2024-08-01 17:51:38.587161

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'eefc16572a83'
down_revision: Union[str, None] = 'b242b1ec30f0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    # op.alter_column(
    #     'user', 'tg_id',
    #     existing_type=sa.VARCHAR(),
    #     type_=sa.Integer(),
    #     existing_nullable=False)
    # ### end Alembic commands ###
    pass


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    # op.alter_column('user', 'tg_id',
    #                 existing_type=sa.Integer(),
    #                 type_=sa.VARCHAR(),
    #                 existing_nullable=False)
    # ### end Alembic commands ###
    pass