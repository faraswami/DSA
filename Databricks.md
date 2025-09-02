1. How does Delta Lake ensure ACID transactions on cloud object stores?

Answer:

Cloud object stores (S3/ADLS/GCS) are eventually consistent and don’t support transactions.

Delta Lake introduces a transaction log (_delta_log) stored alongside the data.

Every write operation creates a new JSON/Parquet commit file in _delta_log with atomic metadata.

Writers use an optimistic concurrency protocol:

Read latest transaction log → Propose changes → Write commit atomically.

If conflict, retry with updated state.

This ensures Atomicity, Consistency, Isolation, Durability across multiple readers/writers.

2. Unity Catalog vs Hive Metastore – differences & migration challenges?

Answer:

Hive Metastore: Legacy, workspace-level, supports table/DB metadata only.

Unity Catalog:

Centralized across all workspaces.

RBAC at catalog, schema, table, column, row levels.

Lineage tracking, audit logging, Delta Sharing.

Migration challenges:

Schema name conflicts.

Updating legacy scripts (Hive → UC).

Permissions need to be remapped (workspace → centralized RBAC).

External tables and unmanaged data need careful handling.

3. How do you optimize a large Delta table with skewed data?

Answer:

Identify skew via query profiles or DESCRIBE EXTENDED.

Optimizations:

Use Z-ORDER BY on frequently filtered columns.

Repartition by high-cardinality keys, avoid small files.

Use salting to distribute skewed keys.

Apply OPTIMIZE for compaction + VACUUM for cleanup.

Enable data skipping indexes in Delta.

For streaming: set proper shuffle partitions and use Adaptive Query Execution (AQE).

4. When would you use Autoloader vs Structured Streaming?

Answer:

Autoloader (cloudFiles):

Best for ingesting files (CSV/JSON/Parquet) from cloud storage.

Incremental discovery with scalable metadata (avoids listing millions of files).

Handles schema inference + evolution automatically.

Structured Streaming:

Best for real-time event streams (Kafka, Event Hub, IoT).

Micro-batch or continuous processing.

Supports complex stateful operations like joins, aggregations, watermarking.
👉 If input is files landing in storage → use Autoloader. If real-time event stream → use Structured Streaming.

5. Explain Z-Ordering vs Partitioning trade-offs.

Answer:

Partitioning:

Physically separates data by a column (e.g., year, region).

Good for low-cardinality, high-filter columns.

Over-partitioning = too many small files → performance issues.

Z-Ordering:

Multi-dimensional clustering technique on Delta tables.

Co-locates related records in the same set of files.

Works well for high-cardinality columns (e.g., user_id).

Trade-off:

Partition on low-cardinality, predictable filters.

Z-Order for high-cardinality, unpredictable filters.

6. How to handle schema evolution in Delta tables?

Answer:

Enable mergeSchema when writing new data.

Use ALTER TABLE … ADD COLUMN for controlled evolution.

Maintain backward compatibility (nullable new columns).

Track schema history with DESCRIBE HISTORY.

For complex evolution:

Create new versioned table → Migrate data gradually.

Ensure BI tools / downstream jobs can handle changes.

7. Describe an end-to-end lakehouse architecture you’ve implemented.

Answer:
(Example answer you can adapt to your experience)

Raw data ingestion: Autoloader for cloud storage + Kafka streaming into Bronze Delta tables.

Bronze layer: Raw, append-only, minimal transformations.

Silver layer: Cleaned, schema enforced, deduplicated, joined datasets.

Gold layer: Aggregated business-level tables (sales KPIs, customer churn models).

Governance: Unity Catalog for access, secret scopes for credentials.

Optimization: Z-Ordering on customer_id, partitioning by date.

Consumption: Power BI + Databricks SQL dashboards.

ML/AI: MLflow for model tracking, Delta Feature Store for serving features.

🆕 Additional Senior-Level Questions
8. How do you debug and optimize a slow Spark job in Databricks?

Answer:

Check Spark UI for stages, shuffle size, skew.

Optimize:

Increase/decrease spark.sql.shuffle.partitions.

Use broadcast joins for small tables.

Avoid UDFs where possible, use built-in Spark functions.

Cache intermediate data if reused.

Enable AQE (Adaptive Query Execution).

9. How do you ensure data quality in Databricks pipelines?

Answer:

Apply schema validation in Autoloader.

Use Delta constraints (NOT NULL, CHECK).

Build unit tests with PySpark testing frameworks.

Add expectations with tools like Great Expectations or Databricks Delta Live Tables (DLT) expectations.

10. How do you secure PII data in Databricks?

Answer:

Unity Catalog column-level masking or row-level filters.

Store sensitive values encrypted in storage (e.g., ADLS with CMK).

Use hashed/pseudonymized keys in analytics layers.

Manage secrets via Databricks Secret Scopes / Key Vault.

Enforce access policies via RBAC (no developer has access to production data).

11. How do you design cost-efficient Databricks pipelines?

Answer:

Use spot instances for clusters.

Autoscaling clusters.

Turn off clusters with auto-termination.

Use Photon Engine for SQL workloads.

Optimize storage with file compaction (OPTIMIZE).

Minimize shuffle → repartition smartly.

12. What are Change Data Feed (CDF) use cases in Delta Lake?

Answer:

Capture inserts/updates/deletes between versions of a Delta table.

Use cases:

Downstream incremental ETL (instead of full refresh).

Change capture for ML features.

Sync with external systems (Snowflake, Synapse, APIs).

13. How do you handle multi-cloud data governance in Databricks?

Answer:

Unity Catalog centralizes across AWS, Azure, GCP.

Policies applied uniformly → RBAC, lineage, audits.

Use Delta Sharing for external partners securely.
