
import os
import shutil

project_path = 'structure2/my_project'
project_templates_path = os.path.join(project_path, 'templates')
try:
    os.mkdir(project_templates_path)
except:
    pass

for dirname in os.listdir(project_path):
    app_template_dir = os.path.join(project_path, dirname, 'templates', dirname)
    if os.path.isdir(app_template_dir):
        shutil.copytree(app_template_dir, os.path.join(project_templates_path, dirname))
