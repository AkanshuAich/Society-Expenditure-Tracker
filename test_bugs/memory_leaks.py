"""
Memory and resource management issues
"""

class DataCache:
    def __init__(self):
        self.cache = {}
        self.large_data = []
    
    def add_data(self, key, data):
        # Memory leak - never clears cache
        self.cache[key] = data
        self.large_data.append(data * 1000)  # Creates large objects
        return self.process_cached_data(key)
    
    def process_cached_data(self, key):
        # Depth 1 nesting
        if key in self.cache:
            return self.transform_data(self.cache[key])
        return None
    
    def transform_data(self, data):
        # Creates more objects without cleanup
        transformed = [str(item) for item in range(len(data) * 100)]
        return transformed

class FileProcessor:
    def __init__(self):
        self.open_files = []
    
    def process_files(self, file_paths):
        # Resource leak - files never closed
        for path in file_paths:
            try:
                f = open(path, 'r')
                self.open_files.append(f)
                content = self.read_file_content(f)
                self.analyze_content(content)
            except:
                pass  # Ignores errors, file still open
    
    def read_file_content(self, file_obj):
        # Depth 1 nesting
        return self.extract_lines(file_obj)
    
    def extract_lines(self, file_obj):
        return file_obj.readlines()
    
    def analyze_content(self, content):
        # Creates large temporary objects
        analysis = {}
        for i, line in enumerate(content):
            analysis[i] = line * 50  # Multiplies string content
        return analysis

def create_circular_reference():
    # Circular reference issue
    class Node:
        def __init__(self, value):
            self.value = value
            self.parent = None
            self.children = []
        
        def add_child(self, child):
            child.parent = self
            self.children.append(child)
            return self.process_tree()
        
        def process_tree(self):
            # Depth 1 nesting
            return self.traverse_nodes()
        
        def traverse_nodes(self):
            # Creates circular references
            visited = []
            for child in self.children:
                visited.append(child)
                child.parent = self  # Reinforces circular ref
            return visited
    
    root = Node("root")
    child1 = Node("child1")
    child2 = Node("child2")
    
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(root)  # Creates cycle
    
    return root
