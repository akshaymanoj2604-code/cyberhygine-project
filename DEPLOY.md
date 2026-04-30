# Deploy Script for Video Recorder App

## Auto-Detection Troubleshooting

If platforms aren't auto-detecting your app, try these solutions:

### Railway Auto-Detection Issues
1. **Check railway.json**: Make sure `railway.json` exists in your repo root
2. **Force Python**: Railway should detect Python automatically, but you can specify it
3. **Check build logs**: Look for Python detection messages in deployment logs

### Heroku Auto-Detection Issues
1. **Check Procfile**: Ensure `Procfile` exists with correct syntax
2. **Check runtime.txt**: Python version should be supported (3.8-3.12)
3. **Check requirements.txt**: Must exist and be valid
4. **Alternative Procfile**: If gunicorn fails, rename `Procfile.alt` to `Procfile`

### Render Auto-Detection Issues
1. **Check render.yaml**: Should auto-detect from this file
2. **Manual setup**: Select "Python" runtime manually
3. **Check build/start commands**: Ensure they're correct

### Netlify Auto-Detection Issues
1. **Check netlify.toml**: Should exist in repo root
2. **Publish directory**: Set to "." (current directory)
3. **Build command**: Should be "echo 'No build step required'"
4. **Manual setup**: Configure build settings manually in Netlify dashboard

## Step 1: Deploy Backend (Flask API)

Choose one platform:

### Option A: Railway (Recommended)
```bash
# Push to GitHub first
git add .
git commit -m "Add deployment files"
git push origin main

# Then deploy on Railway:
# 1. Connect GitHub repo
# 2. Railway should auto-detect Python/Flask
# 3. If not, check railway.json file
```

### Option B: Render
```bash
# render.yaml should handle auto-detection
# If issues, manually select Python runtime
```

### Option C: Heroku
```bash
# Should auto-detect from Procfile and requirements.txt
heroku create your-video-recorder-backend
git push heroku main
```

## Step 2: Update Frontend API URLs

Run the helper script:
```bash
update_urls.bat
```

## Step 3: Deploy Frontend to Netlify

```bash
# Push to GitHub
git add .
git commit -m "Update API URLs"
git push origin main

# Netlify should auto-detect from netlify.toml
# If not, manually set:
# - Build command: echo 'No build step required'
# - Publish directory: .
```

## Common Auto-Detection Fixes

### For Railway:
- Ensure `railway.json` is in root
- Check that `requirements.txt` exists
- Make sure `app.py` is in root

### For Heroku:
- Ensure `Procfile` starts with "web: "
- Check `runtime.txt` has valid Python version
- Verify `requirements.txt` is not empty

### For Render:
- `render.yaml` should handle everything
- If not, select "Python 3" manually

### For Netlify:
- `netlify.toml` should be auto-detected
- If not, set publish directory to "."