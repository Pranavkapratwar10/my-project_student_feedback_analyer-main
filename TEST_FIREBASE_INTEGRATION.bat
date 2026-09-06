@echo off
echo ========================================
echo   Firebase Integration Test
echo ========================================
echo.
echo This script will test the Firebase integration
echo.
echo ========================================
echo.

echo Step 1: Testing Firebase Connection...
echo.
cd backend
python firebase_config.py
echo.

echo ========================================
echo.
echo Step 2: Checking if backend dependencies are installed...
echo.
pip show requests >nul 2>&1
if errorlevel 1 (
    echo ❌ requests library not found
    echo Installing requests...
    pip install requests
) else (
    echo ✓ requests library is installed
)
echo.

echo ========================================
echo.
echo Step 3: Checking frontend dependencies...
echo.
cd ..\frontend
if exist node_modules\firebase (
    echo ✓ Firebase SDK is installed
) else (
    echo ❌ Firebase SDK not found
    echo Installing Firebase...
    call npm install firebase
)
echo.

echo ========================================
echo.
echo NEXT STEPS:
echo.
echo 1. Go to Firebase Console: https://console.firebase.google.com/
echo 2. Select project: predictive-maintenance-8c9b1
echo 3. Create Realtime Database (Build → Realtime Database)
echo 4. Set database rules to test mode
echo 5. Run this script again to verify connection
echo.
echo 6. Start backend: python backend/app.py
echo 7. Start frontend: cd frontend ^&^& npm start
echo 8. Upload feedback with keywords: harassment, unsafe, abuse
echo 9. Check Alerts page for real-time updates
echo.
echo ========================================
pause
