"""
Migration: Increase ip_address and user_agent length in audit_logs
"""
from alembic import op
import sqlalchemy as sa

def upgrade():
    with op.batch_alter_table('audit_logs') as batch_op:
        batch_op.alter_column('ip_address', type_=sa.String(length=100), existing_type=sa.String(length=45), nullable=True)
        batch_op.alter_column('user_agent', type_=sa.String(length=1000), existing_type=sa.String(length=500), nullable=True)

def downgrade():
    with op.batch_alter_table('audit_logs') as batch_op:
        batch_op.alter_column('ip_address', type_=sa.String(length=45), existing_type=sa.String(length=100), nullable=True)
        batch_op.alter_column('user_agent', type_=sa.String(length=500), existing_type=sa.String(length=1000), nullable=True)
