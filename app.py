from flask import Flask, render_template, jsonify
from database import load_jobs_from_db

app = Flask(__name__)

@app.route("/")
def hello_world():
    # Handle the root route ("/") and render the "home.html" template with the loaded jobs.
    # Load the jobs from the database using the load_jobs_from_db() function
    JOBS = load_jobs_from_db()

    # Render the "home.html" template and pass the loaded jobs as a variable named "jobs"
    return render_template("home.html", jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    # Handle the "/api/jobs" route and return the loaded jobs as a JSON response.
    # Load the jobs from the database using the load_jobs_from_db() function
    JOBS = load_jobs_from_db()

    # Return the loaded jobs as a JSON response
    return jsonify(JOBS)


if __name__ == "__main__":
    # Run the Flask application in debug mode, listening on all available network interfaces.
    app.run(host="0.0.0.0", debug=True)