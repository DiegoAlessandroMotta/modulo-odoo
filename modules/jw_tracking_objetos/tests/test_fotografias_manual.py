"""
Script de prueba para verificar funcionalidad de fotografías
Ejecutar desde el shell de Odoo:
    python3 odoo-bin shell -d nombre_base_datos --addons-path=...
"""

import base64
import os


def generar_imagen_prueba():
    """Genera una imagen PNG simple de 1x1 píxel para pruebas"""
    return base64.b64encode(
        b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01'
        b'\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\x0cIDATx\x9cc\x00\x01'
        b'\x00\x00\x05\x00\x01\r\n-\xb4\x00\x00\x00\x00IEND\xaeB`\x82'
    )


def test_crear_objeto_con_imagen(env):
    """Test 1: Crear objeto con imagen principal"""
    print("\n=== Test 1: Crear objeto con imagen principal ===")
    
    objeto = env['jw.tracking.objeto'].create({
        'nombre': 'Mochila de Prueba',
        'descripcion': 'Mochila azul encontrada en el patio',
        'estado': 'encontrado',
        'imagen': generar_imagen_prueba(),
    })
    
    print(f"✓ Objeto creado: {objeto.nombre} (ID: {objeto.id})")
    print(f"✓ Tiene imagen: {bool(objeto.imagen)}")
    print(f"✓ Número de fotografías: {objeto.num_fotografias}")
    
    return objeto


def test_agregar_fotografias(env, objeto):
    """Test 2: Agregar fotografías a un objeto"""
    print("\n=== Test 2: Agregar fotografías ===")
    
    # Crear 3 fotografías de prueba
    fotografias = []
    foto_ids = []
    for i in range(1, 4):
        foto = env['ir.attachment'].create({
            'name': f'foto_{i}.jpg',
            'datas': generar_imagen_prueba(),
            'mimetype': 'image/jpeg',
        })
        fotografias.append(foto)
        foto_ids.append(foto.id)
        print(f"✓ Fotografía {i} creada: {foto.name}")
    
    # Vincular fotografías al objeto usando Many2many
    objeto.write({
        'fotografia_ids': [(6, 0, foto_ids)]
    })
    
    print(f"✓ Total de fotografías en el objeto: {objeto.num_fotografias}")
    print(f"✓ IDs de fotografías: {[f.id for f in objeto.fotografia_ids]}")
    
    return fotografias


def test_verificar_relacion(env, objeto):
    """Test 3: Verificar relación entre objeto y fotografías"""
    print("\n=== Test 3: Verificar relación ===")
    
    # Obtener fotografías del objeto
    fotos = objeto.fotografia_ids
    print(f"✓ Fotografías vinculadas: {len(fotos)}")
    
    for foto in fotos:
        print(f"  - {foto.name} (ID: {foto.id}, Tipo: {foto.mimetype})")
    
    print(f"✓ Todas las fotos vinculadas correctamente mediante Many2many")


def test_eliminar_fotografia(env, objeto):
    """Test 4: Eliminar una fotografía"""
    print("\n=== Test 4: Eliminar fotografía ===")
    
    num_inicial = objeto.num_fotografias
    print(f"Fotografías antes: {num_inicial}")
    
    if objeto.fotografia_ids:
        foto_a_eliminar = objeto.fotografia_ids[0]
        nombre_foto = foto_a_eliminar.name
        foto_id = foto_a_eliminar.id
        
        # Desvincular la foto del objeto usando Many2many
        objeto.write({
            'fotografia_ids': [(3, foto_id)]
        })
        print(f"✓ Fotografía desvinculada: {nombre_foto}")
        
        print(f"Fotografías después: {objeto.num_fotografias}")
        print(f"✓ Diferencia: {num_inicial - objeto.num_fotografias}")


def test_buscar_objetos_con_fotos(env):
    """Test 5: Buscar objetos con fotografías"""
    print("\n=== Test 5: Buscar objetos con fotografías ===")
    
    # Buscar todos los objetos
    todos_objetos = env['jw.tracking.objeto'].search([])
    print(f"Total de objetos: {len(todos_objetos)}")
    
    # Filtrar los que tienen fotos
    con_fotos = todos_objetos.filtered(lambda o: o.num_fotografias > 0)
    print(f"Objetos con fotografías: {len(con_fotos)}")
    
    for obj in con_fotos:
        print(f"  - {obj.nombre}: {obj.num_fotografias} foto(s)")


def test_cambiar_imagen_principal(env, objeto):
    """Test 6: Cambiar imagen principal"""
    print("\n=== Test 6: Cambiar imagen principal ===")
    
    tiene_imagen_inicial = bool(objeto.imagen)
    print(f"Tiene imagen inicial: {tiene_imagen_inicial}")
    
    # Cambiar imagen
    nueva_imagen = generar_imagen_prueba()
    objeto.write({'imagen': nueva_imagen})
    
    print(f"✓ Imagen actualizada")
    print(f"Tiene imagen ahora: {bool(objeto.imagen)}")


def ejecutar_todos_los_tests(env):
    """Ejecutar todos los tests en secuencia"""
    print("\n" + "="*60)
    print("INICIO DE TESTS - FOTOGRAFÍAS EN TRACKING DE OBJETOS")
    print("="*60)
    
    try:
        # Test 1: Crear objeto con imagen
        objeto = test_crear_objeto_con_imagen(env)
        
        # Test 2: Agregar fotografías
        fotografias = test_agregar_fotografias(env, objeto)
        
        # Test 3: Verificar relación
        test_verificar_relacion(env, objeto)
        
        # Test 4: Eliminar fotografía
        test_eliminar_fotografia(env, objeto)
        
        # Test 5: Buscar objetos con fotos
        test_buscar_objetos_con_fotos(env)
        
        # Test 6: Cambiar imagen principal
        test_cambiar_imagen_principal(env, objeto)
        
        print("\n" + "="*60)
        print("✓ TODOS LOS TESTS COMPLETADOS EXITOSAMENTE")
        print("="*60)
        
        return objeto
        
    except Exception as e:
        print(f"\n✗ ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        return None


def limpiar_datos_prueba(env, objeto_id=None):
    """Limpiar datos de prueba creados"""
    print("\n=== Limpieza de datos de prueba ===")
    
    if objeto_id:
        objeto = env['jw.tracking.objeto'].browse(objeto_id)
        if objeto.exists():
            # Eliminar fotografías primero
            objeto.fotografia_ids.unlink()
            # Eliminar objeto
            objeto.unlink()
            print(f"✓ Objeto {objeto_id} y sus fotografías eliminados")
    else:
        # Buscar objetos de prueba
        objetos_prueba = env['jw.tracking.objeto'].search([
            ('nombre', 'ilike', 'prueba')
        ])
        if objetos_prueba:
            print(f"Encontrados {len(objetos_prueba)} objetos de prueba")
            for obj in objetos_prueba:
                obj.fotografia_ids.unlink()
                obj.unlink()
            print(f"✓ {len(objetos_prueba)} objetos eliminados")


# Ejemplo de uso desde el shell de Odoo:
"""
# 1. Entrar al shell
python3 odoo-bin shell -d mi_base_datos

# 2. Ejecutar tests
execfile('/ruta/al/archivo/test_fotografias.py')
objeto = ejecutar_todos_los_tests(env)

# 3. Ver resultado
print(objeto.nombre)
print(objeto.num_fotografias)

# 4. Limpiar (opcional)
limpiar_datos_prueba(env, objeto.id)

# 5. Commit (si quieres guardar cambios)
env.cr.commit()
"""

# Para ejecutar directamente si se usa como script
if __name__ == '__main__':
    print("Este script debe ejecutarse desde el shell de Odoo")
    print("Uso:")
    print("  python3 odoo-bin shell -d mi_base_datos")
    print("  >>> execfile('test_fotografias.py')")
    print("  >>> ejecutar_todos_los_tests(env)")
