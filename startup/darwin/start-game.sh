#!/bin/sh
cd ../..

export DYLD_LIBRARY_PATH=`pwd`/Libraries.bundle
export DYLD_FRAMEWORK_PATH="Frameworks"

# Get the user input:
read -p "Username: " ttaUsername
read -p "Gameserver (DEFAULT:  25.86.16.20): " TTA_GAMESERVER
TTA_GAMESERVER=${TTA_GAMESERVER:-"25.86.16.20"}

# Export the environment variables:
export ttaUsername=$ttaUsername
export ttaPassword="password"
export TTA_PLAYCOOKIE=$ttaUsername
export TTA_GAMESERVER=$TTA_GAMESERVER

echo "==============================="
echo "Starting Toontown Project Altis..."
echo "Username: $ttaUsername"
echo "Gameserver: $TTA_GAMESERVER"
echo "==============================="

ppython -m toontown.toonbase.ClientStart