# Data Engineering Zoomcamp 2026

This repository contains my coursework and homework solutions for the [DataTalksClub Data Engineering Zoomcamp 2026](https://github.com/DataTalksClub/data-engineering-zoomcamp).

## 📚 Repository Structure

This repository follows a **branch-based organization** to keep homework and coursework separate:

- **`main`** branch: Contains this README and general repository information
- **`module-1`** branch: Module 1 content (Docker, Terraform, SQL)
- **`module-2`** branch: Module 2 content (Workflow Orchestration) - *Coming soon*
- **`module-3`** branch: Module 3 content (Data Warehouse) - *Coming soon*

## 🗂️ Module Organization

Within each module branch, you'll find:

```
module-X/
├── README.md                 # Module overview and homework solutions
├── homework/                 # Homework-specific files
│   ├── README.md            # Homework setup and instructions
│   ├── docker-compose.yaml  # Infrastructure setup
│   ├── sql_queries/         # SQL solutions
│   ├── scripts/             # Python ingestion scripts
│   └── data/                # Data files (gitignored)
└── coursework/              # Course notes and practice work
    ├── notes/
    └── exercises/
```

## 🚀 Getting Started

To view homework for a specific module:

```bash
# Clone the repository
git clone <your-repo-url>
cd data-engineering-zoomcamp

# Switch to the module branch
git checkout module-1

# Follow the module-specific README
cat README.md
```

## 📖 Modules

### Module 1: Introduction & Prerequisites
- **Branch**: `module-1`
- **Topics**: Docker, Terraform, SQL, PostgreSQL
- **Status**: ✅ Completed

### Module 2: Workflow Orchestration
- **Branch**: `module-2`
- **Topics**: Kestra, ETL pipelines
- **Status**: 🔄 In Progress

### Module 3: Data Warehouse
- **Branch**: `module-3`
- **Topics**: BigQuery, Data modeling
- **Status**: ⏳ Upcoming

## 🛠️ Technologies Used

- **Containerization**: Docker, Docker Compose
- **Databases**: PostgreSQL, pgAdmin
- **Programming**: Python 3.13
- **Infrastructure as Code**: Terraform
- **Data Processing**: pandas, pyarrow, SQLAlchemy
- **Version Control**: Git

## 📝 Notes

- Each module branch contains complete setup instructions
- Homework solutions include SQL queries and Python scripts
- Data files are excluded from version control (see `.gitignore`)
- All homework has been submitted and graded ✅

## 🔗 Resources

- [Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp)
- [Course Website](https://datatalks.club/blog/data-engineering-zoomcamp.html)
- [DataTalks.Club Community](https://datatalks.club/)

---

**Course**: Data Engineering Zoomcamp 2026  
**Cohort**: 2026  
**Instructor**: DataTalksClub
