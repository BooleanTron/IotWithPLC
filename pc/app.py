from flask import Flask, render_template, jsonify, request
from supabase import create_client
import threading
import time
from datetime import datetime

from config import SUPABASE_URL, SUPABASE_API_KEY
from plcMain import readInt, readFloat, WriteInt, WriteFloat

# -------------------------------------------------
# APP INIT
# -------------------------------------------------
app = Flask(__name__)

# -------------------------------------------------
# SUPABASE INIT
# -------------------------------------------------
supabase = create_client(SUPABASE_URL, SUPABASE_API_KEY)
TABLE = "plcvariables"

# -------------------------------------------------
# PLC → SUPABASE CONTINUOUS LOOP
# -------------------------------------------------
def plc_reader():
    while True:
        try:
            var_int = int(readInt()[0])
            var_float = float(readFloat()[0])
            now = datetime.utcnow().isoformat()

            supabase.table(TABLE).upsert(
                [
                    {
                        "variable_name": "VarInt",
                        "value": var_int,
                        "last_updated": now
                    },
                    {
                        "variable_name": "VarFloat",
                        "value": var_float,
                        "last_updated": now
                    }
                ],
                on_conflict="variable_name"
            ).execute()

        except Exception as e:
            print("PLC error:", e)

        time.sleep(1)  # 1 second scan rate


# Start PLC thread
threading.Thread(target=plc_reader, daemon=True).start()

# -------------------------------------------------
# ROUTES
# -------------------------------------------------
@app.route("/")
def index():
    return render_template("index.html")

# ---------- READ VALUES ----------
@app.route("/api/values", methods=["GET"])
def values():
    res = supabase.table(TABLE) \
        .select("*") \
        .order("variable_name") \
        .execute()
    return jsonify(res.data)

# ---------- WRITE VALUES ----------
@app.route("/api/write", methods=["POST"])
def write():
    data = request.json
    now = datetime.utcnow().isoformat()

    # Write INT
    if data.get("VarInt") not in [None, ""]:
        val = int(data["VarInt"])
        WriteInt(val)

        supabase.table(TABLE).update({
            "value": val,
            "last_updated": now
        }).eq("variable_name", "VarInt").execute()

    # Write FLOAT
    if data.get("VarFloat") not in [None, ""]:
        val = float(data["VarFloat"])
        WriteFloat(val)

        supabase.table(TABLE).update({
            "value": val,
            "last_updated": now
        }).eq("variable_name", "VarFloat").execute()

    return jsonify({"status": "ok"})

# -------------------------------------------------
# RUN
# -------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
