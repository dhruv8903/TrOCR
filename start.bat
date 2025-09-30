@echo off
echo Starting Mossip Decode OCR Application...
echo.

echo Starting Backend Service (TrOCR)...
start "TrOCR Backend" cmd /k "cd backend && python app.py"

echo Waiting for backend to start...
timeout /t 5 /nobreak > nul

echo Starting Frontend Service...
start "Mossip Frontend" cmd /k "npm run dev"

echo.
echo Services are starting...
echo Backend: http://localhost:5000
echo Frontend: http://localhost:3000
echo.
echo Press any key to close this window...
pause > nul
