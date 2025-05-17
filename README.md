
🖼️ Grayscale Image Converter

A simple Python project using OpenCV that reads a color image, converts it to grayscale, saves the result, and displays both images.

🔥 Features

1. Reads and processes images using OpenCV  
2. Converts color images to grayscale  
3. Saves the converted grayscale image  
4. Displays both original and grayscale images  
5. Automatically closes image windows after a short delay  

🚀 Technologies Used

1. Python – General-purpose programming  
2. OpenCV – Image processing and computer vision  

⚙️ Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/grayscale-image-converter.git
   cd grayscale-image-converter
   ```

2. Install required packages:
   ```bash
   pip install opencv-python
   ```

3. Place your input image in the project directory and name it flower.png.

4. Run the script:
   ```bash
   python app.py
   ```

🛠️ How It Works

- The script loads an image named flower.png.  
- It converts the image to grayscale using cv2.cvtColor().  
- The grayscale image is saved as grey.png.  
- Both the original and grayscale images are displayed in separate windows.  
- After 5 seconds, the windows close automatically.  

📂 Project Structure
```bash
📁 grayscale-image-converter  
├── app.py         # Main Python script  
├── flower.png     # Input image (user-provided)  
├── grey.png       # Output grayscale image (auto-generated)  
└── README.md      # Project documentation
```
