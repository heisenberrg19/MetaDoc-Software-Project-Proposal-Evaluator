"""Migration: Increase ip_address and user_agent length in audit_logs

Revision ID: 20260428_increase_auditlog_ip_useragent_length
Revises: 
Create Date: 2026-04-28 00:00:00.000000
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '20260428_increase_auditlog_ip_useragent_length'
down_revision = 'dd4b2bce9163'
branch_labels = None
depends_on = None

def upgrade():
    with op.batch_alter_table('audit_logs') as batch_op:
        batch_op.alter_column('ip_address', type_=sa.String(length=100), existing_type=sa.String(length=45), nullable=True)
        batch_op.alter_column('user_agent', type_=sa.String(length=1000), existing_type=sa.String(length=500), nullable=True)

def downgrade():
    with op.batch_alter_table('audit_logs') as batch_op:
        batch_op.alter_column('ip_address', type_=sa.String(length=45), existing_type=sa.String(length=100), nullable=True)
        batch_op.alter_column('user_agent', type_=sa.String(length=500), existing_type=sa.String(length=1000), nullable=True)
