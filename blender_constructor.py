import bpy
import re

def snap_selected_to_cursor():
    for i in range(3):
        bpy.context.object.location[i] = bpy.data.screens['Default'].scene.cursor_location[i] 

def construct(matrix_plant, lines, columns):
    block = ''
    
    for i in range(lines):
        for j in range(columns):
            if (not matrix_plant.get((i, j),0)):
                if (block):
                    bpy.ops.object.duplicate_move(TRANSFORM_OT_translate={"value":((j - x) * block.dimensions[0], (y - i) * block.dimensions[1], 0)})
                else:
                    bpy.ops.mesh.primitive_plane_add()
                    block = bpy.context.object
                    block.name = 'BlOcK'
                    bpy.ops.transform.translate(value=(j * block.dimensions[0], i * block.dimensions[1], 0))
            
                x = j
                y = i

    regex = re.compile('^BlOcK(.[0-9]+)?')
    for obj in bpy.data.objects:
        if (regex.findall(obj.name) and not obj.select):
            obj.select = True

    bpy.ops.object.join()
    obj = bpy.context.object
    obj.name = 'Maze'
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.remove_doubles()
    bpy.ops.object.editmode_toggle()
    snap_selected_to_cursor()
    
                
              
            


