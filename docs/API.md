# API Reference

## Base URL
```
http://localhost:8000
```

## Endpoints

### Documentation Generation

#### `POST /api/analyze`
Analyzes a GitHub repository and generates documentation using the multi-agent system.

**Request Body:**
```json
{
  "repo_url": "https://github.com/username/repository"
}
```

**Response:**
```json
{
  "status": "success",
  "session_id": "uuid-string",
  "message": "Analysis started"
}
```

### Real-time Updates

#### WebSocket `/ws/{session_id}`
Provides real-time updates from the agent system during documentation generation.

**Connection:**
```javascript
const ws = new WebSocket(`ws://localhost:8000/ws/${sessionId}`);
```

**Message Format:**
```json
{
  "type": "agent_update",
  "agent": "code_analyzer",
  "status": "working",
  "message": "Analyzing repository structure...",
  "progress": 25
}
```

**Message Types:**
- `agent_update` - Agent status and progress
- `task_complete` - Agent task completion
- `error` - Error messages
- `final_result` - Complete documentation output

### Health Check

#### `GET /health`
Returns API health status.

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2024-01-01T00:00:00Z"
}
```

## Error Handling

All endpoints return standardized error responses:

```json
{
  "status": "error",
  "message": "Error description",
  "code": "ERROR_CODE"
}
```

**Common Error Codes:**
- `INVALID_REPO_URL` - Invalid GitHub repository URL
- `REPO_NOT_FOUND` - Repository not accessible
- `API_KEY_MISSING` - OpenAI API key not configured
- `RATE_LIMIT_EXCEEDED` - API rate limits exceeded