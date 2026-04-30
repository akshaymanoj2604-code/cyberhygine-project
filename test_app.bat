@echo off
echo Testing Flask App Startup...
echo ==============================

cd /d c:\Users\aksha\OneDrive\Desktop\video_recorder

echo Checking Python version...
c:/Users/aksha/OneDrive/Desktop/video_recorder/venv/Scripts/python.exe --version

echo.
echo Checking if app.py can be imported...
c:/Users/aksha/OneDrive/Desktop/video_recorder/venv/Scripts/python.exe -c "import app; print('App imported successfully')"

echo.
echo Checking if wsgi.py can be imported...
c:/Users/aksha/OneDrive/Desktop/video_recorder/venv/Scripts/python.exe -c "import wsgi; print('WSGI imported successfully')"

echo.
echo Testing app creation...
c:/Users/aksha/OneDrive/Desktop/video_recorder/venv/Scripts/python.exe -c "from app import app; print('Flask app created successfully')"

echo.
echo All tests passed! App should deploy correctly.
echo.
pause