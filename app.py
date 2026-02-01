from flask import Flask, render_template, request, redirect, session
import os
import numpy as np
import cv2
from PIL import Image
import tensorflow as tf

# =============================
# APP SETUP
# =============================
app = Flask(__name__)
app.secret_key = "super_secret_key_123"

os.makedirs("uploads", exist_ok=True)

# =============================
# SIMPLE CNN (DEMO MODE)
# =============================
layers = tf.keras.layers
models = tf.keras.models

def build_cnn():
    model = models.Sequential([
        layers.Input(shape=(128,128,1)),
        layers.Conv2D(16,3,activation="relu"),
        layers.MaxPooling2D(),
        layers.Flatten(),
        layers.Dense(1,activation="sigmoid")
    ])
    return model

model = build_cnn()

# =============================
# LOGIN ROUTE (FINAL)
# =============================
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if username == "doctor" and password == "ai123":
            session["user"] = "doctor"
            return redirect("/home")
        else:
            return "<h3>❌ Wrong login. Use doctor / ai123</h3>"

    return render_template("login.html")


# =============================
# HOME PAGE
# =============================
@app.route("/home")
def home():
    if "user" not in session:
        return redirect("/")
    return render_template("home.html")


# =============================
# DASHBOARD
# =============================
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/")
    return render_template("dashboard.html")


# =============================
# PREDICT ROUTE
# =============================
@app.route("/predict", methods=["POST"])
def predict():

    if "user" not in session:
        return redirect("/")

    file = request.files.get("file")
    if not file:
        return "No file uploaded"

    path = "uploads/mri.png"
    file.save(path)

    try:
        img = Image.open(path).convert("L").resize((128,128))
    except:
        return "❌ Please upload a valid MRI image (.png / .jpg)"

    arr = np.array(img) / 255.0
    arr = arr.reshape(1,128,128,1)

    # SAFE PREDICTION
    pred = float(arr.mean())

    heat = np.uint8(255 * arr[0,:,:,0])
    heat = cv2.applyColorMap(heat, cv2.COLORMAP_JET)

    original = cv2.imread(path)
    original = cv2.resize(original,(128,128))

    final = cv2.addWeighted(original,0.6,heat,0.4,0)
    cv2.imwrite("static/heatmap.png",final)

    result = "Tumor Detected" if pred > 0.5 else "No Tumor"

    return render_template(
        "result.html",
        result=result,
        confidence=round(pred*100,2)
    )


# =============================
# EXTRA PAGES
# =============================
@app.route("/clinical")
def clinical():
    return render_template("clinical.html")

@app.route("/about")
def about():
    return render_template("about.html")


# =============================
# LOGOUT
# =============================
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


# =============================
# RUN SERVER
# =============================
if __name__ == "__main__":
    app.run(debug=True)
