from setuptools import setup, find_packages

setup(
    name="easy-youtube-downloader",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "yt-dlp>=2023.12.30",
    ],
    entry_points={
        'console_scripts': [
            'youtube-dl=youtube_downloader.main:main',
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple YouTube video and audio downloader",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/youtube-downloader",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
