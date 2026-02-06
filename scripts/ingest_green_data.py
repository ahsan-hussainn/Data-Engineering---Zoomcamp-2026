#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm
import click


def ingest_data(
        file_path: str,
        engine,
        target_table: str,
        chunksize: int = 100000,
) -> None:
    """
    Ingest parquet data into PostgreSQL database in chunks.
    
    Args:
        file_path: Path to the parquet file
        engine: SQLAlchemy engine
        target_table: Name of the target table
        chunksize: Number of rows per chunk
    """
    # Read parquet file in chunks
    parquet_file = pd.read_parquet(file_path)
    total_rows = len(parquet_file)
    
    print(f"Total rows to ingest: {total_rows}")
    
    # Create chunks manually since parquet doesn't support iterator
    chunks = [parquet_file[i:i+chunksize] for i in range(0, total_rows, chunksize)]
    
    # Create table with first chunk (no data)
    chunks[0].head(0).to_sql(
        name=target_table,
        con=engine,
        if_exists="replace",
        index=False
    )
    print(f"Table {target_table} created")
    
    # Insert first chunk
    chunks[0].to_sql(
        name=target_table,
        con=engine,
        if_exists="append",
        index=False
    )
    print(f"Inserted first chunk: {len(chunks[0])} rows")
    
    # Insert remaining chunks with progress bar
    for chunk in tqdm(chunks[1:], desc="Ingesting chunks"):
        chunk.to_sql(
            name=target_table,
            con=engine,
            if_exists="append",
            index=False
        )
    
    print(f'Done ingesting {total_rows} rows to {target_table}')


@click.command()
@click.option('--pg-user', default='root', help='PostgreSQL username')
@click.option('--pg-pass', default='root', help='PostgreSQL password')
@click.option('--pg-host', default='localhost', help='PostgreSQL host')
@click.option('--pg-port', default='5432', help='PostgreSQL port')
@click.option('--pg-db', default='ny_taxi', help='PostgreSQL database name')
@click.option('--file-path', default='data/green_tripdata_2025-11.parquet', help='Path to parquet file')
@click.option('--target-table', default='green_taxi_data', help='Target table name')
@click.option('--chunksize', default=100000, type=int, help='Chunk size for ingestion')
def main(pg_user, pg_pass, pg_host, pg_port, pg_db, file_path, target_table, chunksize):
    """Ingest green taxi parquet data into PostgreSQL."""
    
    # Create database engine
    engine = create_engine(f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}')
    
    print(f"Connecting to PostgreSQL at {pg_host}:{pg_port}/{pg_db}")
    print(f"Reading file: {file_path}")
    
    # Ingest data
    ingest_data(
        file_path=file_path,
        engine=engine,
        target_table=target_table,
        chunksize=chunksize
    )


if __name__ == '__main__':
    main()