import os
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from ttkbootstrap import Style, ttk
from ttkbootstrap.constants import *

from PIL import Image
from moviepy.editor import VideoFileClip
from pydub import AudioSegment

class ConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Universal File Converter")
        self.root.geometry("900x800")
        self.root.resizable(False, False)

        # Initialize ttkbootstrap style
        self.style = Style(theme='cyborg')  # Options: 'darkly', 'superhero', 'cyborg', etc.

        # Create Notebook for tabs
        self.notebook = ttk.Notebook(self.root, bootstyle=PRIMARY)
        self.notebook.pack(pady=10, padx=10, expand=True, fill='both')

        # Initialize Tabs
        self.init_image_tab()
        self.init_video_tab()
        self.init_audio_tab()

    def init_image_tab(self):
        # Image Conversion Tab
        self.image_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.image_tab, text='Images')

        # Frame for Input Selection
        self.img_input_frame = ttk.Frame(self.image_tab)
        self.img_input_frame.pack(pady=20, padx=20, fill='x')

        self.img_input_label = ttk.Label(self.img_input_frame, text="Select Image(s):", font=("Helvetica", 12))
        self.img_input_label.pack(side='left', padx=(0,10))

        self.img_input_entry = ttk.Entry(self.img_input_frame, font=("Helvetica", 12), width=50)
        self.img_input_entry.pack(side='left', fill='x', expand=True)

        self.img_browse_input_btn = ttk.Button(self.img_input_frame, text="Browse", command=self.browse_image_input, bootstyle=PRIMARY)
        self.img_browse_input_btn.pack(side='left', padx=(10,0))

        # Frame for Output Format Selection
        self.img_output_frame = ttk.Frame(self.image_tab)
        self.img_output_frame.pack(pady=10, padx=20, fill='x')

        self.img_output_label = ttk.Label(self.img_output_frame, text="Select Output Format:", font=("Helvetica", 12))
        self.img_output_label.pack(side='left', padx=(0,10))

        self.img_format_var = tk.StringVar()
        self.img_format_combobox = ttk.Combobox(
            self.img_output_frame,
            textvariable=self.img_format_var,
            state='readonly',
            font=("Helvetica", 12)
        )
        # Comprehensive list of formats supported by Pillow
        self.img_format_combobox['values'] = (
            'JPEG', 'JPG', 'PNG', 'BMP', 'GIF', 'TIFF', 'ICO', 'WEBP', 'PPM', 'PBM', 'PGM',
            'TGA', 'DDS', 'ICNS', 'IM', 'PCX', 'SGI', 'SPI', 'XBM', 'XPM', 'XV Thumbnails'
        )
        self.img_format_combobox.current(0)
        self.img_format_combobox.pack(side='left', fill='x', expand=True)

        # Convert Button
        self.img_convert_btn = ttk.Button(self.image_tab, text="Convert Images", command=self.start_image_conversion, bootstyle=SUCCESS)
        self.img_convert_btn.pack(pady=20)

        # Progress Bar
        self.img_progress = ttk.Progressbar(self.image_tab, mode='indeterminate')
        self.img_progress.pack(pady=(0,10), padx=20, fill='x')

        # Conversion Log
        self.img_log_label = ttk.Label(self.image_tab, text="Conversion Log:", font=("Helvetica", 12))
        self.img_log_label.pack(pady=(10,0))

        self.img_log_text = scrolledtext.ScrolledText(
            self.image_tab,
            wrap=tk.WORD,
            width=90,
            height=15,
            font=("Helvetica", 10),
            state='disabled',
            bg="#2e2e2e",       # Dark background
            fg="white",         # White text
            insertbackground="white"  # Cursor color
        )
        self.img_log_text.pack(padx=20, pady=(0,20))

    def init_video_tab(self):
        # Video Conversion Tab
        self.video_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.video_tab, text='Videos')

        # Frame for Input Selection
        self.vid_input_frame = ttk.Frame(self.video_tab)
        self.vid_input_frame.pack(pady=20, padx=20, fill='x')

        self.vid_input_label = ttk.Label(self.vid_input_frame, text="Select Video(s):", font=("Helvetica", 12))
        self.vid_input_label.pack(side='left', padx=(0,10))

        self.vid_input_entry = ttk.Entry(self.vid_input_frame, font=("Helvetica", 12), width=50)
        self.vid_input_entry.pack(side='left', fill='x', expand=True)

        self.vid_browse_input_btn = ttk.Button(self.vid_input_frame, text="Browse", command=self.browse_video_input, bootstyle=PRIMARY)
        self.vid_browse_input_btn.pack(side='left', padx=(10,0))

        # Frame for Output Format Selection
        self.vid_output_frame = ttk.Frame(self.video_tab)
        self.vid_output_frame.pack(pady=10, padx=20, fill='x')

        self.vid_output_label = ttk.Label(self.vid_output_frame, text="Select Output Format:", font=("Helvetica", 12))
        self.vid_output_label.pack(side='left', padx=(0,10))

        self.vid_format_var = tk.StringVar()
        self.vid_format_combobox = ttk.Combobox(
            self.vid_output_frame,
            textvariable=self.vid_format_var,
            state='readonly',
            font=("Helvetica", 12)
        )
        # Comprehensive list of common video formats
        self.vid_format_combobox['values'] = (
            'MP4', 'AVI', 'MOV', 'MKV', 'WMV', 'FLV', 'WEBM', 'MPEG', 'MPG', '3GP'
        )
        self.vid_format_combobox.current(0)
        self.vid_format_combobox.pack(side='left', fill='x', expand=True)

        # Convert Button
        self.vid_convert_btn = ttk.Button(self.video_tab, text="Convert Videos", command=self.start_video_conversion, bootstyle=SUCCESS)
        self.vid_convert_btn.pack(pady=20)

        # Progress Bar
        self.vid_progress = ttk.Progressbar(self.video_tab, mode='indeterminate')
        self.vid_progress.pack(pady=(0,10), padx=20, fill='x')

        # Conversion Log
        self.vid_log_label = ttk.Label(self.video_tab, text="Conversion Log:", font=("Helvetica", 12))
        self.vid_log_label.pack(pady=(10,0))

        self.vid_log_text = scrolledtext.ScrolledText(
            self.video_tab,
            wrap=tk.WORD,
            width=90,
            height=15,
            font=("Helvetica", 10),
            state='disabled',
            bg="#2e2e2e",       # Dark background
            fg="white",         # White text
            insertbackground="white"  # Cursor color
        )
        self.vid_log_text.pack(padx=20, pady=(0,20))

    def init_audio_tab(self):
        # Audio Conversion Tab
        self.audio_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.audio_tab, text='Audio')

        # Frame for Input Selection
        self.aud_input_frame = ttk.Frame(self.audio_tab)
        self.aud_input_frame.pack(pady=20, padx=20, fill='x')

        self.aud_input_label = ttk.Label(self.aud_input_frame, text="Select Audio(s):", font=("Helvetica", 12))
        self.aud_input_label.pack(side='left', padx=(0,10))

        self.aud_input_entry = ttk.Entry(self.aud_input_frame, font=("Helvetica", 12), width=50)
        self.aud_input_entry.pack(side='left', fill='x', expand=True)

        self.aud_browse_input_btn = ttk.Button(self.aud_input_frame, text="Browse", command=self.browse_audio_input, bootstyle=PRIMARY)
        self.aud_browse_input_btn.pack(side='left', padx=(10,0))

        # Frame for Output Format Selection
        self.aud_output_frame = ttk.Frame(self.audio_tab)
        self.aud_output_frame.pack(pady=10, padx=20, fill='x')

        self.aud_output_label = ttk.Label(self.aud_output_frame, text="Select Output Format:", font=("Helvetica", 12))
        self.aud_output_label.pack(side='left', padx=(0,10))

        self.aud_format_var = tk.StringVar()
        self.aud_format_combobox = ttk.Combobox(
            self.aud_output_frame,
            textvariable=self.aud_format_var,
            state='readonly',
            font=("Helvetica", 12)
        )
        # Comprehensive list of common audio formats
        self.aud_format_combobox['values'] = (
            'MP3', 'WAV', 'OGG', 'FLAC', 'AAC', 'M4A', 'WMA', 'ALAC', 'AIFF', 'APE'
        )
        self.aud_format_combobox.current(0)
        self.aud_format_combobox.pack(side='left', fill='x', expand=True)

        # Convert Button
        self.aud_convert_btn = ttk.Button(self.audio_tab, text="Convert Audio", command=self.start_audio_conversion, bootstyle=SUCCESS)
        self.aud_convert_btn.pack(pady=20)

        # Progress Bar
        self.aud_progress = ttk.Progressbar(self.audio_tab, mode='indeterminate')
        self.aud_progress.pack(pady=(0,10), padx=20, fill='x')

        # Conversion Log
        self.aud_log_label = ttk.Label(self.audio_tab, text="Conversion Log:", font=("Helvetica", 12))
        self.aud_log_label.pack(pady=(10,0))

        self.aud_log_text = scrolledtext.ScrolledText(
            self.audio_tab,
            wrap=tk.WORD,
            width=90,
            height=15,
            font=("Helvetica", 10),
            state='disabled',
            bg="#2e2e2e",       # Dark background
            fg="white",         # White text
            insertbackground="white"  # Cursor color
        )
        self.aud_log_text.pack(padx=20, pady=(0,20))

    def browse_image_input(self):
        files = filedialog.askopenfilenames(
            title="Select Image File(s)",
            filetypes=[
                ("Image Files", "*.jpg *.jpeg *.png *.bmp *.gif *.tiff *.ico *.webp *.ppm *.pbm *.pgm *.tga *.dds *.icns *.im *.pcx *.sgi *.spi *.xbm *.xpm *.xv"),
                ("All Files", "*.*")
            ]
        )
        if files:
            self.img_input_entry.delete(0, tk.END)
            self.img_input_entry.insert(0, '; '.join(files))

    def browse_video_input(self):
        files = filedialog.askopenfilenames(
            title="Select Video File(s)",
            filetypes=[
                ("Video Files", "*.mp4 *.avi *.mov *.mkv *.wmv *.flv *.webm *.mpeg *.mpg *.3gp"),
                ("All Files", "*.*")
            ]
        )
        if files:
            self.vid_input_entry.delete(0, tk.END)
            self.vid_input_entry.insert(0, '; '.join(files))

    def browse_audio_input(self):
        files = filedialog.askopenfilenames(
            title="Select Audio File(s)",
            filetypes=[
                ("Audio Files", "*.mp3 *.wav *.ogg *.flac *.aac *.m4a *.wma *.alac *.aiff *.ape"),
                ("All Files", "*.*")
            ]
        )
        if files:
            self.aud_input_entry.delete(0, tk.END)
            self.aud_input_entry.insert(0, '; '.join(files))

    def log_callback_image(self, message):
        self.img_log_text.config(state='normal')
        self.img_log_text.insert(tk.END, message + '\n')
        self.img_log_text.config(state='disabled')
        self.img_log_text.see(tk.END)

    def log_callback_video(self, message):
        self.vid_log_text.config(state='normal')
        self.vid_log_text.insert(tk.END, message + '\n')
        self.vid_log_text.config(state='disabled')
        self.vid_log_text.see(tk.END)

    def log_callback_audio(self, message):
        self.aud_log_text.config(state='normal')
        self.aud_log_text.insert(tk.END, message + '\n')
        self.aud_log_text.config(state='disabled')
        self.aud_log_text.see(tk.END)

    def start_image_conversion(self):
        input_files = self.img_input_entry.get().split('; ')
        output_format = self.img_format_var.get().lower()

        if not input_files or input_files == ['']:
            messagebox.showerror("Error", "Please select at least one input image.")
            self.log_callback_image("❌ No input image selected.")
            return

        if not output_format:
            messagebox.showerror("Error", "Please select an output format.")
            self.log_callback_image("❌ No output format selected.")
            return

        # Start the progress bar
        self.img_progress.start(10)
        self.log_callback_image(f"🔄 Starting image conversion to {output_format.upper()} format...")

        # Run conversion in a separate thread to keep GUI responsive
        thread = threading.Thread(target=self.convert_images, args=(input_files, output_format))
        thread.start()

    def convert_images(self, input_files, output_format):
        for input_file in input_files:
            try:
                img = Image.open(input_file)
                base, ext = os.path.splitext(input_file)
                # Handle special cases for certain formats
                if output_format in ['jpeg', 'jpg'] and img.mode in ('RGBA', 'P'):
                    img = img.convert("RGB")  # JPEG doesn't support transparency
                elif output_format == 'gif' and img.mode not in ('RGB', 'P'):
                    img = img.convert("P", palette=Image.ADAPTIVE)

                output_file = f"{base}.{output_format}"
                img.save(output_file, output_format.upper())
                self.log_callback_image(f"✅ Converted: {os.path.basename(input_file)} → {os.path.basename(output_file)}")
            except Exception as e:
                self.log_callback_image(f"❌ Failed to convert {os.path.basename(input_file)}: {e}")

        # Stop the progress bar
        self.img_progress.stop()
        self.log_callback_image("🔄 All image conversions completed.")

    def start_video_conversion(self):
        input_files = self.vid_input_entry.get().split('; ')
        output_format = self.vid_format_var.get().lower()

        if not input_files or input_files == ['']:
            messagebox.showerror("Error", "Please select at least one input video.")
            self.log_callback_video("❌ No input video selected.")
            return

        if not output_format:
            messagebox.showerror("Error", "Please select an output format.")
            self.log_callback_video("❌ No output format selected.")
            return

        # Start the progress bar
        self.vid_progress.start(10)
        self.log_callback_video(f"🔄 Starting video conversion to {output_format.upper()} format...")

        # Run conversion in a separate thread to keep GUI responsive
        thread = threading.Thread(target=self.convert_videos, args=(input_files, output_format))
        thread.start()

    def convert_videos(self, input_files, output_format):
        for input_file in input_files:
            try:
                clip = VideoFileClip(input_file)
                base, ext = os.path.splitext(input_file)
                output_file = f"{base}.{output_format}"

                # Define codec based on output format
                codec_map = {
                    'mp4': 'libx264',
                    'avi': 'mpeg4',
                    'mov': 'libx264',
                    'mkv': 'libx264',
                    'wmv': 'wmv2',
                    'flv': 'flv',
                    'webm': 'libvpx',
                    'mpeg': 'mpeg4',
                    'mpg': 'mpeg4',
                    '3gp': 'libx264'
                }

                codec = codec_map.get(output_format, 'libx264')  # Default codec

                # Write the video file
                clip.write_videofile(
                    output_file,
                    codec=codec,
                    audio_codec='aac',
                    logger=None  # Suppress moviepy's own logging
                )
                self.log_callback_video(f"✅ Converted: {os.path.basename(input_file)} → {os.path.basename(output_file)}")
            except Exception as e:
                self.log_callback_video(f"❌ Failed to convert {os.path.basename(input_file)}: {e}")

        # Stop the progress bar
        self.vid_progress.stop()
        self.log_callback_video("🔄 All video conversions completed.")

    def start_audio_conversion(self):
        input_files = self.aud_input_entry.get().split('; ')
        output_format = self.aud_format_var.get().lower()

        if not input_files or input_files == ['']:
            messagebox.showerror("Error", "Please select at least one input audio file.")
            self.log_callback_audio("❌ No input audio file selected.")
            return

        if not output_format:
            messagebox.showerror("Error", "Please select an output format.")
            self.log_callback_audio("❌ No output format selected.")
            return

        # Start the progress bar
        self.aud_progress.start(10)
        self.log_callback_audio(f"🔄 Starting audio conversion to {output_format.upper()} format...")

        # Run conversion in a separate thread to keep GUI responsive
        thread = threading.Thread(target=self.convert_audios, args=(input_files, output_format))
        thread.start()

    def convert_audios(self, input_files, output_format):
        for input_file in input_files:
            try:
                audio = AudioSegment.from_file(input_file)
                base, ext = os.path.splitext(input_file)
                output_file = f"{base}.{output_format}"

                # Export audio in the desired format
                audio.export(output_file, format=output_format)
                self.log_callback_audio(f"✅ Converted: {os.path.basename(input_file)} → {os.path.basename(output_file)}")
            except Exception as e:
                self.log_callback_audio(f"❌ Failed to convert {os.path.basename(input_file)}: {e}")

        # Stop the progress bar
        self.aud_progress.stop()
        self.log_callback_audio("🔄 All audio conversions completed.")

def main():
    root = tk.Tk()
    app = ConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
