import mysql.connector
import json
from datetime import datetime

mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="",
                               database="ccas_db")


def fetch_rows():
    cur = mydb.cursor()
    query = """
            SELECT a.call_id, a.datetime, b.operator_name, a.emotion, a.sentiment, a.call_score, c.topic_name, d.intent_name 
            FROM uploaded_calls as a INNER JOIN operators b, topics c, intent d
            WHERE a.operator_id = b.operator_id AND a.topic_id = c.topic_id AND a.intent_id = d.intent_id
            ORDER BY a.datetime
            """
    cur.execute(query)

    results = {}

    for (call_id, datetime, operator_name, emotion, sentiment, call_score, topic_name, intent_name) in cur:
        results[str(call_id)] = {
            "datetime": datetime.strftime("%d/%b %I:%M %p")}
        results[str(call_id)].update(
            {"operator": str(operator_name).capitalize()})
        results[str(call_id)].update({"emotion": str(emotion).capitalize()})
        results[str(call_id)].update(
            {"sentiment": str(sentiment).capitalize()})
        results[str(call_id)].update(
            {"call_score": round(call_score * 100, 2)})
        results[str(call_id)].update({"topic": str(topic_name).capitalize()})
        results[str(call_id)].update({"intent": str(intent_name).capitalize()})

    print(results)
    cur.close()

    return results


if __name__ == "__main__":
    fetch_rows()
