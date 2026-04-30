# Video Recorder App

A Flask-based video recording system where admins can create recording sessions and users can record videos through their browser.

## Features

- Admin panel to create recording sessions
- Unique recording links for each session
- Browser-based video recording with webcam
- Video upload and storage
- Admin verification system
- Secure video downloads

## Architecture

This app uses a **separated frontend/backend architecture**:
- **Frontend**: Static HTML/CSS/JS deployed to Netlify
- **Backend**: Flask API deployed to Heroku/Railway/Render

## Local Development

1. Clone the repository
2. Set up backend:
   ```bash
   cd backend  # (Flask app)
   python -m venv venv
   venv\Scripts\activate  # Windows
   pip install -r requirements.txt
   python app.py
   ```
3. Open frontend files (index.html, record.html) in browser

## Deployment

### Backend Deployment (Flask API)

Choose one of these platforms:

**Heroku:**
```bash
heroku create your-backend-name
git push heroku main
# Get the URL: https://your-backend-name.herokuapp.com
```

**Railway:**
1. Connect GitHub repo
2. Railway auto-detects Flask
3. Get deployment URL

**Render:**
1. Create Web Service
2. Set build command: `pip install -r requirements.txt`
3. Set start command: `python app.py`

### Frontend Deployment (Netlify)

1. **Update API URLs**: In `index.html` and `record.html`, replace:
   ```javascript
   const API_BASE = 'https://your-backend-url.herokuapp.com';
   ```
   With your actual backend URL.

2. **Deploy to Netlify**:
   - Go to https://netlify.com
   - Drag & drop the project folder, or connect GitHub
   - Netlify will auto-detect settings from `netlify.toml`
   - Get your frontend URL: `https://your-netlify-site.netlify.app`

## Usage

1. Visit the Netlify frontend URL
2. Click "Create New Recording Session"
3. Copy the generated link (points to backend)
4. Share the link with users
5. Users record videos through their browser
6. Admin views, verifies, and downloads recordings

## File Structure

```
/
├── index.html          # Admin panel (frontend)
├── record.html         # Recording page (frontend)
├── netlify.toml        # Netlify configuration
├── app.py             # Flask backend
├── requirements.txt   # Python dependencies
├── Procfile          # Heroku deployment
├── runtime.txt       # Python version
└── templates/        # Flask templates (backend only)
```

## Security Notes

- CORS is enabled for cross-origin requests
- File uploads are validated
- Database uses SQLite (upgrade to PostgreSQL for production)