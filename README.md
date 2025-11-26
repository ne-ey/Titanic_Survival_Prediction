Titanic Survival Prediction - Local UI + IBM AutoAI integration

Setup:
1. Create virtualenv: python -m venv venv
2. Activate:
   - Windows: venv\Scripts\activate
   - mac/linux: source venv/bin/activate
3. Install: pip install -r requirements.txt
4. Edit app.py: replace API_KEY and DEPLOYMENT_URL with your IBM credentials.
5. Run: python app.py
6. Open: http://127.0.0.1:5000

To create final ZIP:
From parent folder run:
  zip -r titanic_project.zip titanic_project
