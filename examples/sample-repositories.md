# Sample Repositories for Testing

## Recommended Test Cases

### Simple Projects
- **requests** - `https://github.com/kennethreitz/requests`
  - Well-documented Python HTTP library
  - Clear API structure
  - Good for testing basic documentation generation

### Medium Complexity
- **Flask** - `https://github.com/pallets/flask`
  - Python web framework
  - Multiple modules and components
  - API endpoints and documentation examples

- **FastAPI** - `https://github.com/tiangolo/fastapi`
  - Modern Python web framework
  - Extensive API documentation
  - Good for testing API documentation features

### Complex Projects
- **Django** - `https://github.com/django/django`
  - Large, mature Python framework
  - Complex architecture
  - Stress test for agent coordination

### JavaScript/Node.js
- **Express** - `https://github.com/expressjs/express`
  - Node.js web framework
  - Different language patterns
  - API server documentation

### React/Frontend
- **React** - `https://github.com/facebook/react`
  - Complex frontend library
  - Component-based architecture
  - Documentation examples and patterns

## Testing Strategy

1. **Start Simple**: Begin with well-documented projects like `requests`
2. **Increase Complexity**: Move to frameworks like Flask or FastAPI
3. **Test Edge Cases**: Try repositories with unusual structures
4. **Language Variety**: Test different programming languages
5. **Private Repos**: Test with GitHub token for private repositories

## Expected Outputs

Each test should generate:
- Clear README with installation instructions
- API documentation (if applicable)
- Usage examples
- Project structure overview
- Contributing guidelines

## Common Issues to Watch For

- Rate limiting with large repositories
- Timeout issues with complex analysis
- Quality of generated examples
- Accuracy of API documentation
- Proper formatting and structure