"""
AI Interior Design Configurator - SAFE VERSION
Wersja bezpieczna - zmienia tylko kolory, NIE pozycje obiektów
"""

import bpy
import json
from bpy.types import Panel, Operator
from bpy.props import EnumProperty

# ============================================================
# ŚCIEŻKA DO PLIKU JSON
# ============================================================

DESIGNS_JSON_PATH = r"C:\Users\timur\OneDrive\Рабочий стол\ai\designs.json"


# ============================================================
# FUNKCJE POMOCNICZE
# ============================================================

def load_designs():
    """Wczytuje presety designów z pliku JSON"""
    try:
        with open(DESIGNS_JSON_PATH, 'r', encoding='utf-8') as f:
            designs = json.load(f)
        print(f"✅ Wczytano {len(designs)} presetów designu")
        return designs
    except FileNotFoundError:
        print(f"❌ Nie znaleziono pliku: {DESIGNS_JSON_PATH}")
        return None
    except Exception as e:
        print(f"❌ Błąd wczytywania: {e}")
        return None


def set_material_color(obj_name, color):
    """Ustawia kolor materiału obiektu"""
    obj = bpy.data.objects.get(obj_name)
    
    if not obj:
        print(f"⚠️ Obiekt '{obj_name}' nie istnieje")
        return False
    
    # Jeśli obiekt nie ma danych (np. Empty), pomiń
    if not hasattr(obj, 'data') or not hasattr(obj.data, 'materials'):
        print(f"⚠️ Obiekt '{obj_name}' nie ma materiałów")
        return False
    
    if not obj.data.materials:
        mat = bpy.data.materials.new(name=f"{obj_name}_Material")
        mat.use_nodes = True
        obj.data.materials.append(mat)
    
    mat = obj.data.materials[0]
    
    if mat.use_nodes:
        principled = mat.node_tree.nodes.get('Principled BSDF')
        if principled:
            principled.inputs['Base Color'].default_value = color
            print(f"✅ Zmieniono kolor: {obj_name}")
            return True
    
    return False


def toggle_light(enabled):
    """Włącza/wyłącza światło"""
    lamp = bpy.data.objects.get("Lamp")
    
    if not lamp or lamp.type != 'LIGHT':
        return False
    
    if enabled:
        lamp.data.energy = 1000
        lamp.hide_viewport = False
        lamp.hide_render = False
    else:
        lamp.data.energy = 0
        lamp.hide_viewport = True
        lamp.hide_render = True
    
    return True


def set_light_properties(energy, color):
    """Ustawia właściwości światła"""
    lamp = bpy.data.objects.get("Lamp")
    
    if not lamp or lamp.type != 'LIGHT':
        return False
    
    lamp.data.energy = energy
    lamp.data.color = color[:3]
    return True


# ============================================================
# OPERATORY
# ============================================================

class AIDESIGN_OT_ApplyStyle(Operator):
    """Zastosuj wybrany styl AI (tylko kolory)"""
    bl_idname = "aidesign.apply_style"
    bl_label = "Zastosuj Styl"
    bl_options = {'REGISTER', 'UNDO'}
    
    style: EnumProperty(
        name="Styl",
        items=[
            ('minimalist', 'Minimalist', ''),
            ('cozy', 'Cozy', ''),
            ('futuristic', 'Futuristic', ''),
            ('industrial', 'Industrial', ''),
            ('scandinavian', 'Scandinavian', ''),
        ]
    )
    
    def execute(self, context):
        designs = load_designs()
        
        if not designs or self.style not in designs:
            self.report({'ERROR'}, "Nie można wczytać stylu")
            return {'CANCELLED'}
        
        design = designs[self.style]
        print(f"\n🎨 Aplikowanie stylu: {design['name']}")
        
        # TYLKO KOLORY - NIE ZMIENIAMY POZYCJI!
        set_material_color("Walls", design.get("wall_color", [0.8, 0.8, 0.8, 1.0]))
        set_material_color("Sofa", design.get("sofa_color", [0.5, 0.5, 0.5, 1.0]))
        set_material_color("Carpet", design.get("carpet_color", [0.8, 0.5, 0.3, 1.0]))
        set_material_color("Zaslona1", design.get("zaslona_color", [0.9, 0.9, 0.9, 1.0]))
        set_material_color("Zaslona2", design.get("zaslona_color", [0.9, 0.9, 0.9, 1.0]))
        set_material_color("FloorPlates", design.get("floorplates_color", [0.9, 0.9, 0.9, 1.0]))
        set_material_color("FloorUnder", design.get("floorunder_color", [0.85, 0.85, 0.85, 1.0]))
        
        # Aplikuj oświetlenie
        if design.get("lamp_enabled", True):
            set_light_properties(
                design.get("light_energy", 800),
                design.get("light_color", [1.0, 1.0, 1.0])
            )
            toggle_light(True)
        
        self.report({'INFO'}, f"Zastosowano styl: {design['name']}")
        return {'FINISHED'}


class AIDESIGN_OT_ToggleLight(Operator):
    """Włącz/Wyłącz światło"""
    bl_idname = "aidesign.toggle_light"
    bl_label = "Przełącz Światło"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        lamp = bpy.data.objects.get("Lamp")
        
        if not lamp:
            self.report({'ERROR'}, "Brak obiektu Lamp")
            return {'CANCELLED'}
        
        is_on = lamp.data.energy > 0
        toggle_light(not is_on)
        
        status = "wyłączone" if is_on else "włączone"
        self.report({'INFO'}, f"Światło {status}")
        return {'FINISHED'}


class AIDESIGN_OT_RandomDesign(Operator):
    """Wygeneruj losowy design"""
    bl_idname = "aidesign.random_design"
    bl_label = "Losowy Design"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        import random
        
        styles = ['minimalist', 'cozy', 'futuristic', 'industrial', 'scandinavian']
        random_style = random.choice(styles)
        
        print(f"\n🎲 Losowy styl: {random_style}")
        
        bpy.ops.aidesign.apply_style(style=random_style)
        
        self.report({'INFO'}, f"Wygenerowano losowy design!")
        return {'FINISHED'}


class AIDESIGN_OT_RandomColor(Operator):
    """Losowy kolor dla obiektu"""
    bl_idname = "aidesign.random_color"
    bl_label = "Losowy Kolor"
    bl_options = {'REGISTER', 'UNDO'}
    
    object_name: EnumProperty(
        name="Obiekt",
        items=[
            ('Walls', 'Ściany', ''),
            ('Sofa', 'Sofa', ''),
            ('Carpet', 'Dywan', ''),
            ('Zaslona1', 'Zasłony', ''),
        ]
    )
    
    def execute(self, context):
        import random
        
        r = random.uniform(0.2, 0.9)
        g = random.uniform(0.2, 0.9)
        b = random.uniform(0.2, 0.9)
        color = (r, g, b, 1.0)
        
        set_material_color(self.object_name, color)
        
        if self.object_name == "Zaslona1":
            set_material_color("Zaslona2", color)
        
        self.report({'INFO'}, f"Zmieniono kolor: {self.object_name}")
        return {'FINISHED'}


class AIDESIGN_OT_ResetColors(Operator):
    """Przywróć domyślne kolory"""
    bl_idname = "aidesign.reset_colors"
    bl_label = "Reset Kolorów"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        # Neutralne szare kolory
        set_material_color("Walls", [0.8, 0.8, 0.8, 1.0])
        set_material_color("Sofa", [0.6, 0.6, 0.6, 1.0])
        set_material_color("Carpet", [0.7, 0.7, 0.7, 1.0])
        set_material_color("Zaslona1", [0.9, 0.9, 0.9, 1.0])
        set_material_color("Zaslona2", [0.9, 0.9, 0.9, 1.0])
        set_material_color("FloorPlates", [0.85, 0.85, 0.85, 1.0])
        set_material_color("FloorUnder", [0.75, 0.75, 0.75, 1.0])
        
        self.report({'INFO'}, "Przywrócono domyślne kolory")
        return {'FINISHED'}


# ============================================================
# PANEL UI
# ============================================================

class AIDESIGN_PT_MainPanel(Panel):
    """Panel AI Design Configurator - SAFE VERSION"""
    bl_label = "AI Design (Safe)"
    bl_idname = "AIDESIGN_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'AI Design'
    
    def draw(self, context):
        layout = self.layout
        
        box = layout.box()
        box.label(text="🤖 AI Interior Configurator", icon='HOME')
        box.label(text="⚠️ Wersja bezpieczna (tylko kolory)", icon='INFO')
        
        layout.separator()
        box = layout.box()
        box.label(text="🎨 Style AI", icon='COLOR')
        
        col = box.column(align=True)
        col.operator("aidesign.apply_style", text="Minimalist").style = 'minimalist'
        col.operator("aidesign.apply_style", text="Cozy").style = 'cozy'
        col.operator("aidesign.apply_style", text="Futuristic").style = 'futuristic'
        col.operator("aidesign.apply_style", text="Industrial").style = 'industrial'
        col.operator("aidesign.apply_style", text="Scandinavian").style = 'scandinavian'
        
        layout.separator()
        box = layout.box()
        box.label(text="💡 Oświetlenie", icon='LIGHT')
        box.operator("aidesign.toggle_light", text="Przełącz Światło", icon='OUTLINER_OB_LIGHT')
        
        layout.separator()
        layout.operator("aidesign.random_design", text="🎲 Losowy Styl", icon='FILE_REFRESH')
        
        layout.separator()
        box = layout.box()
        box.label(text="🎨 Losowe Kolory", icon='BRUSH_DATA')
        
        col = box.column(align=True)
        col.operator("aidesign.random_color", text="Losuj Kolor Ścian").object_name = 'Walls'
        col.operator("aidesign.random_color", text="Losuj Kolor Sofy").object_name = 'Sofa'
        col.operator("aidesign.random_color", text="Losuj Kolor Dywanu").object_name = 'Carpet'
        col.operator("aidesign.random_color", text="Losuj Kolor Zasłon").object_name = 'Zaslona1'
        
        layout.separator()
        layout.operator("aidesign.reset_colors", text="↺ Reset Kolorów", icon='LOOP_BACK')


# ============================================================
# REJESTRACJA
# ============================================================

classes = (
    AIDESIGN_OT_ApplyStyle,
    AIDESIGN_OT_ToggleLight,
    AIDESIGN_OT_RandomDesign,
    AIDESIGN_OT_RandomColor,
    AIDESIGN_OT_ResetColors,
    AIDESIGN_PT_MainPanel,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    print("\n✅ AI Design Configurator (SAFE) zarejestrowany!")
    print(f"📁 Używam designs.json z: {DESIGNS_JSON_PATH}")
    print("⚠️ Ta wersja NIE zmienia pozycji obiektów\n")


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
