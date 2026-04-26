import os, re
src_dir = r'c:\Users\MarkChristian Garing\OneDrive\Desktop\MetaDoc-Software-Project-Proposal-Evaluator\frontend\metadoc\src'

for root, dirs, files in os.walk(src_dir):
    for f in files:
        if f.endswith('.jsx'):
            filepath = os.path.join(root, f)
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # calculate relative path from the current file's directory to the Icons component
            rel_path = os.path.relpath(os.path.join(src_dir, 'components', 'common', 'Icons'), root).replace(os.sep, '/')
            if not rel_path.startswith('.'):
                rel_path = './' + rel_path
                
            new_content = re.sub(r'import\s+\{([^}]+)\}\s+from\s+[\'\"\`]lucide-react[\'\"\`];?', 
                   lambda m: 'import {' + m.group(1) + '} from \'' + rel_path + '\';', 
                   content)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(new_content)
