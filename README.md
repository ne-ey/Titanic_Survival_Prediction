---

# 🚢 Titanic Survival Prediction

### **A Cinematic Flask Web App Powered by IBM Watson AutoAI**

![App Screenshot](![alt text](image.png))

This project predicts whether a Titanic passenger would survive or not using a machine learning model deployed with **IBM Watson AutoAI**.
The interface is designed as a **cinematic recreation of the Titanic night** — deep ocean, moonlight, fog, cold wind, animated waves, and a floating Titanic hero image.

This is a unique blend of **Machine Learning + Cloud Deployment + Immersive UI/UX design**.

---

## ⭐ Features

### 🎨 **Cinematic Frontend**

* Deep ocean + night sky theme
* Realistic **animated waves** (foreground + background layers)
* Floating **Titanic hero image**
* Fog, mist, cold wind & moonlight
* Iceberg glow on both sides
* Frosted glass animated form UI

### 🤖 **IBM AutoAI Model**

* Auto-trained classification model
* Deployed on IBM Cloud Machine Learning
* Results fetched via REST API

### ✨ **Prediction Animations**

* ❄️ Snow animation → **Survived**
* 💀 Skull rain effect → **Not Survived**

### ⚡ **Modern Architecture**

* AJAX-based prediction (no page reload)
* Clean and responsive UI

---

## 📸 Preview

> Replace this link after uploading your screenshot to GitHub or imgur:
> `![Preview Screenshot](YOUR_SCREENSHOT_URL_HERE)`

---

## 🛠 Technology Stack

| Component        | Technology                             |
| ---------------- | -------------------------------------- |
| **Frontend**     | HTML, CSS, JavaScript, Bootstrap       |
| **Backend**      | Flask (Python)                         |
| **Model**        | IBM Watson AutoAI                      |
| **Design Style** | Cinematic ocean + glassmorphism        |
| **Deployment**   | IBM Cloud ML API                       |
| **Animations**   | CSS keyframes + custom JS (effects.js) |

---

## 📂 Project Structure

```
Titanic_Survival_Prediction/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── effects.js
│   └── assets/
│       ├── titanic.jpg
│       ├── wave.png
│       └── stars.png
│
└── venv/ (not uploaded)
```

---

## ⚙️ Setup Instructions

### 1️⃣ Create Virtual Environment

#### Windows

```sh
python -m venv venv
venv\Scripts\activate
```

#### Mac / Linux

```sh
python3 -m venv venv
source venv/bin/activate
```

---

### 2️⃣ Install Dependencies

```sh
pip install -r requirements.txt
```

---

### 3️⃣ Add IBM Credentials

Create a `.env` file:

```
IBM_API_KEY=your_api_key_here
IBM_DEPLOYMENT_URL=your_autoai_endpoint_url
```

💡 *Important:* `.env` is **ignored** using `.gitignore`.

---

### 4️⃣ Run the Web App

```sh
python app.py
```

Visit:
👉 **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## 📡 Prediction Workflow

```
User Input →
Flask →
IBM Watson AutoAI Model →
JSON Response →
Animated UI Result (snow / skull) →
Display Probability
```

---

## 🎯 Objective of This Project

* Build a full ML pipeline using IBM AutoAI
* Connect cloud-deployed model with a Flask frontend
* Deliver predictions using an immersive Titanic-themed interface
* Demonstrate ML + UI/UX storytelling

---

## 🤝 Contribution

Suggestions, UI improvements & PRs are welcome!

---

## 📜 License

MIT License (optional — add if required)

---


