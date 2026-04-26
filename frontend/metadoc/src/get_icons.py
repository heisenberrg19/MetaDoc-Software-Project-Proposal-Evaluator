import os, re
src_dir = r'c:\Users\MarkChristian Garing\OneDrive\Desktop\MetaDoc-Software-Project-Proposal-Evaluator\frontend\metadoc\src'
icons = set()

for root, dirs, files in os.walk(src_dir):
    for f in files:
        if f.endswith('.jsx'):
            filepath = os.path.join(root, f)
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Find lucide-react imports
            match = re.search(r'import\s+\{([^}]+)\}\s+from\s+[\'\"\`]lucide-react[\'\"\`];?', content)
            if match:
                imports = match.group(1).replace('\n', ' ').split(',')
                for imp in imports:
                    name = imp.strip()
                    if name:
                        icons.add(name)

print(','.join(sorted(list(icons))))
