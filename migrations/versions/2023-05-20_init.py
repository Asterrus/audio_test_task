"""init

Revision ID: 7acf31ba0c60
Revises: 
Create Date: 2023-05-20 02:05:39.143655

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7acf31ba0c60'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('audio',
    sa.Column('UUID', sa.String(), nullable=False),
    sa.Column('user_UUID', sa.String(), nullable=False),
    sa.Column('file_path', sa.String(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_audio_id'), 'audio', ['id'], unique=False)
    op.create_table('user',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('unique_slug', sa.String(), nullable=False),
    sa.Column('UUID', sa.String(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_audio_id'), table_name='audio')
    op.drop_table('audio')
    # ### end Alembic commands ###