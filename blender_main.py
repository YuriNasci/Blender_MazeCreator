import bpy
from blender_constructor import construct
from Maze import Maze

bl_info = \
        {
            "name" : "Maze Maker",
            "author" : "Yuri Alves Nascimento <yurinascimento@outlook.com>",
            "version" : (1, 0, 0),
            "blender" : (2, 7, 3),
            "location" : "View 3D > Object Mode > Tool Shelf",
            "description" :
            "Generate a maze mesh",
            #"warning" : "",
            #"wiki_url" : "",
            #"tracker_url" : "https://github.com/YuriNasci",
            "category" : "Add Mesh",
        }

class MazeMakerPanel(bpy.types.Panel) :
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_context = "objectmode"
    bl_label = "Add Maze"
    
    def draw(self, context) :
        TheCol = self.layout.column(align = True)
        TheCol.label(text = 'Size:')
        TheCol.prop(context.scene, "rows")
        TheCol.prop(context.scene, "columns")
        
        TheCol = self.layout.column(align = True)
        TheCol.operator("mesh.make_maze", text = "Add Maze")
    #end draw
#end TetrahedronMakerPanel

class MakeMaze(bpy.types.Operator) :
    bl_idname = "mesh.make_maze"
    bl_label = "Add Maze"
    bl_options = {"UNDO"}
    
    def invoke(self, context, event) :
        # contruir o labirinto
        obj = Maze(context.scene.rows, context.scene.columns)
        construct(obj.maze, obj.lin, obj.col)
        if (obj.lin < obj.col):
            for i in range(3):
                bpy.context.object.scale[i] = 1 / obj.lin
        else:
            for i in range(3):
                bpy.context.object.scale[i] = 1 / obj.col
        
        return {"FINISHED"}
    #end invoke

def register() :
    bpy.utils.register_class(MakeMaze)
    bpy.utils.register_class(MazeMakerPanel)
    bpy.types.Scene.rows = bpy.props.IntProperty \
    (
    name = "Rows",
    min = 3,
    default = 15
    )
    bpy.types.Scene.columns = bpy.props.IntProperty \
    (
    name = "Columns",
    min = 3,
    default = 15
    )
#end register

def unregister() :
    bpy.utils.unregister_class(MakeMaze)
    bpy.utils.unregister_class(MazeMakerPanel)
    del bpy.types.Scene.rows
    del bpy.types.Scene.columns
#end unregister

if __name__ == "__main__" :
    register()

