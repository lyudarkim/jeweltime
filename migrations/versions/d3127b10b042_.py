"""empty message

Revision ID: d3127b10b042
Revises: 
Create Date: 2023-07-14 09:13:38.847057

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3127b10b042'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('account',
    sa.Column('account_id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=80), nullable=True),
    sa.Column('last_name', sa.String(length=80), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('zipcode', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('account_id')
    )
    op.create_table('project',
    sa.Column('project_id', sa.Integer(), nullable=False),
    sa.Column('project_name', sa.String(length=100), nullable=True),
    sa.Column('description', sa.String(length=250), nullable=True),
    sa.Column('started_at', sa.DateTime(), nullable=False),
    sa.Column('completed_at', sa.DateTime(), nullable=True),
    sa.Column('hours_spent', sa.Float(), nullable=True),
    sa.Column('materials_cost', sa.Float(), nullable=True),
    sa.Column('materials', sa.PickleType(), nullable=True),
    sa.Column('metals', sa.PickleType(), nullable=True),
    sa.Column('gemstones', sa.PickleType(), nullable=True),
    sa.Column('shape', sa.String(length=100), nullable=True),
    sa.Column('jewelry_type', sa.String(length=100), nullable=True),
    sa.Column('account_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['account_id'], ['account.account_id'], ),
    sa.PrimaryKeyConstraint('project_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('project')
    op.drop_table('account')
    # ### end Alembic commands ###
