#!/bin/bash

# Update the apk package index
echo "Updating package index..."
sudo apk update

# List of packages to install
PACKAGES=(
    python3-tkinter
    py3-virtualenv
    sdl2-dev
    sdl2_image-dev
    sdl2_mixer-dev
    sdl2_ttf-dev
    mesa
    mesa-dri-gallium
    mesa-gl
    mesa-egl
    libx11
    libxext
    cmake
    portmidi-dev
    github-cli
)

echo "Installing packages..."
sudo apk add --no-cache "${PACKAGES[@]}"

echo "Setting up python"
virtualenv .venv
source ".venv/bin/activate"
pip install -r requirements.txt

echo "Postcreate complete!"
