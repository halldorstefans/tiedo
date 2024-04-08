#!/bin/bash

# Define paths
DATABASE_FILE="telematics.db"
BACKUP_DIR="/path/to/backup/directory"

# Create backup directory if not exists
mkdir -p "$BACKUP_DIR"

# Backup file with timestamp
BACKUP_FILE="$BACKUP_DIR/gps_data_backup_$(date +"%Y-%m-%d").db"

# Copy database file to backup location
cp "$DATABASE_FILE" "$BACKUP_FILE"

echo "SQLite database backed up to: $BACKUP_FILE"
