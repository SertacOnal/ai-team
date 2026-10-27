#!/bin/bash
# Chrome with remote debugging for OpenCode/Playwright integration
# Usage: source this or run directly

CHROME_DEBUG_PORT="${CHROME_DEBUG_PORT:-9222}"
CHROME_DEBUG_PROFILE="${CHROME_DEBUG_PROFILE:-$HOME/chrome-debug}"
CHROME_APP="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Check if Chrome is already running on debug port
if curl -s "http://127.0.0.1:$CHROME_DEBUG_PORT/json/version" >/dev/null 2>&1; then
    echo "Chrome already running on port $CHROME_DEBUG_PORT"
    exit 0
fi

# Check if Chrome app exists
if [[ ! -x "$CHROME_APP" ]]; then
    echo "Chrome not found at: $CHROME_APP"
    exit 1
fi

# Start Chrome with remote debugging
echo "Starting Chrome with remote debugging on port $CHROME_DEBUG_PORT..."
"$CHROME_APP" \
    --remote-debugging-port="$CHROME_DEBUG_PORT" \
    --user-data-dir="$CHROME_DEBUG_PROFILE" \
    "$@" &

# Wait for Chrome to be ready
for i in {1..30}; do
    if curl -s "http://127.0.0.1:$CHROME_DEBUG_PORT/json/version" >/dev/null 2>&1; then
        echo "Chrome ready on port $CHROME_DEBUG_PORT"
        exit 0
    fi
    sleep 0.5
done

echo "Chrome failed to start within 15 seconds"
exit 1
