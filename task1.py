from flask import Flask, render_template, request, redirect, flash
import pandas as pd
import os
import datetime
import webbrowser

app = Flask(__name__)

# store uploaded data
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
            # Check if the file has a .csv extension
            if not file.filename.endswith(".csv"):
                flash("Invalid file type. Please upload a CSV file.", "error")
                return redirect("/")

            try:
                df = pd.read_csv(file)

                if set(df.columns) != {"Patient ID", "Outcome"}:
                    raise ValueError("Invalid CSV format. Required columns: Patient ID, Outcome")

                df["Patient ID"] = df["Patient ID"].astype(str)

                # add timestamp to track the latest entry
                df["Date/Time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # append new data
                data_store = pd.concat([data_store, df], ignore_index=True)

                # Sort by Date/Time (latest first)
                data_store = data_store.sort_values("Date/Time", ascending=False)

                # Mark the most recent record for each Patient ID
                data_store["is_latest"] = False  # Default to False for all
                latest_entries = data_store.groupby("Patient ID").head(1)  # Get latest for each patient
                data_store.loc[latest_entries.index, "is_latest"] = True  # Set latest as True                                                                          as_index=False).first()


            except Exception as e:

                flash(f"Error: The CSV is malformed. {str(e)}", "error")

                return render_template("index.html", files=data_store.to_dict("records"), current_sort="Date/Time",
                                       current_order="desc")

    # get sorting preferences
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
