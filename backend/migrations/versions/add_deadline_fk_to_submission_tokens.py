"""Add ForeignKey constraint to submission_tokens.deadline_id

Revision ID: a8d3f2b1e4c5
Revises: d1b5d8f1c7a4
Create Date: 2026-04-26 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a8d3f2b1e4c5'
down_revision = 'd1b5d8f1c7a4'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('submission_tokens', schema=None) as batch_op:
        batch_op.create_foreign_key(
            'submission_tokens_deadline_id_fkey',
            'deadlines',
            ['deadline_id'],
            ['id'],
            ondelete='SET NULL'
        )


def downgrade():
    with op.batch_alter_table('submission_tokens', schema=None) as batch_op:
        batch_op.drop_constraint('submission_tokens_deadline_id_fkey', type_='foreignkey')
