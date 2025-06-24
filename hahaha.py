from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        secim = request.form.get("secim")
        if secim:  # boş değilse
            try:
                with open("secimler.txt", "a", encoding="utf-8") as f:
                    f.write(secim + "\n")
                print("YAZILDI:", secim)
            except Exception as e:
                print("YAZMA HATASI:", e)
        else:
            print("SECİM GELMEDİ")
        return redirect("/")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
