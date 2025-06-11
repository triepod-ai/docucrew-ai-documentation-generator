"""
GitHub Repository Analyzer
"""
from github import Github
from typing import Dict, Any, List, Optional
import base64
from urllib.parse import urlparse


class GitHubAnalyzer:
    """Analyzes GitHub repositories for documentation generation"""
    
    def __init__(self, token: Optional[str] = None):
        self.github = Github(token) if token else Github()
    
    def parse_repo_url(self, url: str) -> tuple[str, str]:
        """Extract owner and repo name from GitHub URL"""
        # Handle various GitHub URL formats
        parsed = urlparse(url)
        path_parts = parsed.path.strip('/').split('/')
        
        if len(path_parts) >= 2:
            return path_parts[0], path_parts[1]
        
        # Handle owner/repo format
        if '/' in url and not url.startswith('http'):
            parts = url.split('/')
            return parts[0], parts[1]
        
        raise ValueError(f"Invalid GitHub repository URL: {url}")
    
    def get_repository_structure(self, owner: str, repo_name: str) -> Dict[str, Any]:
        """Get repository structure and metadata"""
        try:
            repo = self.github.get_repo(f"{owner}/{repo_name}")
            
            # Get repository metadata
            metadata = {
                'name': repo.name,
                'description': repo.description,
                'main_language': repo.language,
                'languages': repo.get_languages(),
                'topics': repo.get_topics(),
                'stars': repo.stargazers_count,
                'forks': repo.forks_count,
                'created_at': repo.created_at.isoformat(),
                'updated_at': repo.updated_at.isoformat()
            }
            
            # Get file structure
            structure = self._get_file_tree(repo)
            
            # Get key files content
            key_files = self._get_key_files(repo)
            
            return {
                'metadata': metadata,
                'structure': structure,
                'key_files': key_files,
                'file_count': self._count_files(structure)
            }
            
        except Exception as e:
            raise Exception(f"Failed to analyze repository: {str(e)}")
    
    def _get_file_tree(self, repo, path: str = "", max_depth: int = 3) -> Dict[str, Any]:
        """Recursively get file tree structure"""
        tree = {}
        
        try:
            contents = repo.get_contents(path)
            
            for content in contents:
                if content.type == "dir" and max_depth > 0:
                    tree[content.name] = self._get_file_tree(
                        repo, content.path, max_depth - 1
                    )
                else:
                    tree[content.name] = {
                        'type': content.type,
                        'size': content.size,
                        'path': content.path
                    }
                    
        except Exception:
            pass
            
        return tree
    
    def _get_key_files(self, repo) -> Dict[str, str]:
        """Get content of key files for analysis"""
        key_files = {}
        important_files = [
            'README.md', 'readme.md', 'README.rst',
            'package.json', 'requirements.txt', 'setup.py',
            'Cargo.toml', 'go.mod', 'pom.xml'
        ]
        
        for filename in important_files:
            try:
                content = repo.get_contents(filename)
                if content.type == "file":
                    # Decode base64 content
                    decoded = base64.b64decode(content.content).decode('utf-8')
                    key_files[filename] = decoded[:1000]  # First 1000 chars
            except:
                continue
                
        return key_files
    
    def _count_files(self, tree: Dict[str, Any], count: int = 0) -> int:
        """Count total files in tree structure"""
        for item in tree.values():
            if isinstance(item, dict):
                if item.get('type') == 'file':
                    count += 1
                else:
                    count = self._count_files(item, count)
        return count
    
    def get_api_files(self, repo) -> List[Dict[str, str]]:
        """Find and return API-related files"""
        api_patterns = [
            'api', 'routes', 'endpoints', 'controllers',
            'handlers', 'views', 'resolvers'
        ]
        
        api_files = []
        
        def search_tree(tree: Dict[str, Any], current_path: str = ""):
            for name, item in tree.items():
                if isinstance(item, dict):
                    if item.get('type') == 'file':
                        # Check if file might contain API definitions
                        if any(pattern in name.lower() or pattern in current_path.lower() 
                               for pattern in api_patterns):
                            api_files.append({
                                'name': name,
                                'path': item.get('path', '')
                            })
                    else:
                        search_tree(item, f"{current_path}/{name}")
        
        structure = self._get_file_tree(repo)
        search_tree(structure)
        
        return api_files[:10]  # Limit to 10 most relevant files