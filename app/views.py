import secrets
from flask import render_template, request, redirect, flash
from app import app
from .rvp import pvr
from .algo import finalList

@app.route("/", methods=["GET", "POST"])
def index():
    secret_key = secrets.token_hex(16)
    app.config["SECRET_KEY"] = secret_key

    if request.method == "POST":
        req = request.form

        percentile = req["percentile"]
        rank = req["rank"]
        university = req["university"]
        pwd = req["pwd"]
        gender = req["gender"]
        category = req["category"]
        sortby = str(req["sortby"])
        branch = req["branch"]  # New line to retrieve branch from form

        if percentile == "" and rank == "":
            flash("Please enter either your Rank or your Percentile", 'error')
            return redirect(request.url)

        if rank == "":
            ranks = pvr(float(percentile), pwd, category)
            ranks = int(ranks)

            if ranks <= 0:
                ranks = 2
            result = finalList(ranks, float(percentile), category, university, gender, pwd, sortby, branch)

        if rank:
            result = finalList(int(rank), percentile, category, university, gender, pwd, sortby, branch)
            ranks = rank

        # Print the result DataFrame for debugging
        print(result)

        # Pass 'result' to the template context
        return render_template("public/result.html", ranks=ranks, category=category, result=result)

    return render_template("public/index.html")
