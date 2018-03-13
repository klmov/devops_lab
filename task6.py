import json
import pip
import site
import sys
import yaml



def getData():
    result = {}  # Output dict
    # Version
    result["Version"] = sys.version[:5]
    # Virtualenv info
    result["Virtualenv"] = sys.prefix
    # Executable location
    result["ExecutableLocation"] = sys.executable
    # Pip location
    result["pipLocation"] = pip.__path__[0]
    # Pip packages
    result["pip"] = ([i.key + "=" + i.version
                      for i in pip.get_installed_distributions()])
    # PYTRHONPATH
    result["PYTHONPATH"] = sys.path[2]
    # Site-Packages
    result["Site-PackagesLocation"] = site.getsitepackages()[0]
    return result


def jsonOut(data):
    with open('pyinfo.json', 'w') as json_file:
        json.dump(data,
                  json_file,
                  sort_keys=False,
                  indent=5,
                  ensure_ascii=False)


def yamlOut(data):
    with open('pyinfo.yaml', 'w') as yaml_file:
        yaml.dump(data,
                  yaml_file,
                  default_flow_style=False)

if __name__ == '__main__':
    print("Python Info")
    data = getData()
    print(json.dumps(data,
                    sort_keys=False,
                    indent=5,
                    ensure_ascii=False))

    jsonOut(data)
    yamlOut(data)
