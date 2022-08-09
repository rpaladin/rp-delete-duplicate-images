bl_info = {
    "name": "Delete Duplicate Images",
    "description": "Deletes duplicate image data-blocks from the blend file, immediately.",
    "author": "RPaladin",
    "version": (8, 9, 2022),
    "blender": (2, 80, 0),
    "location": "F3 > delete_duplicate_images",
    "warning": "",
    "doc_url": "",
    "tracker_url": "",
    "support": "COMMUNITY",
    "category": "3D Viewport",
}

import bpy

class DeleteDuplicateImages(bpy.types.Operator):
    bl_idname = "wm.delete_duplicate_images"
    bl_label = "Deletes Duplicate Images"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        for i in bpy.data.images:
            if i.name[-3:].isdigit():
                bpy.data.images.remove(i)
        print("Successfully deleted any duplicate images.")
        return {"FINISHED"}
    
def register():
    bpy.utils.register_class(DeleteDuplicateImages)

def unregister():
    bpy.utils.unregister_class(DeleteDuplicateImages)

if __name__ == "__main__":
    register()