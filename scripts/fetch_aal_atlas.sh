#!/bin/bash
set -e

echo "--- Manual Setup for AAL Atlas ---"

# Directory to store the AAL atlas data
DEST_DIR="/home/vscode/nilearn_data/aal_3v2"
mkdir -p "$DEST_DIR"

# Download the AAL3v2 atlas file
FILE_PATH="$DEST_DIR/AAL3v2_for_SPM12.tar.gz"
echo "Downloading AAL3v2..."
curl -k https://www.gin.cnrs.fr/wp-content/uploads/AAL3v2_for_SPM12.tar.gz -o "$FILE_PATH"

# Verify the download
if [ -f "$FILE_PATH" ]; then
    echo "Download completed successfully."
else
    echo "Error: Download failed."
    exit 1
fi

# Extract the downloaded file
echo "Extracting files..."
tar -xzf "$FILE_PATH" -C "$DEST_DIR"

# Delete the tar.gz file after extraction
rm "$FILE_PATH"

echo "--- Setup Complete ---"