echo "Removing old files..."
ampy --port COM3 rmdir src
echo "Moving src files to board..."
ampy --port COM3 put src
echo "Moving main.py file..."
ampy --port COM3 put main.py