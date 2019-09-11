"""empty message

Revision ID: 098b3b890eca
Revises: 
Create Date: 2019-09-11 17:01:12.376900

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '098b3b890eca'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tag',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('article',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('article_tag',
    sa.Column('article_id', sa.Integer(), nullable=False),
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['article_id'], ['article.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], ),
    sa.PrimaryKeyConstraint('article_id', 'tag_id')
    )
    op.add_column('user', sa.Column('email', sa.String(length=50), nullable=True))
    op.alter_column('user', 'username',
               existing_type=mysql.VARCHAR(length=50),
               nullable=True)
    op.drop_column('user', 'height')
    op.drop_column('user', 'age')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('age', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('height', mysql.VARCHAR(length=30), nullable=True))
    op.alter_column('user', 'username',
               existing_type=mysql.VARCHAR(length=50),
               nullable=False)
    op.drop_column('user', 'email')
    op.drop_table('article_tag')
    op.drop_table('article')
    op.drop_table('tag')
    # ### end Alembic commands ###
