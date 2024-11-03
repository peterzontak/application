import os

dir_path = 'poznamky'
current_script_directory = os.path.dirname(os.path.abspath(__file__))
notes_root = os.path.join(current_script_directory, '../../config',dir_path)


def split_content(f):
    content = f.read()
    normalized_content = content.replace('\r\n', '\n').replace('\r', '\n')
    pieces = normalized_content.split('\n\n')
    trimmed_pieces = [piece.strip() for piece in pieces if piece.strip()]
    
    return trimmed_pieces


def read_folder(folder: str):
    root = os.path.join(notes_root, folder)
    result = {'files': {}, 'dirs': {}}
    for d in os.listdir(root):
        _path = os.path.join(folder, d)
        if os.path.isdir(_path):
            result['dirs'][d] = {}
            for _file in os.listdir(_path):
                _file_path = os.path.join(_path, _file)
                if os.path.isfile(_file_path):
                    with open(_file_path, 'r', encoding='utf-8') as f:
                        name, ext = os.path.splitext(_file)                        
                        result['dirs'][d][name] = {
                            'ext': ext,
                            'content': split_content(f)
                        }
        elif os.path.isfile(_path):
            with open(_path, 'r', encoding='utf-8') as f:
                name, ext = os.path.splitext(d)
                result['files'][name] = {
                    'ext': ext,
                    'content': split_content(f)
                }
    return result
            

def get_notes_categories():
    # print(notes_root)
    notes = [d for d in os.listdir(notes_root) if os.path.isdir(os.path.join(notes_root, d))]
    return notes

def get_note(note: str):
    root = os.path.join(notes_root, note)
    # headings = [d for d in os.listdir(root) if os.path.isdir(os.path.join(root, d))]
    # notes = [d for d in os.listdir(root) if os.path.isfile(os.path.join(root, d))]
    
     
    
    # print(read_folder(root))
    # print(headings)
    # print(notes)
    return read_folder(root)
