import redis
import json
import sqlite3

r = redis.Redis(host="redis", port=6379, decode_responses=True)

conn = sqlite3.connect("/data/events.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS events (
    timestamp TEXT,
    service TEXT,
    latency REAL,
    mode TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS anomalies (
    timestamp TEXT,
    service TEXT,
    latency REAL,
    reason TEXT
)
""")

conn.commit()

while True:
    _, raw = r.blpop("events")
    event = json.loads(raw)

    cur.execute(
        "INSERT INTO events VALUES (?, ?, ?, ?)",
        (event["timestamp"], event["service"], event["latency"], event["mode"])
    )

    if event["latency"] > 500:
        cur.execute(
            "INSERT INTO anomalies VALUES (?, ?, ?, ?)",
            (event["timestamp"], event["service"], event["latency"], "high_latency")
        )

    conn.commit()
