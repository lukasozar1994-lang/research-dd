# Troubleshooting

## Diagnostics

Run the built-in doctor command:

```bash
research-driven-setup doctor
```

This checks environment prerequisites, MCP configuration, generated assets, and npm dependencies.

## Common Issues

### Command Not Found

If `research-driven-setup` is not recognized:

```bash
# Verify installation
pip show research-driven-setup

# If using uv
uv tool list | grep research-driven

# Reinstall
pip install -e .
```

### MCP Servers Not Starting

1. Ensure npm dependencies are installed: `npm install`
2. Check `.vscode/mcp.json` syntax
3. In VS Code: Command Palette → "MCP: List Servers" → Start individual servers
4. Check terminal output for error messages

### Context7 API Key

```bash
# Check if key is set
grep CONTEXT7_API_KEY .env

# Set the key
echo "CONTEXT7_API_KEY=your-key" >> .env

# Verify with doctor
research-driven-setup doctor
```

### GitHub MCP Authentication

GitHub MCP uses VS Code's OAuth flow:
1. Start the "github" server in MCP: List Servers
2. A browser window opens for authentication
3. Authorize the GitHub Copilot application
4. Return to VS Code — the server should be connected

### Workspace Conflicts

If the installer reports blocked or skipped files:

```bash
# Force overwrite all managed files
research-driven-setup install --force

# Preview update changes first
research-driven-setup update --dry-run
```

### npm Install Failures

```bash
# Clear cache and retry
rm -rf node_modules package-lock.json
npm install

# Check Node.js version
node --version  # Should be 18+
```

## Getting Help

1. Run `research-driven-setup doctor` to diagnose issues
2. Check `.research-driven/install-report.md` for install details
3. Check `.research-driven/doctor-report.md` for diagnostic details
