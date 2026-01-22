import requests
from models.customer import Customer

FLASK_URL = "http://mock-server:5000/api/customers"

def ingest_customers(db):
    page = 1
    limit = 10
    processed = 0

    while True:
        r = requests.get(FLASK_URL, params={"page": page, "limit": limit})
        data = r.json()["data"]

        if not data:
            break

        for item in data:
            existing = db.get(Customer, item["customer_id"])
            if existing:
                for k, v in item.items():
                    setattr(existing, k, v)
            else:
                db.add(Customer(**item))
            processed += 1

        db.commit()
        page += 1

    return processed
