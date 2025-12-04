#!/usr/bin/env python3
"""
Script de validación del módulo jw_documents_extension
Valida la estructura, modelos, vistas y permisos.
"""

import os
import sys
from pathlib import Path

# Colores para salida en terminal
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

def print_section(title):
    """Imprime un título de sección"""
    print(f"\n{Colors.BLUE}{'='*60}{Colors.END}")
    print(f"{Colors.BLUE}{title}{Colors.END}")
    print(f"{Colors.BLUE}{'='*60}{Colors.END}\n")

def check_file_exists(path, description):
    """Valida que un archivo existe"""
    if os.path.exists(path):
        print(f"{Colors.GREEN}✓{Colors.END} {description}: {path}")
        return True
    else:
        print(f"{Colors.RED}✗{Colors.END} {description} NO EXISTE: {path}")
        return False

def check_file_content(path, required_strings, description):
    """Valida que un archivo contiene ciertos strings"""
    if not os.path.exists(path):
        print(f"{Colors.RED}✗{Colors.END} {description}: archivo no existe")
        return False
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    all_found = True
    for required_str in required_strings:
        if required_str in content:
            print(f"{Colors.GREEN}✓{Colors.END} {description} - encontrado: {required_str}")
        else:
            print(f"{Colors.RED}✗{Colors.END} {description} - NO ENCONTRADO: {required_str}")
            all_found = False
    
    return all_found

def main():
    """Función principal de validación"""
    module_path = Path(__file__).parent
    
    print_section("VALIDACIÓN DEL MÓDULO jw_documents_extension (Refactorizado)")
    
    # 1. Validar estructura de directorios
    print_section("1. Estructura de Directorios")
    
    required_dirs = [
        (module_path / "models", "Directorio models"),
        (module_path / "views", "Directorio views"),
        (module_path / "security", "Directorio security"),
        (module_path / "tests", "Directorio tests"),
    ]
    
    dirs_ok = True
    for dir_path, description in required_dirs:
        if dir_path.exists():
            print(f"{Colors.GREEN}✓{Colors.END} {description}")
        else:
            print(f"{Colors.RED}✗{Colors.END} {description} NO EXISTE")
            dirs_ok = False
    
    # 2. Validar archivos base
    print_section("2. Archivos Base del Módulo")
    
    base_files = [
        (module_path / "__init__.py", "Archivo __init__.py"),
        (module_path / "__manifest__.py", "Archivo __manifest__.py"),
    ]
    
    files_ok = True
    for file_path, description in base_files:
        files_ok &= check_file_exists(file_path, description)
    
    # 3. Validar contenido de __manifest__.py
    print_section("3. Contenido de __manifest__.py")
    
    manifest_checks = [
        "JW Documents Extension",
        "17.0",
        "Gestión documentaria",
        "'base'",
        "'mail'",
    ]
    
    manifest_ok = check_file_content(
        module_path / "__manifest__.py",
        manifest_checks,
        "Manifest"
    )
    
    # 4. Validar modelo
    print_section("4. Modelo de Datos (jw.documento)")
    
    model_checks = [
        "class JWDocumento",
        "_name = 'jw.documento'",
        "archivo = fields.Binary",
        "tipo_documento",
        "ubicacion_fisica",
        "responsable_custodia",
        "DOCUMENTO_TYPE",
        "mail.thread",
    ]
    
    model_ok = check_file_content(
        module_path / "models" / "jw_documento.py",
        model_checks,
        "Modelo jw_documento"
    )
    
    # 5. Validar vistas XML
    print_section("5. Vistas XML")
    
    views_checks = [
        "view_jw_documento_form",
        "view_jw_documento_tree",
        "view_jw_documento_search",
        "tipo_documento",
        "filter_administrativo",
        "filter_estudiantil",
        "filter_oficial",
    ]
    
    views_ok = check_file_content(
        module_path / "views" / "jw_documento_views.xml",
        views_checks,
        "Vistas XML"
    )
    
    # 6. Validar menús
    print_section("6. Menús")
    
    menus_checks = [
        "menu_jw_documentos_root",
        "action_jw_documento_view",
        "Gestión Documentaria",
        "Documentos Administrativos",
        "Documentos Estudiantiles",
        "Documentos Oficiales",
    ]
    
    menus_ok = check_file_content(
        module_path / "views" / "jw_documento_menus.xml",
        menus_checks,
        "Menús"
    )
    
    # 7. Validar seguridad (ACL)
    print_section("7. Control de Acceso (ACL)")
    
    security_file = module_path / "security" / "ir.model.access.csv"
    if check_file_exists(security_file, "Archivo ir.model.access.csv"):
        with open(security_file, 'r') as f:
            lines = f.readlines()
        print(f"{Colors.GREEN}✓{Colors.END} Número de permisos definidos: {len(lines) - 1}")
    
    security_checks = [
        "jw.documento",
        "group_jw_documentos_usuarios",
        "group_jw_documentos_administrador",
    ]
    security_ok = check_file_content(
        security_file,
        security_checks,
        "Permisos"
    )
    
    # 8. Validar grupos
    print_section("8. Grupos de Seguridad")
    
    groups_checks = [
        "group_jw_documentos_usuarios",
        "group_jw_documentos_administrador",
        "Usuarios de Documentos",
        "Administrador de Documentos",
    ]
    
    groups_ok = check_file_content(
        module_path / "security" / "jw_documents_groups.xml",
        groups_checks,
        "Grupos"
    )
    
    # 9. Validar pruebas unitarias
    print_section("9. Pruebas Unitarias")
    
    test_checks = [
        "class JWDocumentoTestCase",
        "test_create_documento_basico",
        "test_create_documento_completo",
        "test_documento_sin_archivo_falla",
        "test_tipos_documento_validos",
        "test_search_by_tipo_documento",
        "test_search_by_responsable",
    ]
    
    tests_ok = check_file_content(
        module_path / "tests" / "test_jw_documento.py",
        test_checks,
        "Pruebas"
    )
    
    # Resumen final
    print_section("RESUMEN DE VALIDACIÓN")
    
    all_ok = (dirs_ok and files_ok and manifest_ok and model_ok and 
              views_ok and menus_ok and security_ok and groups_ok and tests_ok)
    
    print(f"\nComponentes validados:")
    print(f"  {Colors.GREEN}✓{Colors.END} Estructura de directorios" if dirs_ok else f"  {Colors.RED}✗{Colors.END} Estructura de directorios")
    print(f"  {Colors.GREEN}✓{Colors.END} Archivos base" if files_ok else f"  {Colors.RED}✗{Colors.END} Archivos base")
    print(f"  {Colors.GREEN}✓{Colors.END} Manifest" if manifest_ok else f"  {Colors.RED}✗{Colors.END} Manifest")
    print(f"  {Colors.GREEN}✓{Colors.END} Modelo jw.documento" if model_ok else f"  {Colors.RED}✗{Colors.END} Modelo jw.documento")
    print(f"  {Colors.GREEN}✓{Colors.END} Vistas" if views_ok else f"  {Colors.RED}✗{Colors.END} Vistas")
    print(f"  {Colors.GREEN}✓{Colors.END} Menús" if menus_ok else f"  {Colors.RED}✗{Colors.END} Menús")
    print(f"  {Colors.GREEN}✓{Colors.END} Control de acceso" if security_ok else f"  {Colors.RED}✗{Colors.END} Control de acceso")
    print(f"  {Colors.GREEN}✓{Colors.END} Grupos de seguridad" if groups_ok else f"  {Colors.RED}✗{Colors.END} Grupos de seguridad")
    print(f"  {Colors.GREEN}✓{Colors.END} Pruebas unitarias" if tests_ok else f"  {Colors.RED}✗{Colors.END} Pruebas unitarias")
    
    if all_ok:
        print(f"\n{Colors.GREEN}✓ TODAS LAS VALIDACIONES PASARON{Colors.END}")
        print(f"\n{Colors.GREEN}El módulo jw_documents_extension está correctamente refactorizado y listo para usar.{Colors.END}")
        return 0
    else:
        print(f"\n{Colors.RED}✗ ALGUNAS VALIDACIONES FALLARON{Colors.END}")
        print(f"\n{Colors.YELLOW}Por favor, revisa los errores anteriores.{Colors.END}")
        return 1

if __name__ == '__main__':
    sys.exit(main())
