"""remove the profile table"


Revision ID: d037e193abc7
Revises: 40b505401d3f
Create Date: 2020-09-20 22:03:19.484525

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd037e193abc7'
down_revision = '40b505401d3f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('profiles')
    op.add_column('pitches', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'pitches', 'users', ['user_id'], ['user_id'])
    op.add_column('users', sa.Column('User_bio', sa.String(), nullable=True))
    op.add_column('users', sa.Column('profile_pic', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'profile_pic')
    op.drop_column('users', 'User_bio')
    op.drop_constraint(None, 'pitches', type_='foreignkey')
    op.drop_column('pitches', 'user_id')
    op.create_table('profiles',
    sa.Column('profile_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('profile_pic', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('User_bio', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('profile_id', name='profiles_pkey')
    )
    # ### end Alembic commands ###