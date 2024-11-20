"""partition tables

Revision ID: partition_tables
Revises: previous_revision
Create Date: 2024-01-20 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

def upgrade():
    # Create partition function
    op.execute("""
    CREATE OR REPLACE FUNCTION school_id_hash_partition(school_id integer) 
    RETURNS integer AS $$
    BEGIN
        RETURN school_id % 100;  -- 100 partitions
    END;
    $$ LANGUAGE plpgsql IMMUTABLE;
    """)

    # Partition students table
    op.execute("""
    CREATE TABLE students_partitioned (
        id SERIAL,
        school_id INTEGER NOT NULL,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (school_id, id)
    ) PARTITION BY HASH (school_id_hash_partition(school_id));
    """)

    # Create partitions
    for i in range(100):
        op.execute(f"""
        CREATE TABLE students_partition_{i} 
        PARTITION OF students_partitioned 
        FOR VALUES WITH (MODULUS 100, REMAINDER {i});
        """)

    # Add indexes
    op.execute("""
    CREATE INDEX idx_students_school_id ON students_partitioned(school_id);
    CREATE INDEX idx_students_email ON students_partitioned(email);
    """)

def downgrade():
    op.execute("DROP TABLE IF EXISTS students_partitioned CASCADE;")
    op.execute("DROP FUNCTION IF EXISTS school_id_hash_partition;")