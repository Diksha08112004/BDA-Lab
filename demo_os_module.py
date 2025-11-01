""
OS Module Demo
Showcasing working directory and file listing functionality
"""

import os
from datetime import datetime

def get_file_info(path):
    """Get file information in a readable format"""
    stats = os.stat(path)
    size_kb = stats.st_size / 1024  # Convert to KB
    mod_time = datetime.fromtimestamp(stats.st_mtime)
    return {
        'name': os.path.basename(path),
        'size_kb': f"{size_kb:.2f} KB",
        'modified': mod_time.strftime('%Y-%m-%d %H:%M'),
        'is_dir': os.path.isdir(path),
        'is_file': os.path.isfile(path)
    }

def list_directory(path='.'):
    """List directory contents with details"""
    print(f"\nContents of: {os.path.abspath(path)}\n")
    print(f"{'Name':<30} {'Type':<8} {'Size':<12} {'Modified'}")
    print("-" * 65)
    
    # List all entries in the directory
    for entry in os.scandir(path):
        try:
            info = get_file_info(entry.path)
            entry_type = 'DIR' if info['is_dir'] else 'FILE'
            print(f"{info['name']:<30} {entry_type:<8} {info['size_kb']:<12} {info['modified']}")
        except (PermissionError, FileNotFoundError) as e:
            print(f"Error accessing {entry.path}: {e}")

def main():
    print("=== OS Module Demo ===\n")
    
    # 1. Get current working directory
    cwd = os.getcwd()
    print(f"1. Current Working Directory: {cwd}")
    
    # 2. List contents of current directory
    print("\n2. Listing current directory:")
    list_directory()
    
    # 3. Navigate to parent directory
    parent_dir = os.path.dirname(cwd)
    print(f"\n3. Parent directory contents:")
    list_directory(parent_dir)
    
    # 4. Create a test directory and file
    test_dir = os.path.join(cwd, 'test_dir')
    if not os.path.exists(test_dir):
        os.mkdir(test_dir)
        test_file = os.path.join(test_dir, 'test.txt')
        with open(test_file, 'w') as f:
            f.write("This is a test file.")
        
        print(f"\n4. Created test directory and file:")
        list_directory(test_dir)
    
    # 5. Environment variables
    print("\n5. Some Environment Variables:")
    print(f"   USERNAME: {os.getenv('USERNAME', 'Not available')}")
    print(f"   COMPUTERNAME: {os.getenv('COMPUTERNAME', 'Not available')}")
    print(f"   PYTHONPATH: {os.getenv('PYTHONPATH', 'Not set')}")

if __name__ == "__main__":
    main()
