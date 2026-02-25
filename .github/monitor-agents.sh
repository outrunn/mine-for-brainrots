#!/bin/bash
# Monitor agent progress

cd ~/Dev/games/roblox/mine-for-brainrots

echo "=== Agent Monitoring ==="
echo "Time: $(date)"
echo ""

echo "Git Branches:"
git branch | grep -E "(fix/brainrot|feature/mining)"
echo ""

echo "Recent Git Activity:"
git log --oneline -5 --all
echo ""

echo "Modified Files (last 5 min):"
find . -type f -mmin -5 -not -path "./.git/*" | head -10
echo ""

echo "Claude Processes:"
ps aux | grep claude | grep -v grep | grep -v monitor
