#!/bin/sh -l

echo "Uploading file to Google Drive..."
python /app/src/main.py
# Write outputs to the $GITHUB_OUTPUT file
# echo "uploaded_item_id=$UPLOADED_ITEM_ID" >> "$GITHUB_OUTPUT"

exit 0
