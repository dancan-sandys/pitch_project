"""remove the upvotes and downvotes section in thereviews

Revision ID: de05f91e9936
Revises: 5690ed2fd298
Create Date: 2020-09-21 09:54:34.540931

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de05f91e9936'
down_revision = '5690ed2fd298'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reviews', sa.Column('pitch_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'reviews', 'pitches', ['pitch_id'], ['pitch_id'])
    op.drop_column('reviews', 'downvotes')
    op.drop_column('reviews', 'upvotes')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reviews', sa.Column('upvotes', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('reviews', sa.Column('downvotes', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'reviews', type_='foreignkey')
    op.drop_column('reviews', 'pitch_id')
    # ### end Alembic commands ###
