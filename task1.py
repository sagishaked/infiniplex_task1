from flask import Flask, render_template, request, redirect, flash
import pandas as pd
import os
import datetime
import webbrowser

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed for flash messages
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Store uploaded data
data_store = pd.DataFrame(columns=["Date/Time", "Patient ID", "Outcome"])

@app.route("/", methods=["GET", "POST"])
def index():
    global data_store

    if request.method == "POST":
        if "file" in request.files:
            file = request.files["file"]
            if not file:
                flash("No file uploaded", "error")
                return redirect("/")

            try:
                df = pd.read_csv(file)
                if set(df.columns) != {"Patient ID", "Outcome"}:
                    raise ValueError("Invalid CSV format. Required columns: Patient ID, Outcome")

                # Add timestamp to track the latest entry
                df["Date/Time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # Append new data
                data_store = pd.concat([data_store, df], ignore_index=True)

                # Keep only the last entry for each Patient ID (most recent)
                data_store = data_store.sort_values("Date/Time").groupby("Patient ID", as_index=False).last()

            except Exception as e:
                flash(f"Error: {str(e)}", "error")
                return redirect("/")

    # Get sorting preferences
    primary_sort = request.args.get("sort", "Date/Time")
    order = request.args.get("order", "desc")
    ascending = order == "asc"

    data_store.sort_values(by=[primary_sort], ascending=ascending, inplace=True)

    return render_template("index.html", files=data_store.to_dict("records"), current_sort=primary_sort, current_order=order)


if __name__ == "__main__":
    from threading import Timer


    def open_browser():
        webbrowser.open("http://127.0.0.1:5000/")


    Timer(1, open_browser).start()

    app.run(debug=True, host='0.0.0.0', port=5000)
