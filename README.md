# Module 1: Introduction & Prerequisites

This module covers the fundamentals of containerization, databases, and infrastructure as code.

## 📋 Topics Covered

- Docker & Docker Compose
- PostgreSQL database setup
- SQL queries for data analysis
- Python data ingestion scripts
- Terraform basics
- Git version control

## 🎯 Homework Solutions

### Question 1: Understanding Docker Images
**Question**: What's the version of `pip` in the `python:3.13` image?

**Answer**: **24.3.1**

**Solution**:
```bash
docker run -it --entrypoint bash python:3.13
pip --version
```

---

### Question 2: Understanding Docker Networking
**Question**: What hostname and port should pgAdmin use to connect to the postgres database?

**Answer**: **db:5432**

**Explanation**: Inside the Docker network, containers communicate using service names as hostnames, and the internal port (5432), not the mapped external port (5433).

---

### Question 3: Counting Short Trips
**Question**: How many trips had a `trip_distance` ≤ 1 mile in November 2025?

**Answer**: **8,254**

**SQL Query**: See [`homework/sql_queries/question_3.sql`](homework/sql_queries/question_3.sql)

---

### Question 4: Longest Trip for Each Day
**Question**: Which day had the longest trip distance (excluding trips ≥100 miles)?

**Answer**: **2025-11-23**

**SQL Query**: See [`homework/sql_queries/question_4.sql`](homework/sql_queries/question_4.sql)

---

### Question 5: Biggest Pickup Zone
**Question**: Which pickup zone had the largest `total_amount` on November 18th, 2025?

**Answer**: **East Harlem North**

**SQL Query**: See [`homework/sql_queries/question_5.sql`](homework/sql_queries/question_5.sql)

---

### Question 6: Largest Tip
**Question**: For pickups in "East Harlem North" in November 2025, which dropoff zone had the largest tip?

**Answer**: **JFK Airport**

**SQL Query**: See [`homework/sql_queries/question_6.sql`](homework/sql_queries/question_6.sql)

---

### Question 7: Terraform Workflow
**Question**: Which sequence describes the Terraform workflow for:
1. Downloading provider plugins and setting up backend
2. Generating proposed changes and auto-executing the plan
3. Removing all resources

**Answer**: **terraform init, terraform apply -auto-approve, terraform destroy**

---

## 🚀 Setup Instructions

### Prerequisites
- Docker & Docker Compose installed
- Python 3.13+ with `uv` package manager
- At least 2GB free disk space

### 1. Navigate to Homework Directory

```bash
cd homework/
```

### 2. Start Docker Services

```bash
docker-compose up -d
```

This will start:
- PostgreSQL database (port 5432)
- pgAdmin (port 8085)

### 3. Install Python Dependencies

```bash
uv sync
```

### 4. Download Data Files

```bash
# Green taxi data (November 2025)
wget https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-11.parquet

# Taxi zone lookup
wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv

# Move to data directory
mkdir -p data
mv green_tripdata_2025-11.parquet data/
mv taxi_zone_lookup.csv data/
```

### 5. Ingest Data

```bash
# Ingest taxi zones
python scripts/ingest_zones.py

# Ingest green taxi trips
python scripts/ingest_green_taxi.py
```

### 6. Access pgAdmin

1. Open browser: http://localhost:8085
2. Login:
   - Email: `admin@admin.com`
   - Password: `root`
3. Add New Server:
   - Name: `Local Postgres`
   - Host: `pgdatabase` (service name from docker-compose)
   - Port: `5432`
   - Username: `root`
   - Password: `root`

### 7. Run SQL Queries

Execute the queries in the `sql_queries/` directory using pgAdmin's Query Tool.

---

## 📁 Directory Structure

```
module-1/
├── README.md                          # This file
├── homework/
│   ├── README.md                      # Detailed setup guide
│   ├── docker-compose.yaml            # Docker infrastructure
│   ├── sql_queries/                   # SQL solutions
│   │   ├── question_3.sql
│   │   ├── question_4.sql
│   │   ├── question_5.sql
│   │   └── question_6.sql
│   ├── scripts/                       # Python scripts
│   │   ├── ingest_green_taxi.py
│   │   └── ingest_zones.py
│   └── data/                          # Data files (gitignored)
│       ├── green_tripdata_2025-11.parquet
│       └── taxi_zone_lookup.csv
└── coursework/                        # Course notes (optional)
```

---

## 🛠️ Technologies Used

- **Docker**: Container platform
- **PostgreSQL 18**: Relational database
- **pgAdmin 4**: Database administration tool
- **Python 3.13**: Data ingestion
- **pandas**: Data manipulation
- **SQLAlchemy**: Database ORM
- **pyarrow**: Parquet file handling

---

## 🐛 Troubleshooting

### Database Connection Issues
```bash
# Check if containers are running
docker-compose ps

# View logs
docker-compose logs pgdatabase
docker-compose logs pgadmin
```

### Data Ingestion Errors
```bash
# Ensure database is ready
docker-compose exec pgdatabase pg_isready

# Check Python dependencies
uv sync
```

### Port Already in Use
```bash
# Stop existing containers
docker-compose down

# Remove volumes (if needed)
docker-compose down -v
```

---

## 📚 Resources

- [Docker Documentation](https://docs.docker.com/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Module 1 Videos](https://www.youtube.com/playlist?list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb)

---

## ✅ Homework Submission

Homework has been submitted and graded. All questions answered correctly! 🎉
