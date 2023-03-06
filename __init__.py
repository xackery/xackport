import bpy
from bpy.props import StringProperty, EnumProperty, PointerProperty
from bpy.types import Operator, Panel, PropertyGroup, Scene
from bpy.utils import register_class, unregister_class

bl_info = {
    "name": "Xackport",
    "author": "xackery",
    "version" : (1, 0),
    "blender" : (3, 4, 0),
    "location" : "View3D > Xackport",
    "category" : "Export Settings",
    "description" : "Easily export all the settings needed to make glb",
}

# adding a panel
class Xackport_PT_panel(Panel):
    bl_idname = 'Xackport_PT_panel'
    bl_label = 'Export'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Xackport'
 
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text='Special export to *.glb')
        layout.separator()
        col = layout.column()
        col.prop(context.scene.placeholder, "export_path", text="Path")

           

        layout.operator('xackport.op', text='Export').action = 'Xackport'

class XackportProperties(PropertyGroup):
    export_path:  StringProperty(
        name="Path",
        default="out.glb",
        description="Path to save file to",
    )

class Xackport_OT_op(Operator):
    bl_idname = 'xackport.op'
    bl_label = 'Export'
    bl_description = 'Xackport'
    bl_options = {'REGISTER', 'UNDO'}
 
    action: EnumProperty(
        items=[
            ('Xackport', 'Export', 'xackport'),
        ]
    )
 
    def execute(self, context):
        if self.action == 'Xackport':
            self.export(context=context)
        return {'FINISHED'}

    @staticmethod
    def export(context):
        bpy.ops.export_scene.gltf(filepath=bpy.path.abspath(context.scene.placeholder.export_path), check_existing=False, export_format='GLB', use_selection=False)        

def register():
    bpy.utils.register_class(Xackport_PT_panel)
    bpy.utils.register_class(XackportProperties)
    bpy.utils.register_class(Xackport_OT_op)
    
    Scene.placeholder = PointerProperty(type=XackportProperties)
 
def unregister():
    bpy.utils.unregister_class(Xackport_OT_op)
    bpy.utils.unregister_class(XackportProperties)
    bpy.utils.unregister_class(Xackport_PT_panel)
    
    del Scene.placeholder
 
 
if __name__ == '__main__':
    register()