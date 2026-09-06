@echo off
echo ========================================
echo RESTARTING BACKEND WITH CORS FIX
echo ========================================
echo.
echo The CORS configuration has been updated to fix the
echo "Access blocked by CORS policy" error.
echo.
echo This script will restart the backend server.
echo.
echo Press Ctrl+C to stop the backend when needed.
echo.
echo ========================================
echo Starting Backend Server...
echo ========================================
echo.

cd backend
python app.py

pause
