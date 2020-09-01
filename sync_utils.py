import bpy


def pull_text(name: str):
    try:
        return bpy.data.texts[str(name)].as_string()
    except KeyError:
        return None


def update_text(name: str, content: str = None, path: str = None):
    try:
        if path:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
        return bpy.data.texts[str(name)].from_string(str(content))
    except KeyError:
        return False


def delete_text(name: str):
    try:
        return bpy.data.texts.remove(bpy.data.texts[str(name)])
    except KeyError:
        return False


def create_text(name: str):
    try:
        bpy.data.texts[str(name)]
        return False
    except KeyError:
        return bpy.data.texts.new(str(name))


def rename_text(old: str, new: str):
    try:
        bpy.data.texts[str(old)].name = str(new)
    except KeyError:
        return False
