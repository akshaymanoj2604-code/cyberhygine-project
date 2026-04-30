from setuptools import setup

setup(
    name="video-recorder",
    version="1.0.0",
    description="A Flask-based video recording system",
    author="Video Recorder App",
    packages=[],
    include_package_data=True,
    install_requires=[
        "Flask==3.1.0",
        "Flask-SQLAlchemy==3.1.1",
        "Flask-CORS==6.0.2",
        "Werkzeug==3.1.3",
    ],
)