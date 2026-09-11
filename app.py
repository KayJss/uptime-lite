from flask import Flask, jsonify, render_template, request

from monitor import check_url

app = Flask(__name__)

DEFAULT_TARGETS = [
    "https://example.com",
    "https://github.com",
]


@app.get("/")
def dashboard():
    raw_targets = request.args.get("targets", "")
    targets = [item.strip() for item in raw_targets.split(",") if item.strip()]
    if not targets:
        targets = DEFAULT_TARGETS

    results = []
    for target in targets[:10]:
        try:
            results.append(check_url(target).to_dict())
        except ValueError as exc:
            results.append({
                "url": target,
                "online": False,
                "status_code": None,
                "response_time_ms": None,
                "error": str(exc),
            })

    return render_template("index.html", results=results, targets=", ".join(targets))


@app.get("/api/check")
def api_check():
    url = request.args.get("url", "")
    try:
        return jsonify(check_url(url).to_dict())
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400


@app.get("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(debug=True)
