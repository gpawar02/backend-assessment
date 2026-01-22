from flask import Flask, jsonify, request, abort
import json

app = Flask(__name__)

with open("data/customers.json") as f:
    CUSTOMERS = json.load(f)

@app.route("/api/health")
def health():
    return {"status": "ok"}

@app.route("/api/customers")
def get_customers():
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 10))

    start = (page - 1) * limit
    end = start + limit

    return jsonify({
        "data": CUSTOMERS[start:end],
        "total": len(CUSTOMERS),
        "page": page,
        "limit": limit
    })

@app.route("/api/customers/<customer_id>")
def get_customer(customer_id):
    customer = next((c for c in CUSTOMERS if c["customer_id"] == customer_id), None)
    if not customer:
        abort(404)
    return jsonify(customer)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
