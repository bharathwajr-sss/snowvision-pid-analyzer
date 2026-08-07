# snowvision-pid-analyzer
Snowflake Pipeline ID Detection Repository
# SnowVision P&ID Analyzer

## Overview

SnowVision P&ID Analyzer is an AI-powered application built on **Snowflake**, **Snowpark Python**, **Streamlit**, and **OpenCV** that automatically analyzes Piping and Instrumentation Diagram (P&ID) images.

The application extracts:

- Pipelines
- Equipment
- Valves
- Instruments
- OCR Text
- Equipment Connections

The processed information is stored in Snowflake and an annotated image is generated for visualization.

---

# Features

- Upload P&ID images
- Detect pipelines
- Detect equipment symbols
- OCR for equipment tags
- Build equipment connection graph
- Generate annotated image
- Store metadata in Snowflake
- Streamlit dashboard
- Snowflake Native App

---

# Technology Stack

| Component | Technology |
|-----------|------------|
| Database | Snowflake |
| Compute | Snowpark Python |
| UI | Streamlit |
| Image Processing | OpenCV |
| OCR | EasyOCR |
| Graph | NetworkX |
| AI | Snowflake Cortex (Future) |

---

# Project Structure

```
snowvision-pid-analyzer/

config/
docs/
python/
sql/
streamlit/
sample_images/
expected_output/
tests/
```

---

# Project Workflow

```
Upload Image

↓

Preprocessing

↓

Line Detection

↓

Shape Detection

↓

OCR

↓

Equipment Detection

↓

Connection Detection

↓

Annotated Image

↓

Snowflake Tables

↓

Dashboard
```

---

# Current Status

✅ Milestone 1 Completed

🔄 Milestone 2 In Progress

---

# License

MIT License