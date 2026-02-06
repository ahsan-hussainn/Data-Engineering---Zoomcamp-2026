#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from sqlalchemy import create_engine
import click


def ingest_data(
        file_path: str,
        engine,
        target_table: str,
) -> None:
    """
    Ingest CSV zone lookup data into PostgreSQL database.
    
    Args:
        file_path: Path to the CSV file
        engine: SQLAlchemy engine
        target_table: Name of the target table
    """
    # Read CSV file (small file, no need for chunks)
    df = pd.read_csv(file_path)
    
    print(f"Total rows to ingest: {len(df)}")
    print(f"\nData preview:")
    print(df.head())
    
    # Insert data into PostgreSQL
    df.to_sql(
        name=target_table,
        con=engine,
        if_exists="replace",
        index=False
    )
    
    print(f'\nDone ingesting {len(df)} rows to {target_table}')


@click.command()
@click.option('--pg-user', default='root', help='PostgreSQL username')
@click.option('--pg-pass', default='root', help='PostgreSQL password')
@click.option('--pg-host', default='localhost', help='PostgreSQL host')
@click.option('--pg-port', default='5432', help='PostgreSQL port')
@click.option('--pg-db', default='ny_taxi', help='PostgreSQL database name')
@click.option('--file-path', default='data/taxi_zone_lookup.csv', help='Path to CSV file')
@click.option('--target-table', default='taxi_zones', help='Target table name')
def main(pg_user, pg_pass, pg_host, pg_port, pg_db, file_path, target_table):
    """Ingest taxi zone lookup CSV data into PostgreSQL."""
    
    # Create database engine
    engine = create_engine(f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}')
    
    print(f"Connecting to PostgreSQL at {pg_host}:{pg_port}/{pg_db}")
    print(f"Reading file: {file_path}")
    
    # Ingest data
    ingest_data(
        file_path=file_path,
        engine=engine,
        target_table=target_table
    )


if __name__ == '__main__':
    main()