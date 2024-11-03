import os
from django.shortcuts import render, HttpResponse

from notes.controller.poznamky import get_notes_categories

# def build_notes_dict(base_path):
#     # notes = {}
#     notes = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]

#     # Walk through the directory structure
#     print('---------------------------------------------------')
#     for root, dirs, files in os.walk(base_path):
#         # Get the current folder name
#         folder_name = os.path.basename(root)
#         # If we are at a subdirectory level (not at the base path)
#         if root != base_path:
#             # Split the path to get parent folder
#             parent_folder = os.path.basename(os.path.dirname(root))
#             # print(parent_folder)
#             print(folder_name)
#             print(root)
#             print(dirs)
#             print(files)
#             print('---------------------------------------------------')


#             if folder_name not in notes:
#                 notes[folder_name] = files

#             # if os.isdir(root):
#             #     print('ok')

#             # if folder_name not in notes[root]:
                
#             #     notes[parent_folder][folder_name] = []

#             # # Extend the list with files found in this directory
#             # notes[parent_folder][folder_name].extend(files)
#         # else:
#         #     # For top-level folders, just add their files directly
#         #     notes[folder_name] = files

#     return notes


# def build_notes_dict(base_path):
#     notes = {}

#     # Walk through the directory structure
#     for root, dirs, files in os.walk(base_path):
#         # Get the current folder name
#         folder_name = os.path.basename(root)

#         # If we are at a subdirectory level (not at the base path)
#         if root != base_path:
#             # Split the path to get parent folder
#             parent_folder = os.path.basename(os.path.dirname(root))

#             # If parent folder is not already in notes, add it
#             if parent_folder not in notes:
#                 notes[parent_folder] = []

#             # Check if folder_name is already in notes[parent_folder]
#             existing_folders = [item if isinstance(item, str) else list(item.keys())[0] for item in notes[parent_folder]]

#             if folder_name not in existing_folders:
#                 notes[parent_folder].append({folder_name: files})
#             else:
#                 # If the folder already exists, extend its file list
#                 for item in notes[parent_folder]:
#                     if isinstance(item, dict) and folder_name in item:
#                         item[folder_name].extend(files)
#                         break
#         else:
#             # For top-level folders, just add their files directly
#             notes[folder_name] = files

#     return notes


# def build_notes_dict(base_path):
#     notes = {}

#     # Walk through the directory structure
#     for root, dirs, files in os.walk(base_path):
#         # Get the relative path from the base path
#         relative_path = os.path.relpath(root, base_path)
#         path_parts = relative_path.split(os.sep)

#         # Initialize current level of notes
#         current_level = notes

#         # Build the folder structure based on parts
#         for part in path_parts:
#             if part not in current_level:
#                 current_level[part] = {'files': [], 'subfolders': {}}
#             current_level = current_level[part]['subfolders']

#         # Add files to the current folder
#         current_level['files'].extend(files)

#     # Clean up the structure to match desired output format
#     def format_notes_structure(notes):
#         formatted = {}
#         for folder_name, content in notes.items():
#             formatted[folder_name] = []
#             # Add files directly
#             if content['files']:
#                 formatted[folder_name].extend(content['files'])
#             # Add subfolders as objects
#             for subfolder_name, subfolder_content in content['subfolders'].items():
#                 formatted[folder_name].append({
#                     'name': subfolder_name,
#                     'files': subfolder_content['files'],
#                 })
#         return formatted

#     return format_notes_structure(notes)



def home(request):
    # dir_path = './poznamky'
    notes = get_notes_categories()
    return render(request, 'home.html', {'notes': notes})







    # notes = ['a','b','c']
    # notes = [d for d in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, d))]
    # notes = build_notes_dict(os.listdir(dir_path))


# {
#     'poznamky': [{
#         'Docker': [
#             'docker.md',
#             'wsl.md'
#         ]}, {
#         'GULP': [
#             'gulp.md',
#             'gulpfile.js'
#         ]}, {
#         'Linux': [
#             'commands.md',
#             'cron.md'
#         ]}, {
#         'Python': [
#             'pip.md',
#             'venv.md'
#         ]}, {
#         'SQL': [
#             'aggregate.sql',
#             'alter.sql',
#             'create.sql',
#             'delete.sql',
#             'distinct.sql',
#             'group_by.sql',
#             'insert.sql',
#             'join.sql',
#             'ordering_limiting.sql',
#             'regular_Expressions.md',
#             'select.sql',
#             'update.sql',
#             'view.sql',
#             'vseobecne.sql'
#         ]}],
#         'Python': [{'Django': ['deploy.md', 'migrations.md', 'new-project.md', 'postgre.md']}], 'SQL': [{'MySQL': ['functions.sql']}, {'PostgreSQL': ['functions.sql', 'PostreSQL.sql']}]}
