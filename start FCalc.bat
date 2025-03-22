@echo off
set BAT_DIR=%~dp0
cd /d "%BAT_DIR%"
call "%BAT_DIR%figure_calc\Scripts\activate"
python "%BAT_DIR%FigureCalculator.py"
deactivate