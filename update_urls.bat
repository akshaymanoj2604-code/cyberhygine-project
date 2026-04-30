@echo off
echo Video Recorder Deployment Helper
echo ================================
echo.
echo This script will help you update the API URLs in your frontend files.
echo.
set /p backend_url="Enter your backend URL (e.g., https://your-app.herokuapp.com): "

echo.
echo Updating index.html...
powershell -Command "(Get-Content index.html) -replace 'https://your-backend-url\.herokuapp\.com', '%backend_url%' | Set-Content index.html"

echo Updating record.html...
powershell -Command "(Get-Content record.html) -replace 'https://your-backend-url\.herokuapp\.com', '%backend_url%' | Set-Content record.html"

echo.
echo API URLs updated successfully!
echo.
echo Next steps:
echo 1. Commit and push changes to GitHub
echo 2. Deploy frontend to Netlify
echo 3. Test your application
echo.
pause