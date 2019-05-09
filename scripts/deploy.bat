for %%b in ("%~dp0\run_tests.bat" "%~dp0\copy_files.bat") do call %%b|| exit /b 1
