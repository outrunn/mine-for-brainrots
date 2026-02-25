# Claude Code Allowlist Configuration

## Location
`~/.claude/settings.local.json`

## Current Allowlist

### Safe Bash Commands
- `Bash(find:*)` - File searching
- `Bash(cd:*)` - Directory navigation
- `Bash(head:*)`, `Bash(cat:*)`, `Bash(grep:*)` - File reading
- `Bash(ls:*)`, `Bash(pwd:*)` - Directory listing
- `Bash(echo:*)` - Output

### Git & GitHub
- `Bash(git:*)` - All git commands
- `Bash(gh auth:*)` - GitHub authentication
- `Bash(gh label:*)` - Label management
- `Bash(gh issue:*)` - Issue management
- `Bash(gh api:*)` - GitHub API calls

### Roblox Studio MCP (ALL TOOLS)
- `mcp__robloxstudio-1__*` - Port 58741 (all tools)
- `mcp__robloxstudio-2__*` - Port 58742 (all tools)
- `mcp__robloxstudio-3__*` - Port 58743 (all tools)
- `mcp__robloxstudio__*` - Legacy pattern (all tools)

**Includes:**
- `get_instance_properties`
- `create_object`
- `execute_luau`
- `get_script_source`
- `edit_script_lines`
- `set_script_source`
- `delete_script_lines`
- `insert_script_lines`
- `start_playtest`
- `get_playtest_output`
- `stop_playtest`
- `get_project_structure`
- `get_instance_children`
- `get_place_info`
- `get_services`
- `search_objects`
- `search_files`
- `create_object_with_properties`
- `mass_create_objects`
- `mass_get_property`
- `set_property`
- And ANY future MCP commands

### File Operations
- `Edit` - Edit files
- `Read` - Read files
- `Write` - Write files

## Effect

**Agents will NO LONGER need approval for:**
- Reading/writing Roblox Studio scripts via MCP
- Running playtests
- Creating/modifying game objects
- Git operations (commit, branch, push)
- GitHub operations (issues, labels)
- Safe file operations
- Common bash commands

**Agents WILL STILL need approval for:**
- Destructive operations (rm, delete)
- Network operations (curl, wget)
- System changes
- Unknown/new commands not in allowlist

## Last Updated
2026-02-24 19:37 EST
