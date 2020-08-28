import bpy


def pull_text(name: str):
    try:
        return bpy.data.texts[str(name)].as_string()
    except KeyError:
        return False


def update_text(name: str, content: str):
    try:
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
