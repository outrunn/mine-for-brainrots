#!/bin/bash
# MCP Connection Pre-Flight Check

cd ~/Dev/games/roblox/mine-for-brainrots

echo "=== MCP Connection Test ==="
echo "Time: $(date)"
echo ""

# Check if .mcp.json exists
if [ ! -f .mcp.json ]; then
    echo "❌ .mcp.json not found"
    exit 1
fi

echo "✅ .mcp.json found"
echo ""

# Check configured MCP servers
echo "Configured MCP Servers:"
grep -A 3 "robloxstudio-" .mcp.json | grep ROBLOX_STUDIO_PORT
echo ""

# Test each port
echo "Testing MCP Ports..."
for port in 58741 58742 58743; do
    if curl -s -o /dev/null -w "%{http_code}" http://localhost:$port > /dev/null 2>&1; then
        echo "✅ Port $port: Responding"
    else
        echo "❌ Port $port: Not responding"
    fi
done
echo ""

# Check for running Claude processes
echo "Active Claude Agents:"
ps aux | grep claude | grep -v grep | grep -v test-mcp | wc -l | xargs echo "Count:"
echo ""

# Quick MCP tool test
echo "Testing MCP with quick command..."
echo 'List available MCP tools' | /Users/basilisk/.local/bin/claude --non-interactive 2>&1 | grep -i "roblox\|mcp\|tool" | head -5
echo ""

echo "=== Test Complete ==="
