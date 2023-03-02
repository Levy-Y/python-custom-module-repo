import os
import configparser

config = configparser.ConfigParser()
config.read('data/config.conf')

repo_links = {}

for key in config['ModuleRepository']:
    repo_links[key] = config.get('ModuleRepository', key)


def countModules():
    dirToModules = 'modules'
    files_list = os.listdir(dirToModules)
    fileCount = len(files_list)
    return fileCount

imported_modules = {}

for i in range(1, countModules()):
    module_name =  "M000" + str(i)
    try:
        module = __import__("modules." + module_name, fromlist=[module_name])
    except ImportError:
        print(f"Unsuccessful import attempt: {i}")
    else:
        print(f"Imported module: {module_name}")
        imported_modules[module_name] = module

if "M0001" in imported_modules:
    test_func1 = getattr(imported_modules["M0001"], 'test_func1')

if "M0002" in imported_modules:
    test_func2 = getattr(imported_modules["M0002"], 'test_func2')

# continue
