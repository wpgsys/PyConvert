# PyConvert - Universal File Converter (No More Annoying Websites) 🖥️✨

![Universal File Converter](https://img.shields.io/github/license/yourusername/universal-file-converter)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![Dependencies](https://img.shields.io/badge/dependencies-Pillow%2C%20ttkbootstrap%2C%20moviepy%2C%20pydub-green.svg)

**Universal File Converter** is a versatile and user-friendly desktop application built with Python's Tkinter library and enhanced with `ttkbootstrap` for a modern dark-themed interface. This tool allows users to convert images, videos, and audio files between various formats seamlessly. Whether you're a content creator, developer, or casual user, this converter simplifies the process of file format transformation with its intuitive GUI and robust functionality. This tool will save me countless time while working with web devekopmenet. Not neeeding a website makes thing a-okay,

---

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Setup Instructions](#setup-instructions)
3. [Usage](#usage)
    - [Images Conversion](#images-conversion)
    - [Videos Conversion](#videos-conversion)
    - [Audio Conversion](#audio-conversion)
4. [Dependencies](#dependencies)
5. [Contributing](#contributing)
6. [License](#license)
7. [Acknowledgements](#acknowledgements)

---

## Features

- **Tabbed Interface:**
  - **Images Tab:** Convert images between formats like JPEG, PNG, BMP, GIF, TIFF, ICO, WebP, and more.
  - **Videos Tab:** Convert videos between formats such as MP4, AVI, MOV, MKV, WMV, FLV, WEBM, MPEG, MPG, 3GP.
  - **Audio Tab:** Convert audio files between formats including MP3, WAV, OGG, FLAC, AAC, M4A, WMA, ALAC, AIFF, APE.
  
- **Modern Dark Theme:** Utilizes `ttkbootstrap` for a sleek and visually appealing dark interface.

- **Multiple File Selection:** Convert multiple images, videos, or audio files simultaneously.

- **Format Selection:** Choose from a wide range of output formats based on the selected category.

- **Progress Indicator:** Visual feedback during the conversion process with indeterminate progress bars.

- **Conversion Log:** Real-time logging of conversion statuses and errors within the application.

- **Batch Processing:** Efficiently handle multiple conversions simultaneously without freezing the GUI.

---

## Installation

### Prerequisites

Before installing **Universal File Converter**, ensure that your system meets the following requirements:

- **Operating System:** Windows, macOS, or Linux.
- **Python:** Version 3.8 or higher.
- **FFmpeg:** Required for video and audio conversions.

### Setup Instructions

Follow the steps below to set up and run the **Universal File Converter** on your system.

#### 1. Clone the Repository

```bash
git clone https://github.com/wpgsys/PyConverter.git
cd universal-file-converter
```

#### 2. Set Up a Virtual Environment (Optional but Recommended)

Using a virtual environment ensures that your project dependencies are isolated from other Python projects.

```bash
# Create a virtual environment named 'venv'
python3 -m venv venv

# Activate the virtual environment
# On macOS and Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

#### 3. Upgrade `pip`

Ensure that you have the latest version of `pip` to avoid any installation issues.

```bash
pip install --upgrade pip
```

#### 4. Install Required Libraries

Create a `requirements.txt` file with the following content:

```plaintext
Pillow==10.0.0
ttkbootstrap==1.10.1
moviepy==1.0.3
pydub==0.25.1
```

Install the dependencies using `pip`:

```bash
pip install -r requirements.txt
```

#### 5. Install FFmpeg

Both **MoviePy** and **pydub** rely on **FFmpeg** for processing videos and audio files. You need to install FFmpeg on your system and ensure it's added to your system's PATH.

##### For macOS:

Using [Homebrew](https://brew.sh/):

```bash
brew install ffmpeg
```

##### For Windows:

1. **Download FFmpeg:**
   - Visit the [FFmpeg Download Page](https://ffmpeg.org/download.html).
   - Download the latest static build for Windows.

2. **Extract FFmpeg:**
   - Extract the downloaded ZIP file to a directory, e.g., `C:\ffmpeg`.

3. **Add FFmpeg to PATH:**
   - Open **System Properties** > **Advanced** > **Environment Variables**.
   - Under **System Variables**, find and select the **Path** variable, then click **Edit**.
   - Click **New** and add the path to FFmpeg's `bin` folder, e.g., `C:\ffmpeg\bin`.
   - Click **OK** to save changes.

4. **Verify Installation:**
   - Open **Command Prompt** and run:
     ```bash
     ffmpeg -version
     ```
   - You should see FFmpeg version information if installed correctly.

##### For Linux:

```bash
sudo apt-get update
sudo apt-get install ffmpeg
```

---

## Usage

Once the installation is complete, you can run the **Universal File Converter** using the following command:

```bash
python3 converter_app.py
```

### Images Conversion

1. **Select Image(s):**
   - Navigate to the **Images** tab.
   - Click the **Browse** button.
   - In the file dialog, select one or multiple image files (e.g., JPEG, PNG, BMP).

2. **Select Output Format:**
   - Choose the desired output format from the dropdown menu (e.g., PNG, JPEG).

3. **Start Conversion:**
   - Click the **Convert Images** button.
   - The progress bar will activate, and conversion logs will appear in the log area.
   - Upon completion, you'll see a confirmation in the log.

4. **Check Converted Images:**
   - The converted images will be saved in the same directory as the original images, with the new file extension.

### Videos Conversion

1. **Select Video(s):**
   - Navigate to the **Videos** tab.
   - Click the **Browse** button.
   - In the file dialog, select one or multiple video files (e.g., MP4, AVI, MOV).

2. **Select Output Format:**
   - Choose the desired output format from the dropdown menu (e.g., MKV, WMV).

3. **Start Conversion:**
   - Click the **Convert Videos** button.
   - The progress bar will activate, and conversion logs will appear in the log area.
   - Upon completion, you'll see a confirmation in the log.

4. **Check Converted Videos:**
   - The converted videos will be saved in the same directory as the original videos, with the new file extension.

### Audio Conversion

1. **Select Audio(s):**
   - Navigate to the **Audio** tab.
   - Click the **Browse** button.
   - In the file dialog, select one or multiple audio files (e.g., MP3, WAV, OGG).

2. **Select Output Format:**
   - Choose the desired output format from the dropdown menu (e.g., FLAC, AAC).

3. **Start Conversion:**
   - Click the **Convert Audio** button.
   - The progress bar will activate, and conversion logs will appear in the log area.
   - Upon completion, you'll see a confirmation in the log.

4. **Check Converted Audio Files:**
   - The converted audio files will be saved in the same directory as the original audio files, with the new file extension.

---

## Dependencies

The **Universal File Converter** relies on the following Python libraries:

- **[Pillow](https://python-pillow.org/):** Python Imaging Library for image processing.
- **[ttkbootstrap](https://github.com/israel-dryer/ttkbootstrap):** Enhances Tkinter with modern themes and styled widgets.
- **[MoviePy](https://zulko.github.io/moviepy/):** Library for video editing and conversion.
- **[pydub](https://github.com/jiaaro/pydub):** Simplifies audio processing and conversion.

Ensure that all dependencies are installed as per the [Installation Instructions](#installation).

---

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. **Fork the Project**
2. **Create your Feature Branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your Changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the Branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

---

## License

Distributed under the MIT License. See `LICENSE` for more information.

---

## Acknowledgements

- [Tkinter](https://docs.python.org/3/library/tkinter.html) - Python's standard GUI package.
- [ttkbootstrap](https://github.com/israel-dryer/ttkbootstrap) - Modern themes for Tkinter.
- [Pillow](https://python-pillow.org/) - Python Imaging Library.
- [MoviePy](https://zulko.github.io/moviepy/) - Video editing with Python.
- [pydub](https://github.com/jiaaro/pydub) - Manipulate audio with a simple and easy high-level interface.
- [FFmpeg](https://ffmpeg.org/) - Complete, cross-platform solution to record, convert and stream audio and video.

---

## Screenshots

*Add screenshots of your application here to give users a visual overview.*

![Image Conversion](screenshots/image_conversion.png)
*Image Conversion Interface*

![Video Conversion](screenshots/video_conversion.png)
*Video Conversion Interface*

![Audio Conversion](screenshots/audio_conversion.png)
*Audio Conversion Interface*

*Ensure to create a `screenshots` directory and add relevant images.*

---

## Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter) - youremail@example.com

Project Link: [https://github.com/yourusername/universal-file-converter](https://github.com/yourusername/universal-file-converter)

---

**Happy Coding! 🖥️✨**

---

**Note:** Replace placeholders like `yourusername`, `youremail@example.com`, and screenshot paths with your actual GitHub username, contact information, and image paths. Additionally, ensure that FFmpeg is correctly installed and accessible in your system's PATH for video and audio conversions to work seamlessly.
