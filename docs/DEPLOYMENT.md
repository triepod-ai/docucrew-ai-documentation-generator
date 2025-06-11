# Deployment Guide

## Production Deployment

### Environment Setup

**Required Environment Variables:**
```bash
OPENAI_API_KEY=your_production_api_key
GITHUB_TOKEN=your_github_token  # Optional
FRONTEND_URL=https://your-frontend-domain.com
API_HOST=0.0.0.0
API_PORT=8000
```

### Backend Deployment

**Option 1: Railway/Render**
```bash
# Install dependencies
pip install -r requirements.txt

# Start application
python main.py
```

**Option 2: Docker**
```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY backend/ .
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["python", "main.py"]
```

### Frontend Deployment

**Vercel (Recommended):**
```bash
npm run build
# Deploy to Vercel via Git integration
```

**Manual Build:**
```bash
cd frontend
npm install
npm run build
npm start
```

### CORS Configuration

Update FastAPI CORS settings for production:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-frontend-domain.com"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)
```

## Security Considerations

1. **API Keys**: Never commit API keys to version control
2. **CORS**: Restrict to specific domains in production
3. **Rate Limiting**: Implement rate limiting for API endpoints
4. **Input Validation**: Validate repository URLs and inputs
5. **Error Handling**: Don't expose internal errors to users

## Monitoring

### Health Checks
- Backend: `GET /health`
- Frontend: Monitor build and runtime errors

### Logging
- Configure structured logging for agent activities
- Monitor API response times and error rates
- Track WebSocket connection stability

## Scaling Considerations

1. **Agent Concurrency**: Limit concurrent documentation generations
2. **Memory Usage**: Monitor memory usage during large repository analysis
3. **API Quotas**: Monitor OpenAI API usage and quotas
4. **WebSocket Connections**: Handle connection limits appropriately