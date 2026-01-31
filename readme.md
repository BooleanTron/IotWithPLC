# Real-Time PLC Monitoring & Control using OPC UA, Flask, and Supabase

This document describes an industrial automation mini-project that demonstrates real-time monitoring and control of PLC variables using OPC UA, a Python–Flask backend, a Supabase cloud database, and a web-based dashboard.

## Repository Structure

```
plc/
 └── plc_project.zip          Complete Siemens TIA Portal PLC project

pc/
 ├── app.py                   Flask server and API endpoints
 ├── plcMain.py               OPC UA read/write logic
 ├── config.py                Supabase configuration
 ├── requirements.txt         Python dependencies
 ├── templates/
 │   └── index.html           Web dashboard UI
 └── static/
     └── script.js            Frontend logic
```

## System Overview

### PLC Side:
- Siemens S7-1200 Series PLC
- TIA Portal V21
- OPC UA server enabled
- Variables:
  - VarInt (Integer)
  - VarFloat (Float)

### PC Side:
- Python OPC UA client
- Flask backend
- Supabase PostgreSQL database
- Web dashboard

## Data Flow

**Read:**
```
PLC → OPC UA → Python Backend → Supabase → Flask API → Dashboard
```

**Write:**
```
Dashboard → Flask API → Python Backend → OPC UA → PLC
```

## Requirements

- Siemens TIA Portal V21
- UA Expert
- Siemens S7-1200 PLC
- Python 3.9+

### Python Dependencies:
- flask
- opcua
- supabase
- python-dateutil

## Configuration

Supabase credentials are loaded from `config.py`:
- `SUPABASE_URL`
- `SUPABASE_API_KEY`

## How to Run

1. Import `plc_project.zip` into TIA Portal
2. Enable OPC UA and expose variables
3. Install Python dependencies
4. Run `app.py`
5. Open http://127.0.0.1:5000

## Supabase Table (plcVariables)

- `id` (int)
- `variable_name` (text)
- `value` (numeric)
- `updated_at` (timestamp)

---

This project demonstrates an end-to-end industrial data pipeline integrating real PLC hardware with cloud and web technologies.

**License:** Educational and demonstration purposes.