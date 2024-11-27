"""create core tables

Revision ID: 4e6511b12b44
Revises: 001_partition_tables
Create Date: 2024-11-27 11:07:02.907682

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '4e6511b12b44'
down_revision: Union[str, None] = '001_partition_tables'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Drop all tables
    op.execute("DROP TABLE IF EXISTS students_partitioned CASCADE;")
    op.execute("DROP TYPE IF EXISTS userrole;")
    
    # Create core tables
    op.create_table('tenants',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), onupdate=sa.text('now()'), nullable=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('subdomain', sa.String(), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False, default=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('subdomain')
    )
    
    op.create_table('schools',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), onupdate=sa.text('now()'), nullable=True),
        sa.Column('tenant_id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('address', sa.String(), nullable=False),
        sa.Column('phone', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False, default=True),
        sa.ForeignKeyConstraint(['tenant_id'], ['tenants.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )
    
    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), onupdate=sa.text('now()'), nullable=True),
        sa.Column('tenant_id', sa.Integer(), nullable=False),
        sa.Column('username', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('hashed_password', sa.String(), nullable=False),
        sa.Column('role', sa.Enum('SUPER_ADMIN', 'SCHOOL_ADMIN', 'TEACHER', 'STUDENT', 'PARENT', name='userrole'), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False, default=True),
        sa.ForeignKeyConstraint(['tenant_id'], ['tenants.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('username'),
        sa.UniqueConstraint('email')
    )
    # Create indexes
    op.create_index('idx_tenants_subdomain', 'tenants', ['subdomain'])
    op.create_index('idx_schools_tenant_id', 'schools', ['tenant_id'])
    op.create_index('idx_schools_email', 'schools', ['email'])
    op.create_index('idx_users_tenant_id', 'users', ['tenant_id'])
    op.create_index('idx_users_username', 'users', ['username'])
    op.create_index('idx_users_email', 'users', ['email'])
    op.create_index('idx_users_role', 'users', ['role'])
































    op.drop_index('students_partition_11_email_idx', table_name='students_partition_11')
    op.drop_table('students_partition_11')
    op.drop_index('idx_students_partition_16_id', table_name='students_partition_16')
    op.drop_index('idx_students_partition_16_school_id', table_name='students_partition_16')
    op.drop_index('students_partition_16_email_idx', table_name='students_partition_16')
    op.drop_table('students_partition_16')
    op.drop_index('idx_students_partition_45_id', table_name='students_partition_45')
    op.drop_index('idx_students_partition_45_school_id', table_name='students_partition_45')
    op.drop_index('students_partition_45_email_idx', table_name='students_partition_45')
    op.drop_table('students_partition_45')
    op.drop_index('idx_students_partition_23_id', table_name='students_partition_23')
    op.drop_index('idx_students_partition_23_school_id', table_name='students_partition_23')
    op.drop_index('students_partition_23_email_idx', table_name='students_partition_23')
    op.drop_table('students_partition_23')
    op.drop_index('idx_students_partition_38_id', table_name='students_partition_38')
    op.drop_index('idx_students_partition_38_school_id', table_name='students_partition_38')
    op.drop_index('students_partition_38_email_idx', table_name='students_partition_38')
    op.drop_table('students_partition_38')
    op.drop_index('idx_students_partition_56_id', table_name='students_partition_56')
    op.drop_index('idx_students_partition_56_school_id', table_name='students_partition_56')
    op.drop_index('students_partition_56_email_idx', table_name='students_partition_56')
    op.drop_table('students_partition_56')
    op.drop_index('idx_students_partition_49_id', table_name='students_partition_49')
    op.drop_index('idx_students_partition_49_school_id', table_name='students_partition_49')
    op.drop_index('students_partition_49_email_idx', table_name='students_partition_49')
    op.drop_table('students_partition_49')
    op.drop_index('idx_students_partition_2_id', table_name='students_partition_2')
    op.drop_index('idx_students_partition_2_school_id', table_name='students_partition_2')
    op.drop_index('students_partition_2_email_idx', table_name='students_partition_2')
    op.drop_table('students_partition_2')
    op.drop_index('idx_students_partition_51_id', table_name='students_partition_51')
    op.drop_index('idx_students_partition_51_school_id', table_name='students_partition_51')
    op.drop_index('students_partition_51_email_idx', table_name='students_partition_51')
    op.drop_table('students_partition_51')
    op.drop_index('idx_students_partition_61_id', table_name='students_partition_61')
    op.drop_index('idx_students_partition_61_school_id', table_name='students_partition_61')
    op.drop_index('students_partition_61_email_idx', table_name='students_partition_61')
    op.drop_table('students_partition_61')
    op.drop_index('idx_students_partition_57_id', table_name='students_partition_57')
    op.drop_index('idx_students_partition_57_school_id', table_name='students_partition_57')
    op.drop_index('students_partition_57_email_idx', table_name='students_partition_57')
    op.drop_table('students_partition_57')
    op.drop_index('idx_students_partition_85_id', table_name='students_partition_85')
    op.drop_index('idx_students_partition_85_school_id', table_name='students_partition_85')
    op.drop_index('students_partition_85_email_idx', table_name='students_partition_85')
    op.drop_table('students_partition_85')
    op.drop_index('idx_students_partition_82_id', table_name='students_partition_82')
    op.drop_index('idx_students_partition_82_school_id', table_name='students_partition_82')
    op.drop_index('students_partition_82_email_idx', table_name='students_partition_82')
    op.drop_table('students_partition_82')
    op.drop_index('idx_students_partition_65_id', table_name='students_partition_65')
    op.drop_index('idx_students_partition_65_school_id', table_name='students_partition_65')
    op.drop_index('students_partition_65_email_idx', table_name='students_partition_65')
    op.drop_table('students_partition_65')
    op.drop_index('idx_students_partition_93_id', table_name='students_partition_93')
    op.drop_index('idx_students_partition_93_school_id', table_name='students_partition_93')
    op.drop_index('students_partition_93_email_idx', table_name='students_partition_93')
    op.drop_table('students_partition_93')
    op.drop_index('idx_students_partition_50_id', table_name='students_partition_50')
    op.drop_index('idx_students_partition_50_school_id', table_name='students_partition_50')
    op.drop_index('students_partition_50_email_idx', table_name='students_partition_50')
    op.drop_table('students_partition_50')
    op.drop_index('idx_students_partition_31_id', table_name='students_partition_31')
    op.drop_index('idx_students_partition_31_school_id', table_name='students_partition_31')
    op.drop_index('students_partition_31_email_idx', table_name='students_partition_31')
    op.drop_table('students_partition_31')
    op.drop_index('idx_students_partition_4_id', table_name='students_partition_4')
    op.drop_index('idx_students_partition_4_school_id', table_name='students_partition_4')
    op.drop_index('students_partition_4_email_idx', table_name='students_partition_4')
    op.drop_table('students_partition_4')
    op.drop_index('idx_students_partition_44_id', table_name='students_partition_44')
    op.drop_index('idx_students_partition_44_school_id', table_name='students_partition_44')
    op.drop_index('students_partition_44_email_idx', table_name='students_partition_44')
    op.drop_table('students_partition_44')
    op.drop_index('idx_students_partition_1_id', table_name='students_partition_1')
    op.drop_index('idx_students_partition_1_school_id', table_name='students_partition_1')
    op.drop_index('students_partition_1_email_idx', table_name='students_partition_1')
    op.drop_table('students_partition_1')
    op.drop_index('idx_students_partition_91_id', table_name='students_partition_91')
    op.drop_index('idx_students_partition_91_school_id', table_name='students_partition_91')
    op.drop_index('students_partition_91_email_idx', table_name='students_partition_91')
    op.drop_table('students_partition_91')
    op.drop_index('idx_students_partition_74_id', table_name='students_partition_74')
    op.drop_index('idx_students_partition_74_school_id', table_name='students_partition_74')
    op.drop_index('students_partition_74_email_idx', table_name='students_partition_74')
    op.drop_table('students_partition_74')
    op.drop_index('idx_students_partition_70_id', table_name='students_partition_70')
    op.drop_index('idx_students_partition_70_school_id', table_name='students_partition_70')
    op.drop_index('students_partition_70_email_idx', table_name='students_partition_70')
    op.drop_table('students_partition_70')
    op.drop_index('idx_students_partition_13_id', table_name='students_partition_13')
    op.drop_index('idx_students_partition_13_school_id', table_name='students_partition_13')
    op.drop_index('students_partition_13_email_idx', table_name='students_partition_13')
    op.drop_table('students_partition_13')
    op.drop_index('idx_students_partition_25_id', table_name='students_partition_25')
    op.drop_index('idx_students_partition_25_school_id', table_name='students_partition_25')
    op.drop_index('students_partition_25_email_idx', table_name='students_partition_25')
    op.drop_table('students_partition_25')
    op.drop_index('idx_students_partition_48_id', table_name='students_partition_48')
    op.drop_index('idx_students_partition_48_school_id', table_name='students_partition_48')
    op.drop_index('students_partition_48_email_idx', table_name='students_partition_48')
    op.drop_table('students_partition_48')
    op.drop_index('idx_students_partition_59_id', table_name='students_partition_59')
    op.drop_index('idx_students_partition_59_school_id', table_name='students_partition_59')
    op.drop_index('students_partition_59_email_idx', table_name='students_partition_59')
    op.drop_table('students_partition_59')
    op.drop_index('idx_students_partition_19_id', table_name='students_partition_19')
    op.drop_index('idx_students_partition_19_school_id', table_name='students_partition_19')
    op.drop_index('students_partition_19_email_idx', table_name='students_partition_19')
    op.drop_table('students_partition_19')
    op.drop_index('idx_students_partition_88_id', table_name='students_partition_88')
    op.drop_index('idx_students_partition_88_school_id', table_name='students_partition_88')
    op.drop_index('students_partition_88_email_idx', table_name='students_partition_88')
    op.drop_table('students_partition_88')
    op.drop_index('idx_students_partition_28_id', table_name='students_partition_28')
    op.drop_index('idx_students_partition_28_school_id', table_name='students_partition_28')
    op.drop_index('students_partition_28_email_idx', table_name='students_partition_28')
    op.drop_table('students_partition_28')
    op.drop_index('idx_students_partition_18_id', table_name='students_partition_18')
    op.drop_index('idx_students_partition_18_school_id', table_name='students_partition_18')
    op.drop_index('students_partition_18_email_idx', table_name='students_partition_18')
    op.drop_table('students_partition_18')
    op.drop_index('idx_students_partition_17_id', table_name='students_partition_17')
    op.drop_index('idx_students_partition_17_school_id', table_name='students_partition_17')
    op.drop_index('students_partition_17_email_idx', table_name='students_partition_17')
    op.drop_table('students_partition_17')
    op.drop_index('idx_students_partition_47_id', table_name='students_partition_47')
    op.drop_index('idx_students_partition_47_school_id', table_name='students_partition_47')
    op.drop_index('students_partition_47_email_idx', table_name='students_partition_47')
    op.drop_table('students_partition_47')
    op.drop_index('idx_students_partition_37_id', table_name='students_partition_37')
    op.drop_index('idx_students_partition_37_school_id', table_name='students_partition_37')
    op.drop_index('students_partition_37_email_idx', table_name='students_partition_37')
    op.drop_table('students_partition_37')
    op.drop_index('idx_students_partition_5_id', table_name='students_partition_5')
    op.drop_index('idx_students_partition_5_school_id', table_name='students_partition_5')
    op.drop_index('students_partition_5_email_idx', table_name='students_partition_5')
    op.drop_table('students_partition_5')
    op.drop_index('idx_students_partition_68_id', table_name='students_partition_68')
    op.drop_index('idx_students_partition_68_school_id', table_name='students_partition_68')
    op.drop_index('students_partition_68_email_idx', table_name='students_partition_68')
    op.drop_table('students_partition_68')
    op.drop_index('idx_students_partition_96_id', table_name='students_partition_96')
    op.drop_index('idx_students_partition_96_school_id', table_name='students_partition_96')
    op.drop_index('students_partition_96_email_idx', table_name='students_partition_96')
    op.drop_table('students_partition_96')
    op.drop_index('idx_students_partition_79_id', table_name='students_partition_79')
    op.drop_index('idx_students_partition_79_school_id', table_name='students_partition_79')
    op.drop_index('students_partition_79_email_idx', table_name='students_partition_79')
    op.drop_table('students_partition_79')
    op.drop_index('idx_students_partition_33_id', table_name='students_partition_33')
    op.drop_index('idx_students_partition_33_school_id', table_name='students_partition_33')
    op.drop_index('students_partition_33_email_idx', table_name='students_partition_33')
    op.drop_table('students_partition_33')
    op.drop_index('idx_students_partition_73_id', table_name='students_partition_73')
    op.drop_index('idx_students_partition_73_school_id', table_name='students_partition_73')
    op.drop_index('students_partition_73_email_idx', table_name='students_partition_73')
    op.drop_table('students_partition_73')
    op.drop_index('idx_students_partition_54_id', table_name='students_partition_54')
    op.drop_index('idx_students_partition_54_school_id', table_name='students_partition_54')
    op.drop_index('students_partition_54_email_idx', table_name='students_partition_54')
    op.drop_table('students_partition_54')
    op.drop_index('idx_students_partition_34_id', table_name='students_partition_34')
    op.drop_index('idx_students_partition_34_school_id', table_name='students_partition_34')
    op.drop_index('students_partition_34_email_idx', table_name='students_partition_34')
    op.drop_table('students_partition_34')
    op.drop_index('idx_students_partition_12_id', table_name='students_partition_12')
    op.drop_index('idx_students_partition_12_school_id', table_name='students_partition_12')
    op.drop_index('students_partition_12_email_idx', table_name='students_partition_12')
    op.drop_table('students_partition_12')
    op.drop_index('idx_students_partition_62_id', table_name='students_partition_62')
    op.drop_index('idx_students_partition_62_school_id', table_name='students_partition_62')
    op.drop_index('students_partition_62_email_idx', table_name='students_partition_62')
    op.drop_table('students_partition_62')
    op.drop_index('idx_students_partition_0_id', table_name='students_partition_0')
    op.drop_index('idx_students_partition_0_school_id', table_name='students_partition_0')
    op.drop_index('students_partition_0_email_idx', table_name='students_partition_0')
    op.drop_table('students_partition_0')
    op.drop_index('idx_students_partition_39_id', table_name='students_partition_39')
    op.drop_index('idx_students_partition_39_school_id', table_name='students_partition_39')
    op.drop_index('students_partition_39_email_idx', table_name='students_partition_39')
    op.drop_table('students_partition_39')
    op.drop_index('idx_students_partition_64_id', table_name='students_partition_64')
    op.drop_index('idx_students_partition_64_school_id', table_name='students_partition_64')
    op.drop_index('students_partition_64_email_idx', table_name='students_partition_64')
    op.drop_table('students_partition_64')
    op.drop_index('idx_students_partition_69_id', table_name='students_partition_69')
    op.drop_index('idx_students_partition_69_school_id', table_name='students_partition_69')
    op.drop_index('students_partition_69_email_idx', table_name='students_partition_69')
    op.drop_table('students_partition_69')
    op.drop_index('idx_students_partition_80_id', table_name='students_partition_80')
    op.drop_index('idx_students_partition_80_school_id', table_name='students_partition_80')
    op.drop_index('students_partition_80_email_idx', table_name='students_partition_80')
    op.drop_table('students_partition_80')
    op.drop_index('idx_students_partition_99_id', table_name='students_partition_99')
    op.drop_index('idx_students_partition_99_school_id', table_name='students_partition_99')
    op.drop_index('students_partition_99_email_idx', table_name='students_partition_99')
    op.drop_table('students_partition_99')
    op.drop_index('idx_students_partition_63_id', table_name='students_partition_63')
    op.drop_index('idx_students_partition_63_school_id', table_name='students_partition_63')
    op.drop_index('students_partition_63_email_idx', table_name='students_partition_63')
    op.drop_table('students_partition_63')
    op.drop_index('idx_students_partition_15_id', table_name='students_partition_15')
    op.drop_index('idx_students_partition_15_school_id', table_name='students_partition_15')
    op.drop_index('students_partition_15_email_idx', table_name='students_partition_15')
    op.drop_table('students_partition_15')
    op.drop_index('idx_students_partition_30_id', table_name='students_partition_30')
    op.drop_index('idx_students_partition_30_school_id', table_name='students_partition_30')
    op.drop_index('students_partition_30_email_idx', table_name='students_partition_30')
    op.drop_table('students_partition_30')
    op.drop_index('idx_students_partition_83_id', table_name='students_partition_83')
    op.drop_index('idx_students_partition_83_school_id', table_name='students_partition_83')
    op.drop_index('students_partition_83_email_idx', table_name='students_partition_83')
    op.drop_table('students_partition_83')
    op.drop_index('idx_students_partition_35_id', table_name='students_partition_35')
    op.drop_index('idx_students_partition_35_school_id', table_name='students_partition_35')
    op.drop_index('students_partition_35_email_idx', table_name='students_partition_35')
    op.drop_table('students_partition_35')
    op.drop_index('idx_students_partition_77_id', table_name='students_partition_77')
    op.drop_index('idx_students_partition_77_school_id', table_name='students_partition_77')
    op.drop_index('students_partition_77_email_idx', table_name='students_partition_77')
    op.drop_table('students_partition_77')
    op.drop_index('idx_students_partition_94_id', table_name='students_partition_94')
    op.drop_index('idx_students_partition_94_school_id', table_name='students_partition_94')
    op.drop_index('students_partition_94_email_idx', table_name='students_partition_94')
    op.drop_table('students_partition_94')
    op.drop_index('idx_students_partition_75_id', table_name='students_partition_75')
    op.drop_index('idx_students_partition_75_school_id', table_name='students_partition_75')
    op.drop_index('students_partition_75_email_idx', table_name='students_partition_75')
    op.drop_table('students_partition_75')
    op.drop_index('idx_students_partition_78_id', table_name='students_partition_78')
    op.drop_index('idx_students_partition_78_school_id', table_name='students_partition_78')
    op.drop_index('students_partition_78_email_idx', table_name='students_partition_78')
    op.drop_table('students_partition_78')
    op.drop_index('idx_students_partition_60_id', table_name='students_partition_60')
    op.drop_index('idx_students_partition_60_school_id', table_name='students_partition_60')
    op.drop_index('students_partition_60_email_idx', table_name='students_partition_60')
    op.drop_table('students_partition_60')
    op.drop_index('idx_students_partition_6_id', table_name='students_partition_6')
    op.drop_index('idx_students_partition_6_school_id', table_name='students_partition_6')
    op.drop_index('students_partition_6_email_idx', table_name='students_partition_6')
    op.drop_table('students_partition_6')
    op.drop_index('idx_students_partition_32_id', table_name='students_partition_32')
    op.drop_index('idx_students_partition_32_school_id', table_name='students_partition_32')
    op.drop_index('students_partition_32_email_idx', table_name='students_partition_32')
    op.drop_table('students_partition_32')
    op.drop_index('idx_students_partition_66_id', table_name='students_partition_66')
    op.drop_index('idx_students_partition_66_school_id', table_name='students_partition_66')
    op.drop_index('students_partition_66_email_idx', table_name='students_partition_66')
    op.drop_table('students_partition_66')
    op.drop_index('idx_students_partition_14_id', table_name='students_partition_14')
    op.drop_index('idx_students_partition_14_school_id', table_name='students_partition_14')
    op.drop_index('students_partition_14_email_idx', table_name='students_partition_14')
    op.drop_table('students_partition_14')
    op.drop_index('idx_students_partition_40_id', table_name='students_partition_40')
    op.drop_index('idx_students_partition_40_school_id', table_name='students_partition_40')
    op.drop_index('students_partition_40_email_idx', table_name='students_partition_40')
    op.drop_table('students_partition_40')
    op.drop_index('idx_students_partition_24_id', table_name='students_partition_24')
    op.drop_index('idx_students_partition_24_school_id', table_name='students_partition_24')
    op.drop_index('students_partition_24_email_idx', table_name='students_partition_24')
    op.drop_table('students_partition_24')
    op.drop_index('idx_students_partition_26_id', table_name='students_partition_26')
    op.drop_index('idx_students_partition_26_school_id', table_name='students_partition_26')
    op.drop_index('students_partition_26_email_idx', table_name='students_partition_26')
    op.drop_table('students_partition_26')
    op.drop_index('idx_students_partition_84_id', table_name='students_partition_84')
    op.drop_index('idx_students_partition_84_school_id', table_name='students_partition_84')
    op.drop_index('students_partition_84_email_idx', table_name='students_partition_84')
    op.drop_table('students_partition_84')
    # ### end Alembic commands ###


def downgrade() -> None:
    # Drop all tables
    op.drop_table('users')
    op.drop_table('schools')
    op.drop_table('tenants')
    op.execute("DROP TYPE IF EXISTS userrole;")
    op.create_table('students_partition_84',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_84_email_idx', 'students_partition_84', ['email'], unique=False)
    op.create_index('idx_students_partition_84_school_id', 'students_partition_84', ['school_id'], unique=False)
    op.create_index('idx_students_partition_84_id', 'students_partition_84', ['id'], unique=False)
    op.create_table('students_partition_26',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_26_email_idx', 'students_partition_26', ['email'], unique=False)
    op.create_index('idx_students_partition_26_school_id', 'students_partition_26', ['school_id'], unique=False)
    op.create_index('idx_students_partition_26_id', 'students_partition_26', ['id'], unique=False)
    op.create_table('students_partition_24',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_24_email_idx', 'students_partition_24', ['email'], unique=False)
    op.create_index('idx_students_partition_24_school_id', 'students_partition_24', ['school_id'], unique=False)
    op.create_index('idx_students_partition_24_id', 'students_partition_24', ['id'], unique=False)
    op.create_table('students_partition_40',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_40_email_idx', 'students_partition_40', ['email'], unique=False)
    op.create_index('idx_students_partition_40_school_id', 'students_partition_40', ['school_id'], unique=False)
    op.create_index('idx_students_partition_40_id', 'students_partition_40', ['id'], unique=False)
    op.create_table('students_partition_14',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_14_email_idx', 'students_partition_14', ['email'], unique=False)
    op.create_index('idx_students_partition_14_school_id', 'students_partition_14', ['school_id'], unique=False)
    op.create_index('idx_students_partition_14_id', 'students_partition_14', ['id'], unique=False)
    op.create_table('students_partition_66',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_66_email_idx', 'students_partition_66', ['email'], unique=False)
    op.create_index('idx_students_partition_66_school_id', 'students_partition_66', ['school_id'], unique=False)
    op.create_index('idx_students_partition_66_id', 'students_partition_66', ['id'], unique=False)
    op.create_table('students_partition_32',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_32_email_idx', 'students_partition_32', ['email'], unique=False)
    op.create_index('idx_students_partition_32_school_id', 'students_partition_32', ['school_id'], unique=False)
    op.create_index('idx_students_partition_32_id', 'students_partition_32', ['id'], unique=False)
    op.create_table('students_partition_6',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_6_email_idx', 'students_partition_6', ['email'], unique=False)
    op.create_index('idx_students_partition_6_school_id', 'students_partition_6', ['school_id'], unique=False)
    op.create_index('idx_students_partition_6_id', 'students_partition_6', ['id'], unique=False)
    op.create_table('students_partition_60',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_60_email_idx', 'students_partition_60', ['email'], unique=False)
    op.create_index('idx_students_partition_60_school_id', 'students_partition_60', ['school_id'], unique=False)
    op.create_index('idx_students_partition_60_id', 'students_partition_60', ['id'], unique=False)
    op.create_table('students_partition_78',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_78_email_idx', 'students_partition_78', ['email'], unique=False)
    op.create_index('idx_students_partition_78_school_id', 'students_partition_78', ['school_id'], unique=False)
    op.create_index('idx_students_partition_78_id', 'students_partition_78', ['id'], unique=False)
    op.create_table('students_partition_75',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_75_email_idx', 'students_partition_75', ['email'], unique=False)
    op.create_index('idx_students_partition_75_school_id', 'students_partition_75', ['school_id'], unique=False)
    op.create_index('idx_students_partition_75_id', 'students_partition_75', ['id'], unique=False)
    op.create_table('students_partition_94',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_94_email_idx', 'students_partition_94', ['email'], unique=False)
    op.create_index('idx_students_partition_94_school_id', 'students_partition_94', ['school_id'], unique=False)
    op.create_index('idx_students_partition_94_id', 'students_partition_94', ['id'], unique=False)
    op.create_table('students_partition_77',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_77_email_idx', 'students_partition_77', ['email'], unique=False)
    op.create_index('idx_students_partition_77_school_id', 'students_partition_77', ['school_id'], unique=False)
    op.create_index('idx_students_partition_77_id', 'students_partition_77', ['id'], unique=False)
    op.create_table('students_partition_35',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_35_email_idx', 'students_partition_35', ['email'], unique=False)
    op.create_index('idx_students_partition_35_school_id', 'students_partition_35', ['school_id'], unique=False)
    op.create_index('idx_students_partition_35_id', 'students_partition_35', ['id'], unique=False)
    op.create_table('students_partition_83',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_83_email_idx', 'students_partition_83', ['email'], unique=False)
    op.create_index('idx_students_partition_83_school_id', 'students_partition_83', ['school_id'], unique=False)
    op.create_index('idx_students_partition_83_id', 'students_partition_83', ['id'], unique=False)
    op.create_table('students_partition_30',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_30_email_idx', 'students_partition_30', ['email'], unique=False)
    op.create_index('idx_students_partition_30_school_id', 'students_partition_30', ['school_id'], unique=False)
    op.create_index('idx_students_partition_30_id', 'students_partition_30', ['id'], unique=False)
    op.create_table('students_partition_15',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_15_email_idx', 'students_partition_15', ['email'], unique=False)
    op.create_index('idx_students_partition_15_school_id', 'students_partition_15', ['school_id'], unique=False)
    op.create_index('idx_students_partition_15_id', 'students_partition_15', ['id'], unique=False)
    op.create_table('students_partition_63',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_63_email_idx', 'students_partition_63', ['email'], unique=False)
    op.create_index('idx_students_partition_63_school_id', 'students_partition_63', ['school_id'], unique=False)
    op.create_index('idx_students_partition_63_id', 'students_partition_63', ['id'], unique=False)
    op.create_table('students_partition_99',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_99_email_idx', 'students_partition_99', ['email'], unique=False)
    op.create_index('idx_students_partition_99_school_id', 'students_partition_99', ['school_id'], unique=False)
    op.create_index('idx_students_partition_99_id', 'students_partition_99', ['id'], unique=False)
    op.create_table('students_partition_80',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_80_email_idx', 'students_partition_80', ['email'], unique=False)
    op.create_index('idx_students_partition_80_school_id', 'students_partition_80', ['school_id'], unique=False)
    op.create_index('idx_students_partition_80_id', 'students_partition_80', ['id'], unique=False)
    op.create_table('students_partition_69',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_69_email_idx', 'students_partition_69', ['email'], unique=False)
    op.create_index('idx_students_partition_69_school_id', 'students_partition_69', ['school_id'], unique=False)
    op.create_index('idx_students_partition_69_id', 'students_partition_69', ['id'], unique=False)
    op.create_table('students_partition_64',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_64_email_idx', 'students_partition_64', ['email'], unique=False)
    op.create_index('idx_students_partition_64_school_id', 'students_partition_64', ['school_id'], unique=False)
    op.create_index('idx_students_partition_64_id', 'students_partition_64', ['id'], unique=False)
    op.create_table('students_partition_39',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_39_email_idx', 'students_partition_39', ['email'], unique=False)
    op.create_index('idx_students_partition_39_school_id', 'students_partition_39', ['school_id'], unique=False)
    op.create_index('idx_students_partition_39_id', 'students_partition_39', ['id'], unique=False)
    op.create_table('students_partition_0',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_0_email_idx', 'students_partition_0', ['email'], unique=False)
    op.create_index('idx_students_partition_0_school_id', 'students_partition_0', ['school_id'], unique=False)
    op.create_index('idx_students_partition_0_id', 'students_partition_0', ['id'], unique=False)
    op.create_table('students_partition_62',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_62_email_idx', 'students_partition_62', ['email'], unique=False)
    op.create_index('idx_students_partition_62_school_id', 'students_partition_62', ['school_id'], unique=False)
    op.create_index('idx_students_partition_62_id', 'students_partition_62', ['id'], unique=False)
    op.create_table('students_partition_12',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_12_email_idx', 'students_partition_12', ['email'], unique=False)
    op.create_index('idx_students_partition_12_school_id', 'students_partition_12', ['school_id'], unique=False)
    op.create_index('idx_students_partition_12_id', 'students_partition_12', ['id'], unique=False)
    op.create_table('students_partition_34',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_34_email_idx', 'students_partition_34', ['email'], unique=False)
    op.create_index('idx_students_partition_34_school_id', 'students_partition_34', ['school_id'], unique=False)
    op.create_index('idx_students_partition_34_id', 'students_partition_34', ['id'], unique=False)
    op.create_table('students_partition_54',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_54_email_idx', 'students_partition_54', ['email'], unique=False)
    op.create_index('idx_students_partition_54_school_id', 'students_partition_54', ['school_id'], unique=False)
    op.create_index('idx_students_partition_54_id', 'students_partition_54', ['id'], unique=False)
    op.create_table('students_partition_73',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_73_email_idx', 'students_partition_73', ['email'], unique=False)
    op.create_index('idx_students_partition_73_school_id', 'students_partition_73', ['school_id'], unique=False)
    op.create_index('idx_students_partition_73_id', 'students_partition_73', ['id'], unique=False)
    op.create_table('students_partition_33',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_33_email_idx', 'students_partition_33', ['email'], unique=False)
    op.create_index('idx_students_partition_33_school_id', 'students_partition_33', ['school_id'], unique=False)
    op.create_index('idx_students_partition_33_id', 'students_partition_33', ['id'], unique=False)
    op.create_table('students_partition_79',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_79_email_idx', 'students_partition_79', ['email'], unique=False)
    op.create_index('idx_students_partition_79_school_id', 'students_partition_79', ['school_id'], unique=False)
    op.create_index('idx_students_partition_79_id', 'students_partition_79', ['id'], unique=False)
    op.create_table('students_partition_96',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_96_email_idx', 'students_partition_96', ['email'], unique=False)
    op.create_index('idx_students_partition_96_school_id', 'students_partition_96', ['school_id'], unique=False)
    op.create_index('idx_students_partition_96_id', 'students_partition_96', ['id'], unique=False)
    op.create_table('students_partition_68',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_68_email_idx', 'students_partition_68', ['email'], unique=False)
    op.create_index('idx_students_partition_68_school_id', 'students_partition_68', ['school_id'], unique=False)
    op.create_index('idx_students_partition_68_id', 'students_partition_68', ['id'], unique=False)
    op.create_table('students_partition_5',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_5_email_idx', 'students_partition_5', ['email'], unique=False)
    op.create_index('idx_students_partition_5_school_id', 'students_partition_5', ['school_id'], unique=False)
    op.create_index('idx_students_partition_5_id', 'students_partition_5', ['id'], unique=False)
    op.create_table('students_partition_37',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_37_email_idx', 'students_partition_37', ['email'], unique=False)
    op.create_index('idx_students_partition_37_school_id', 'students_partition_37', ['school_id'], unique=False)
    op.create_index('idx_students_partition_37_id', 'students_partition_37', ['id'], unique=False)
    op.create_table('students_partition_47',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_47_email_idx', 'students_partition_47', ['email'], unique=False)
    op.create_index('idx_students_partition_47_school_id', 'students_partition_47', ['school_id'], unique=False)
    op.create_index('idx_students_partition_47_id', 'students_partition_47', ['id'], unique=False)
    op.create_table('students_partition_17',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_17_email_idx', 'students_partition_17', ['email'], unique=False)
    op.create_index('idx_students_partition_17_school_id', 'students_partition_17', ['school_id'], unique=False)
    op.create_index('idx_students_partition_17_id', 'students_partition_17', ['id'], unique=False)
    op.create_table('students_partition_18',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_18_email_idx', 'students_partition_18', ['email'], unique=False)
    op.create_index('idx_students_partition_18_school_id', 'students_partition_18', ['school_id'], unique=False)
    op.create_index('idx_students_partition_18_id', 'students_partition_18', ['id'], unique=False)
    op.create_table('students_partition_28',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_28_email_idx', 'students_partition_28', ['email'], unique=False)
    op.create_index('idx_students_partition_28_school_id', 'students_partition_28', ['school_id'], unique=False)
    op.create_index('idx_students_partition_28_id', 'students_partition_28', ['id'], unique=False)
    op.create_table('students_partition_88',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_88_email_idx', 'students_partition_88', ['email'], unique=False)
    op.create_index('idx_students_partition_88_school_id', 'students_partition_88', ['school_id'], unique=False)
    op.create_index('idx_students_partition_88_id', 'students_partition_88', ['id'], unique=False)
    op.create_table('students_partition_19',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_19_email_idx', 'students_partition_19', ['email'], unique=False)
    op.create_index('idx_students_partition_19_school_id', 'students_partition_19', ['school_id'], unique=False)
    op.create_index('idx_students_partition_19_id', 'students_partition_19', ['id'], unique=False)
    op.create_table('students_partition_59',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_59_email_idx', 'students_partition_59', ['email'], unique=False)
    op.create_index('idx_students_partition_59_school_id', 'students_partition_59', ['school_id'], unique=False)
    op.create_index('idx_students_partition_59_id', 'students_partition_59', ['id'], unique=False)
    op.create_table('students_partition_48',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_48_email_idx', 'students_partition_48', ['email'], unique=False)
    op.create_index('idx_students_partition_48_school_id', 'students_partition_48', ['school_id'], unique=False)
    op.create_index('idx_students_partition_48_id', 'students_partition_48', ['id'], unique=False)
    op.create_table('students_partition_25',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_25_email_idx', 'students_partition_25', ['email'], unique=False)
    op.create_index('idx_students_partition_25_school_id', 'students_partition_25', ['school_id'], unique=False)
    op.create_index('idx_students_partition_25_id', 'students_partition_25', ['id'], unique=False)
    op.create_table('students_partition_13',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_13_email_idx', 'students_partition_13', ['email'], unique=False)
    op.create_index('idx_students_partition_13_school_id', 'students_partition_13', ['school_id'], unique=False)
    op.create_index('idx_students_partition_13_id', 'students_partition_13', ['id'], unique=False)
    op.create_table('students_partition_70',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_70_email_idx', 'students_partition_70', ['email'], unique=False)
    op.create_index('idx_students_partition_70_school_id', 'students_partition_70', ['school_id'], unique=False)
    op.create_index('idx_students_partition_70_id', 'students_partition_70', ['id'], unique=False)
    op.create_table('students_partition_74',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_74_email_idx', 'students_partition_74', ['email'], unique=False)
    op.create_index('idx_students_partition_74_school_id', 'students_partition_74', ['school_id'], unique=False)
    op.create_index('idx_students_partition_74_id', 'students_partition_74', ['id'], unique=False)
    op.create_table('students_partition_91',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_91_email_idx', 'students_partition_91', ['email'], unique=False)
    op.create_index('idx_students_partition_91_school_id', 'students_partition_91', ['school_id'], unique=False)
    op.create_index('idx_students_partition_91_id', 'students_partition_91', ['id'], unique=False)
    op.create_table('students_partition_1',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_1_email_idx', 'students_partition_1', ['email'], unique=False)
    op.create_index('idx_students_partition_1_school_id', 'students_partition_1', ['school_id'], unique=False)
    op.create_index('idx_students_partition_1_id', 'students_partition_1', ['id'], unique=False)
    op.create_table('students_partition_44',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_44_email_idx', 'students_partition_44', ['email'], unique=False)
    op.create_index('idx_students_partition_44_school_id', 'students_partition_44', ['school_id'], unique=False)
    op.create_index('idx_students_partition_44_id', 'students_partition_44', ['id'], unique=False)
    op.create_table('students_partition_4',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_4_email_idx', 'students_partition_4', ['email'], unique=False)
    op.create_index('idx_students_partition_4_school_id', 'students_partition_4', ['school_id'], unique=False)
    op.create_index('idx_students_partition_4_id', 'students_partition_4', ['id'], unique=False)
    op.create_table('students_partition_31',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_31_email_idx', 'students_partition_31', ['email'], unique=False)
    op.create_index('idx_students_partition_31_school_id', 'students_partition_31', ['school_id'], unique=False)
    op.create_index('idx_students_partition_31_id', 'students_partition_31', ['id'], unique=False)
    op.create_table('students_partition_50',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_50_email_idx', 'students_partition_50', ['email'], unique=False)
    op.create_index('idx_students_partition_50_school_id', 'students_partition_50', ['school_id'], unique=False)
    op.create_index('idx_students_partition_50_id', 'students_partition_50', ['id'], unique=False)
    op.create_table('students_partition_93',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_93_email_idx', 'students_partition_93', ['email'], unique=False)
    op.create_index('idx_students_partition_93_school_id', 'students_partition_93', ['school_id'], unique=False)
    op.create_index('idx_students_partition_93_id', 'students_partition_93', ['id'], unique=False)
    op.create_table('students_partition_65',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_65_email_idx', 'students_partition_65', ['email'], unique=False)
    op.create_index('idx_students_partition_65_school_id', 'students_partition_65', ['school_id'], unique=False)
    op.create_index('idx_students_partition_65_id', 'students_partition_65', ['id'], unique=False)
    op.create_table('students_partition_82',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_82_email_idx', 'students_partition_82', ['email'], unique=False)
    op.create_index('idx_students_partition_82_school_id', 'students_partition_82', ['school_id'], unique=False)
    op.create_index('idx_students_partition_82_id', 'students_partition_82', ['id'], unique=False)
    op.create_table('students_partition_85',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_85_email_idx', 'students_partition_85', ['email'], unique=False)
    op.create_index('idx_students_partition_85_school_id', 'students_partition_85', ['school_id'], unique=False)
    op.create_index('idx_students_partition_85_id', 'students_partition_85', ['id'], unique=False)
    op.create_table('students_partition_57',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_57_email_idx', 'students_partition_57', ['email'], unique=False)
    op.create_index('idx_students_partition_57_school_id', 'students_partition_57', ['school_id'], unique=False)
    op.create_index('idx_students_partition_57_id', 'students_partition_57', ['id'], unique=False)
    op.create_table('students_partition_61',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_61_email_idx', 'students_partition_61', ['email'], unique=False)
    op.create_index('idx_students_partition_61_school_id', 'students_partition_61', ['school_id'], unique=False)
    op.create_index('idx_students_partition_61_id', 'students_partition_61', ['id'], unique=False)
    op.create_table('students_partition_51',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_51_email_idx', 'students_partition_51', ['email'], unique=False)
    op.create_index('idx_students_partition_51_school_id', 'students_partition_51', ['school_id'], unique=False)
    op.create_index('idx_students_partition_51_id', 'students_partition_51', ['id'], unique=False)
    op.create_table('students_partition_2',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_2_email_idx', 'students_partition_2', ['email'], unique=False)
    op.create_index('idx_students_partition_2_school_id', 'students_partition_2', ['school_id'], unique=False)
    op.create_index('idx_students_partition_2_id', 'students_partition_2', ['id'], unique=False)
    op.create_table('students_partition_49',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_49_email_idx', 'students_partition_49', ['email'], unique=False)
    op.create_index('idx_students_partition_49_school_id', 'students_partition_49', ['school_id'], unique=False)
    op.create_index('idx_students_partition_49_id', 'students_partition_49', ['id'], unique=False)
    op.create_table('students_partition_56',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_56_email_idx', 'students_partition_56', ['email'], unique=False)
    op.create_index('idx_students_partition_56_school_id', 'students_partition_56', ['school_id'], unique=False)
    op.create_index('idx_students_partition_56_id', 'students_partition_56', ['id'], unique=False)
    op.create_table('students_partition_38',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_38_email_idx', 'students_partition_38', ['email'], unique=False)
    op.create_index('idx_students_partition_38_school_id', 'students_partition_38', ['school_id'], unique=False)
    op.create_index('idx_students_partition_38_id', 'students_partition_38', ['id'], unique=False)
    op.create_table('students_partition_23',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_23_email_idx', 'students_partition_23', ['email'], unique=False)
    op.create_index('idx_students_partition_23_school_id', 'students_partition_23', ['school_id'], unique=False)
    op.create_index('idx_students_partition_23_id', 'students_partition_23', ['id'], unique=False)
    op.create_table('students_partition_45',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_45_email_idx', 'students_partition_45', ['email'], unique=False)
    op.create_index('idx_students_partition_45_school_id', 'students_partition_45', ['school_id'], unique=False)
    op.create_index('idx_students_partition_45_id', 'students_partition_45', ['id'], unique=False)
    op.create_table('students_partition_16',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_16_email_idx', 'students_partition_16', ['email'], unique=False)
    op.create_index('idx_students_partition_16_school_id', 'students_partition_16', ['school_id'], unique=False)
    op.create_index('idx_students_partition_16_id', 'students_partition_16', ['id'], unique=False)
    op.create_table('students_partition_11',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_11_email_idx', 'students_partition_11', ['email'], unique=False)
    op.create_index('idx_students_partition_11_school_id', 'students_partition_11', ['school_id'], unique=False)
    op.create_index('idx_students_partition_11_id', 'students_partition_11', ['id'], unique=False)
    op.create_table('students_partition_36',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_36_email_idx', 'students_partition_36', ['email'], unique=False)
    op.create_index('idx_students_partition_36_school_id', 'students_partition_36', ['school_id'], unique=False)
    op.create_index('idx_students_partition_36_id', 'students_partition_36', ['id'], unique=False)
    op.create_table('students_partition_29',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_29_email_idx', 'students_partition_29', ['email'], unique=False)
    op.create_index('idx_students_partition_29_school_id', 'students_partition_29', ['school_id'], unique=False)
    op.create_index('idx_students_partition_29_id', 'students_partition_29', ['id'], unique=False)
    op.create_table('students_partition_22',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_22_email_idx', 'students_partition_22', ['email'], unique=False)
    op.create_index('idx_students_partition_22_school_id', 'students_partition_22', ['school_id'], unique=False)
    op.create_index('idx_students_partition_22_id', 'students_partition_22', ['id'], unique=False)
    op.create_table('students_partition_76',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_76_email_idx', 'students_partition_76', ['email'], unique=False)
    op.create_index('idx_students_partition_76_school_id', 'students_partition_76', ['school_id'], unique=False)
    op.create_index('idx_students_partition_76_id', 'students_partition_76', ['id'], unique=False)
    op.create_table('students_partitioned',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('idx_students_school_id', 'students_partitioned', ['school_id'], unique=False)
    op.create_index('idx_students_email', 'students_partitioned', ['email'], unique=False)
    op.create_table('students_partition_67',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_67_email_idx', 'students_partition_67', ['email'], unique=False)
    op.create_index('idx_students_partition_67_school_id', 'students_partition_67', ['school_id'], unique=False)
    op.create_index('idx_students_partition_67_id', 'students_partition_67', ['id'], unique=False)
    op.create_table('students_partition_89',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_89_email_idx', 'students_partition_89', ['email'], unique=False)
    op.create_index('idx_students_partition_89_school_id', 'students_partition_89', ['school_id'], unique=False)
    op.create_index('idx_students_partition_89_id', 'students_partition_89', ['id'], unique=False)
    op.create_table('students_partition_46',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_46_email_idx', 'students_partition_46', ['email'], unique=False)
    op.create_index('idx_students_partition_46_school_id', 'students_partition_46', ['school_id'], unique=False)
    op.create_index('idx_students_partition_46_id', 'students_partition_46', ['id'], unique=False)
    op.create_table('students_partition_21',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_21_email_idx', 'students_partition_21', ['email'], unique=False)
    op.create_index('idx_students_partition_21_school_id', 'students_partition_21', ['school_id'], unique=False)
    op.create_index('idx_students_partition_21_id', 'students_partition_21', ['id'], unique=False)
    op.create_table('students_partition_81',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_81_email_idx', 'students_partition_81', ['email'], unique=False)
    op.create_index('idx_students_partition_81_school_id', 'students_partition_81', ['school_id'], unique=False)
    op.create_index('idx_students_partition_81_id', 'students_partition_81', ['id'], unique=False)
    op.create_table('students_partition_52',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_52_email_idx', 'students_partition_52', ['email'], unique=False)
    op.create_index('idx_students_partition_52_school_id', 'students_partition_52', ['school_id'], unique=False)
    op.create_index('idx_students_partition_52_id', 'students_partition_52', ['id'], unique=False)
    op.create_table('students_partition_87',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_87_email_idx', 'students_partition_87', ['email'], unique=False)
    op.create_index('idx_students_partition_87_school_id', 'students_partition_87', ['school_id'], unique=False)
    op.create_index('idx_students_partition_87_id', 'students_partition_87', ['id'], unique=False)
    op.create_table('students_partition_72',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_72_email_idx', 'students_partition_72', ['email'], unique=False)
    op.create_index('idx_students_partition_72_school_id', 'students_partition_72', ['school_id'], unique=False)
    op.create_index('idx_students_partition_72_id', 'students_partition_72', ['id'], unique=False)
    op.create_table('students_partition_97',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_97_email_idx', 'students_partition_97', ['email'], unique=False)
    op.create_index('idx_students_partition_97_school_id', 'students_partition_97', ['school_id'], unique=False)
    op.create_index('idx_students_partition_97_id', 'students_partition_97', ['id'], unique=False)
    op.create_table('students_partition_98',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_98_email_idx', 'students_partition_98', ['email'], unique=False)
    op.create_index('idx_students_partition_98_school_id', 'students_partition_98', ['school_id'], unique=False)
    op.create_index('idx_students_partition_98_id', 'students_partition_98', ['id'], unique=False)
    op.create_table('students_partition_55',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_55_email_idx', 'students_partition_55', ['email'], unique=False)
    op.create_index('idx_students_partition_55_school_id', 'students_partition_55', ['school_id'], unique=False)
    op.create_index('idx_students_partition_55_id', 'students_partition_55', ['id'], unique=False)
    op.create_table('students_partition_20',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_20_email_idx', 'students_partition_20', ['email'], unique=False)
    op.create_index('idx_students_partition_20_school_id', 'students_partition_20', ['school_id'], unique=False)
    op.create_index('idx_students_partition_20_id', 'students_partition_20', ['id'], unique=False)
    op.create_table('students_partition_41',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_41_email_idx', 'students_partition_41', ['email'], unique=False)
    op.create_index('idx_students_partition_41_school_id', 'students_partition_41', ['school_id'], unique=False)
    op.create_index('idx_students_partition_41_id', 'students_partition_41', ['id'], unique=False)
    op.create_table('students_partition_90',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_90_email_idx', 'students_partition_90', ['email'], unique=False)
    op.create_index('idx_students_partition_90_school_id', 'students_partition_90', ['school_id'], unique=False)
    op.create_index('idx_students_partition_90_id', 'students_partition_90', ['id'], unique=False)
    op.create_table('students_partition_10',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_10_email_idx', 'students_partition_10', ['email'], unique=False)
    op.create_index('idx_students_partition_10_school_id', 'students_partition_10', ['school_id'], unique=False)
    op.create_index('idx_students_partition_10_id', 'students_partition_10', ['id'], unique=False)
    op.create_table('students_partition_71',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_71_email_idx', 'students_partition_71', ['email'], unique=False)
    op.create_index('idx_students_partition_71_school_id', 'students_partition_71', ['school_id'], unique=False)
    op.create_index('idx_students_partition_71_id', 'students_partition_71', ['id'], unique=False)
    op.create_table('students_partition_95',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_95_email_idx', 'students_partition_95', ['email'], unique=False)
    op.create_index('idx_students_partition_95_school_id', 'students_partition_95', ['school_id'], unique=False)
    op.create_index('idx_students_partition_95_id', 'students_partition_95', ['id'], unique=False)
    op.create_table('students_partition_43',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_43_email_idx', 'students_partition_43', ['email'], unique=False)
    op.create_index('idx_students_partition_43_school_id', 'students_partition_43', ['school_id'], unique=False)
    op.create_index('idx_students_partition_43_id', 'students_partition_43', ['id'], unique=False)
    op.create_table('students_partition_7',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_7_email_idx', 'students_partition_7', ['email'], unique=False)
    op.create_index('idx_students_partition_7_school_id', 'students_partition_7', ['school_id'], unique=False)
    op.create_index('idx_students_partition_7_id', 'students_partition_7', ['id'], unique=False)
    op.create_table('students_partition_3',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_3_email_idx', 'students_partition_3', ['email'], unique=False)
    op.create_index('idx_students_partition_3_school_id', 'students_partition_3', ['school_id'], unique=False)
    op.create_index('idx_students_partition_3_id', 'students_partition_3', ['id'], unique=False)
    op.create_table('students_partition_53',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_53_email_idx', 'students_partition_53', ['email'], unique=False)
    op.create_index('idx_students_partition_53_school_id', 'students_partition_53', ['school_id'], unique=False)
    op.create_index('idx_students_partition_53_id', 'students_partition_53', ['id'], unique=False)
    op.create_table('students_partition_58',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_58_email_idx', 'students_partition_58', ['email'], unique=False)
    op.create_index('idx_students_partition_58_school_id', 'students_partition_58', ['school_id'], unique=False)
    op.create_index('idx_students_partition_58_id', 'students_partition_58', ['id'], unique=False)
    op.create_table('students_partition_8',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_8_email_idx', 'students_partition_8', ['email'], unique=False)
    op.create_index('idx_students_partition_8_school_id', 'students_partition_8', ['school_id'], unique=False)
    op.create_index('idx_students_partition_8_id', 'students_partition_8', ['id'], unique=False)
    op.create_table('students_partition_42',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_42_email_idx', 'students_partition_42', ['email'], unique=False)
    op.create_index('idx_students_partition_42_school_id', 'students_partition_42', ['school_id'], unique=False)
    op.create_index('idx_students_partition_42_id', 'students_partition_42', ['id'], unique=False)
    op.create_table('students_partition_86',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_86_email_idx', 'students_partition_86', ['email'], unique=False)
    op.create_index('idx_students_partition_86_school_id', 'students_partition_86', ['school_id'], unique=False)
    op.create_index('idx_students_partition_86_id', 'students_partition_86', ['id'], unique=False)
    op.create_table('students_partition_27',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_27_email_idx', 'students_partition_27', ['email'], unique=False)
    op.create_index('idx_students_partition_27_school_id', 'students_partition_27', ['school_id'], unique=False)
    op.create_index('idx_students_partition_27_id', 'students_partition_27', ['id'], unique=False)
    op.create_table('students_partition_9',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_9_email_idx', 'students_partition_9', ['email'], unique=False)
    op.create_index('idx_students_partition_9_school_id', 'students_partition_9', ['school_id'], unique=False)
    op.create_index('idx_students_partition_9_id', 'students_partition_9', ['id'], unique=False)
    op.create_table('students_partition_92',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    op.create_index('students_partition_92_email_idx', 'students_partition_92', ['email'], unique=False)
    op.create_index('idx_students_partition_92_school_id', 'students_partition_92', ['school_id'], unique=False)
    op.create_index('idx_students_partition_92_id', 'students_partition_92', ['id'], unique=False)
    # ### end Alembic commands ###