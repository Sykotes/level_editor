#!/bin/bash

# Update the apk package index
echo "Updating package index..."
sudo apk update

# List of packages you want to install
PACKAGES=(
    python3-tkinter
    sdl2-dev
    mesa
    mesa-dri-gallium
    mesa-gl
    mesa-egl
    libx11
    libxext
)

# Install all the packages
echo "Installing packages..."
sudo apk add --no-cache "${PACKAGES[@]}"

echo "Postcreate complete!"
