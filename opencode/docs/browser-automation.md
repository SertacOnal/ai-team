# Browser Automation with OpenCode

OpenCode can control browsers via Playwright MCP, using your existing Chrome
sessions and logins (Google SSO, Jenkins, etc.).

## Setup

### 1. Start Chrome with Remote Debugging

```bash
# One-time or on demand:
~/Repos/ai-team/opencode/scripts/chrome-debug.sh

# Or add to ~/.zshrc:
alias chrome-debug='~/Repos/ai-team/opencode/scripts/chrome-debug.sh'
```

Chrome starts with:
- Remote debugging on port 9222
- Persistent profile at `~/chrome-debug`
- All your login sessions preserved

### 2. Configure OpenCode

Add to your project's `opencode.json`:

```jsonc
{
  "mcp": {
    "servers": {
      "playwright": {
        "type": "local",
        "command": ["npx", "-y", "@playwright/mcp", "--cdp-endpoint", "http://127.0.0.1:9222"]
      }
    }
  }
}
```

Or copy `../ai-team/opencode/config/playwright.jsonc`.

### 3. Verify Connection

```bash
opencode mcp list
# Should show: ✓ playwright  connected
```

## Usage

Once connected, agents can:

- Navigate to URLs
- Click elements
- Fill forms
- Take screenshots
- Read page content

### Example Commands

```
# Navigate
await tools.playwright.browser_navigate({ url: "https://example.com" })

# Get page snapshot
await tools.playwright.browser_snapshot()

# Click element
await tools.playwright.browser_click({ element: "Submit button", target: "ref123" })

# Fill input
await tools.playwright.browser_type({ target: "ref456", text: "hello" })
```

## Session Persistence

The `~/chrome-debug` profile stores:
- Cookies and sessions
- Saved passwords (via macOS Keychain)
- Browser history
- Extensions

Login once manually, and OpenCode/Playwright will use those sessions.

## Troubleshooting

### "Browser is already in use"
Close regular Chrome or use the debug profile exclusively.

### "Connection refused"
Chrome isn't running with remote debugging. Run:
```bash
~/Repos/ai-team/opencode/scripts/chrome-debug.sh
```

### "Port 9222 not responding"
```bash
# Check if Chrome is listening
curl http://127.0.0.1:9222/json/version

# Kill stuck Chrome processes
pkill -9 -i chrome
rm -f ~/chrome-debug/SingletonLock
```

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `CHROME_DEBUG_PORT` | 9222 | Remote debugging port |
| `CHROME_DEBUG_PROFILE` | ~/chrome-debug | Profile directory |
