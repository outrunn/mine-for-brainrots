#!/bin/bash
# Detect when agents complete and notify for testing

cd ~/Dev/games/roblox/mine-for-brainrots

STATE_FILE=".github/.completion-state.json"

# Initialize state if needed
if [ ! -f "$STATE_FILE" ]; then
    echo '{"trackedAgents": {}, "completed": []}' > "$STATE_FILE"
fi

# Get current running agents
RUNNING_AGENTS=$(ps aux | grep "/Users/basilisk/.local/bin/claude" | grep -v grep | wc -l | tr -d ' ')

echo "=== Agent Completion Check ==="
echo "Time: $(date)"
echo "Running: $RUNNING_AGENTS agents"
echo ""

# Check each active issue
for ISSUE in 8 7 2; do
    BRANCH=""
    case $ISSUE in
        8) BRANCH="fix/brainrot-physics" ;;
        7) BRANCH="feature/teleport-buttons" ;;
        2) BRANCH="feature/shop-ui-rework" ;;
    esac
    
    # Check if branch exists and has recent commits
    if git show-ref --verify --quiet refs/heads/$BRANCH; then
        LAST_COMMIT=$(git log $BRANCH --oneline -1 2>/dev/null)
        COMMIT_TIME=$(git log $BRANCH --format=%ct -1 2>/dev/null)
        NOW=$(date +%s)
        AGE=$((NOW - COMMIT_TIME))
        
        # If commit is recent (< 2 min) and files modified recently, agent is working
        # If commit is older (> 2 min) and no recent file changes, agent likely finished
        RECENT_FILES=$(find . -type f -mmin -2 -not -path "./.git/*" 2>/dev/null | wc -l | tr -d ' ')
        
        if [ $AGE -lt 120 ] || [ $RECENT_FILES -gt 0 ]; then
            echo "⚙️  Issue #$ISSUE ($BRANCH): WORKING"
            echo "   Last commit: $LAST_COMMIT (${AGE}s ago)"
        else
            echo "✅ Issue #$ISSUE ($BRANCH): LIKELY COMPLETE"
            echo "   Last commit: $LAST_COMMIT (${AGE}s ago)"
            echo "   No file changes in 2 minutes"
            echo ""
            echo "   🎯 READY FOR TESTING!"
            echo ""
        fi
    else
        echo "⏳ Issue #$ISSUE ($BRANCH): Not started yet"
    fi
    echo ""
done

# Check if all agents finished
if [ $RUNNING_AGENTS -eq 0 ]; then
    echo "🎉 ALL AGENTS FINISHED!"
    echo ""
    echo "Branches ready for testing:"
    git branch | grep -E "(fix/|feature/)"
fi
