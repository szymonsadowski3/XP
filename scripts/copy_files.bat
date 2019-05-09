echo "Removing old files..."
ampy --port COM4 rmdir src
echo "Moving src files to board..."
ampy --port COM4 put src
echo "Moving main.py file..."
ampy --port COM4 put main.py

