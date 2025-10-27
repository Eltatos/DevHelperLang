#!/usr/bin/env python3
"""
DEVHELPER LANGUAGE v2.0 - LENGUAJE OFICIAL
Domain-Specific Language for Rapid Development
"""

import os
import sys
import json
import time

class DevHelperLanguage:
    def __init__(self):
        self.version = "2.0.0"
        self.author = "DevHelper Language Team"
        self.archivo_actual = None
        self.contenido_actual = []

        # Mostrar banner de inicio
        self.mostrar_banner()

        # Cargar sistema del lenguaje
        self.sistema = self.cargar_sistema_lenguaje()

    def mostrar_banner(self):                                   """Banner oficial de DevHelper Language"""
        print(f"""
    ╔══════════════════════════════════════════╗
    ║           🚀 DEVHELPER LANGUAGE         ║
    ║               v{self.version} - OFICIAL     ║
    ║        Code Faster, Create Smarter      ║
    ║                                          ║
    ║   Lenguaje Específico de Dominio (DSL)  ║
    ║     para Desarrollo Rápido en Móviles   ║
    ╚══════════════════════════════════════════╝
        """)

    def cargar_sistema_lenguaje(self):
        """Sistema completo de DevHelper Language"""
        return {
            'comandos': {
                '@crear': self.comando_crear,
                '@editar': self.comando_editar,
                '@snippet': self.comando_snippet,
                '@ayuda': self.comando_ayuda,
                '@proyecto': self.comando_proyecto,
                '@eliminar': self.comando_eliminar,
                '@listar': self.comando_listar,
                '@permisos': self.comando_permisos,
                '@ejemplo': self.comando_ejemplo,
                '@version': self.comando_version
            },
            'templates': self.cargar_templates_oficiales(),
            'config': {
                'extension': '.dhl',
                'lenguajes': ['html5', 'css3', 'javascript', 'java', 'python'],
                'version': self.version
            }
        }

    def cargar_templates_oficiales(self):
        """Templates oficiales del lenguaje"""
        return {
            'html5': {
                'pagina_completa': '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{titulo}</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header class="header">
        <nav class="nav">
            <div class="logo">{titulo}</div>
            <ul class="nav-menu">
                <li><a href="#inicio">Inicio</a></li>
                <li><a href="#acerca">Acerca</a></li>
                <li><a href="#contacto">Contacto</a></li>
            </ul>
        </nav>
    </header>

    <main class="main">
        <section id="inicio" class="hero">
            <h1>Bienvenido a {titulo}</h1>
            <p>Creado con DevHelper Language v{version}</p>
            <button class="btn">Comenzar</button>
        </section>
    </main>

    <footer class="footer">
        <p>&copy; 2024 {titulo}. Todos los derechos reservados.</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>''',

                'formulario': '''<form class="form" action="/enviar" method="POST">
    <h2>{titulo_form}</h2>

    <div class="form-group">
        <label for="nombre">Nombre:</label>
        <input type="text" id="nombre" name="nombre" required>
    </div>

    <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
    </div>

    <div class="form-group">
        <label for="mensaje">Mensaje:</label>
        <textarea id="mensaje" name="mensaje" rows="4" required></textarea>
    </div>

    <button type="submit" class="btn">{texto_boton}</button>
</form>''',

                'tarjeta': '''<div class="card">
    <div class="card-header">
        <h3>{titulo}</h3>
    </div>
    <div class="card-body">
        <p>{descripcion}</p>
        <div class="card-footer">
            <button class="btn">{boton_texto}</button>
        </div>
    </div>
</div>'''
            },

            'css3': {
                'estilos_completos': '''/* {nombre} - DevHelper Language v{version} */
* {{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}}

body {{
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f4f4f4;
}}

.container {{
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}}

.header {{
    background: #2c3e50;
    color: white;
    padding: 1rem 0;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}}

.nav {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}}

.logo {{
    font-size: 1.5rem;
    font-weight: bold;
}}

.nav-menu {{
    display: flex;
    list-style: none;
    gap: 2rem;
}}

.nav-menu a {{
    color: white;
    text-decoration: none;
    transition: color 0.3s;
}}

.nav-menu a:hover {{
    color: #3498db;
}}

.hero {{
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 4rem 0;
    text-align: center;
}}

.hero h1 {{
    font-size: 3rem;
    margin-bottom: 1rem;
}}

.btn {{
    background: #e74c3c;
    color: white;
    border: none;
    padding: 12px 30px;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1rem;
    transition: background 0.3s;
}}

.btn:hover {{
    background: #c0392b;
}}

.form {{
    background: white;
    padding: 2rem;
    border-radius: 10px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    max-width: 500px;
    margin: 2rem auto;
}}

.form-group {{
    margin-bottom: 1rem;
}}

.form-group label {{
    display: block;
    margin-bottom: 0.5rem;
    font-weight: bold;
}}

.form-group input,
.form-group textarea {{
    width: 100%;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
    font-size: 1rem;
}}

.card {{
    background: white;
    border-radius: 10px;
    box-shadow: 0 3px 10px rgba(0,0,0,0.1);
    overflow: hidden;
    margin: 1rem;
}}

.card-header {{
    background: #34495e;
    color: white;
    padding: 1rem;
}}

.card-body {{
    padding: 1.5rem;
}}

.card-footer {{
    padding: 1rem;
    background: #f8f9fa;
    text-align: center;
}}

.footer {{
    background: #2c3e50;
    color: white;
    text-align: center;
    padding: 2rem 0;
    margin-top: 3rem;
}}

/* Responsive */
@media (max-width: 768px) {{
    .nav {{
        flex-direction: column;
        gap: 1rem;
    }}

    .nav-menu {{
        flex-direction: column;
        gap: 1rem;
        text-align: center;
    }}

    .hero h1 {{
        font-size: 2rem;
    }}
}}''',

                'grid_sistema': '''.grid-container {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    padding: 2rem;
}}

.grid-item {{
    background: white;
    padding: 2rem;
    border-radius: 10px;
    box-shadow: 0 3px 10px rgba(0,0,0,0.1);
    text-align: center;
}}'''
            },

            'javascript': {
                'aplicacion_completa': '''// {nombre} - DevHelper Language v{version}
class {Clase} {{
    constructor() {{
        this.inicializado = false;
        this.config = {{
            version: '{version}',
            nombre: '{nombre}'
        }};
        this.init();
    }}

    init() {{
        console.log('🚀 {Clase} inicializada');
        this.inicializado = true;
        this.cargarEventos();
        this.mostrarMensaje();
    }}

    cargarEventos() {{
        // Eventos del DOM
        document.addEventListener('DOMContentLoaded', () => {{
            console.log('✅ DOM cargado');
            this.manejarFormularios();
            this.manejarBotones();
        }});
    }}

    manejarFormularios() {{
        const forms = document.querySelectorAll('form');
        forms.forEach(form => {{
            form.addEventListener('submit', (e) => {{
                e.preventDefault();
                this.enviarFormulario(form);
            }});
        }});
    }}

    manejarBotones() {{
        const botones = document.querySelectorAll('.btn');
        botones.forEach(btn => {{
            btn.addEventListener('click', (e) => {{
                this.manejarClickBoton(e.target);
            }});
        }});
    }}

    enviarFormulario(form) {{
        const formData = new FormData(form);
        const datos = Object.fromEntries(formData);

        console.log('📤 Enviando formulario:', datos);
        alert('Formulario enviado correctamente');
        form.reset();
    }}

    manejarClickBoton(boton) {{
        console.log('🖱️ Botón clickeado:', boton.textContent);
        // Aquí tu lógica para botones
    }}

    mostrarMensaje() {{
        console.log('🎉 ¡Aplicación {nombre} funcionando!');
    }}
}}

// Inicializar aplicación
const app = new {Clase}();''',

                'utilidades': '''// Utilidades - DevHelper Language
const {nombre} = {{
    // Selectores rápidos
    $: (selector) => document.querySelector(selector),
    $$: (selector) => document.querySelectorAll(selector),

    // Manejo de eventos
    on: (elemento, evento, callback) => {{
        elemento.addEventListener(evento, callback);
    }},

    // HTTP requests
    async get(url) {{
        try {{
            const response = await fetch(url);
            return await response.json();
        }} catch (error) {{
            console.error('Error GET:', error);
        }}
    }},

    async post(url, datos) {{
        try {{
            const response = await fetch(url, {{
                method: 'POST',
                headers: {{
                    'Content-Type': 'application/json',
                }},
                body: JSON.stringify(datos)
            }});
            return await response.json();
        }} catch (error) {{
            console.error('Error POST:', error);
        }}
    }},

    // Almacenamiento local
    guardar: (clave, valor) => {{
        localStorage.setItem(clave, JSON.stringify(valor));
    }},

    cargar: (clave) => {{
        return JSON.parse(localStorage.getItem(clave));
    }},

    // Utilidades de DOM
    crearElemento: (tag, contenido, clases = []) => {{
        const elemento = document.createElement(tag);
        elemento.innerHTML = contenido;
        clases.forEach(clase => elemento.classList.add(clase));
        return elemento;
    }},

    // Animaciones
    animar: (elemento, animacion) => {{
        elemento.style.animation = animacion;
    }}
}};

// Hacer disponibles globalmente
window.{nombre} = {nombre};
console.log('✅ Utilidades {nombre} cargadas');'''
            }
        }

    def comando_crear(self, args):
        """@crear [tipo] [nombre] - Crear archivos con templates"""
        if len(args) < 2:
            print("❌ Uso: @crear [tipo] [nombre]")
            print("   Tipos: html5, css3, javascript")
            return

        tipo, nombre = args[0], args[1]

        if tipo in self.sistema['templates']:
            # Obtener el primer template del tipo
            template_nombre, template = list(self.sistema['templates'][tipo].items())[0]

            # Personalizar template
            contenido = template.format(
                titulo=nombre,
                titulo_form=f"Formulario {nombre}",
                texto_boton="Enviar",
                boton_texto="Acción",
                descripcion=f"Descripción de {nombre}",
                nombre=nombre,
                Clase=nombre.title(),
                version=self.version
            )

            # Determinar extensión
            extensiones = {'html5': '.html', 'css3': '.css', 'javascript': '.js'}
            extension = extensiones.get(tipo, '.txt')
            archivo = f"{nombre}{extension}"

            with open(archivo, 'w', encoding='utf-8') as f:
                f.write(contenido)

            print(f"✅ Archivo '{archivo}' creado")
            print(f"📁 Template: {template_nombre}")
            print(f"📏 Tamaño: {len(contenido)} caracteres")

        else:
            print(f"❌ Tipo '{tipo}' no soportado")
            print("💡 Tipos disponibles: html5, css3, javascript")

    def comando_editar(self, args):
        """@editar [archivo] - Editor integrado"""
        if not args:
            print("❌ Uso: @editar [archivo]")
            return

        archivo = args[0]
        self.editor_dhl(archivo)

    def comando_snippet(self, args):
        """@snippet [lenguaje] - Mostrar código reusable"""
        lenguaje = args[0] if args else 'html5'

        if lenguaje in self.sistema['templates']:
            print(f"\n🎯 SNIPPETS {lenguaje.upper()}:")
            print("═" * 50)

            for nombre, codigo in self.sistema['templates'][lenguaje].items():
                primera_linea = codigo.split('\n')[0]
                print(f"\n🔹 {nombre}:")
                print(f"   {primera_linea[:60]}...")
                print(f"   📏 {len(codigo)} caracteres")

        else:
            print(f"❌ Lenguaje '{lenguaje}' no soportado")
            print("💡 Lenguajes: html5, css3, javascript")

    def comando_ayuda(self, args):
        """@ayuda - Sistema de ayuda completo"""
        ayuda = """
📚 DEVHELPER LANGUAGE - SISTEMA DE AYUDA OFICIAL

🎯 COMANDOS PRINCIPALES:
  @crear [tipo] [nombre]    - Crear archivo con template
  @editar [archivo]         - Abrir editor integrado
  @snippet [lenguaje]       - Mostrar código reusable
  @proyecto [nombre]        - Crear proyecto completo
  @listar                   - Ver archivos disponibles
  @eliminar [archivo]       - Eliminar archivo
  @permisos                 - Verificar configuración
  @ejemplo                  - Ejemplos prácticos
  @version                  - Información de versión
  @ayuda                    - Esta ayuda

🚀 EJEMPLOS PRÁCTICOS:
  @crear html5 mi_pagina
  @crear css3 estilos
  @crear javascript app
  @proyecto sitio_web
  @editar mi_pagina.html

📖 LENGUAJES SOPORTADOS:
  • html5       - Páginas web completas
  • css3        - Estilos modernos y responsive
  • javascript  - Aplicaciones interactivas

💡 CARACTERÍSTICAS:
  • Templates profesionales
  • Código listo para usar
  • Diseño responsive incluido
  • Estructura organizada
  • Comentarios explicativos

🔧 EDITOR INTEGRADO:
  • Numeración de líneas
  • Guardado automático
  • Navegación fácil
  • Compatible con móviles
        """
        print(ayuda)

    def comando_proyecto(self, args):
        """@proyecto [nombre] - Crear proyecto completo"""
        if not args:
            print("❌ Uso: @proyecto [nombre]")
            return

        nombre = args[0]
        print(f"🚀 Creando proyecto: {nombre}")

        estructura = {
            f"{nombre}/": "📁 Carpeta principal",
            f"{nombre}/index.html": "📄 Página principal",
            f"{nombre}/styles.css": "🎨 Estilos principales",
            f"{nombre}/script.js": "⚡ Lógica de la aplicación",
            f"{nombre}/assets/": "📁 Imágenes y recursos",
            f"{nombre}/README.md": "📖 Documentación"
        }

        for ruta, descripcion in estructura.items():
            if ruta.endswith('/'):
                os.makedirs(ruta, exist_ok=True)
                print(f"✅ {descripcion}")
            else:
                with open(ruta, 'w', encoding='utf-8') as f:
                    if 'index.html' in ruta:
                        f.write(self.sistema['templates']['html5']['pagina_completa'].format(
                            titulo=nombre, version=self.version
                        ))
                    elif 'styles.css' in ruta:
                        f.write(self.sistema['templates']['css3']['estilos_completos'].format(
                            nombre=nombre, version=self.version
                        ))
                    elif 'script.js' in ruta:
                        f.write(self.sistema['templates']['javascript']['aplicacion_completa'].format(
                            nombre=nombre, Clase=nombre.title(), version=self.version
                        ))
                    else:
                        f.write(f"# {nombre}\n\nProyecto creado con DevHelper Language v{self.version}")
                print(f"✅ {descripcion}")

        print(f"\n🎉 ¡Proyecto '{nombre}' creado exitosamente!")
        print("📁 Estructura creada:")
        for ruta in estructura:
            print(f"   📄 {ruta}")

    def comando_eliminar(self, args):
        """@eliminar [archivo] - Eliminar archivos"""
        if not args:
            print("❌ Uso: @eliminar [archivo]")
            return

        archivo = args[0]
        if os.path.exists(archivo):
            confirmar = input(f"⚠️  ¿Eliminar '{archivo}'? (s/n): ")
            if confirmar.lower() == 's':
                os.remove(archivo)
                print(f"✅ '{archivo}' eliminado")
        else:
            print(f"❌ Archivo '{archivo}' no existe")

    def comando_listar(self, args):
        """@listar - Mostrar archivos del proyecto"""
        archivos = os.listdir('.')
        print("\n📁 ARCHIVOS EN EL PROYECTO:")
        print("═" * 40)

        for archivo in sorted(archivos):
            if os.path.isfile(archivo):
                tamaño = os.path.getsize(archivo)
                icono = "📄"
                if archivo.endswith('.html'): icono = " 🌐"
                elif archivo.endswith('.css'): icono = "🎨"
                elif archivo.endswith('.js'): icono = " ⚡"
                elif archivo.endswith('.dhl'): icono = "🚀"

                print(f"   {icono} {archivo:<25} ({tamaño:>6} bytes)")
            else:
                print(f"   📁 {archivo}/")

        print(f"═" * 40)
        print(f"📊 Total: {len(archivos)} elementos")

    def comando_permisos(self, args):
        """@permisos - Verificar configuración del sistema"""
        print("\n🔐 VERIFICACIÓN DE SISTEMA DEVHELPER LANGUAGE")
        print("═" * 50)

        # Verificar instalación
        checks = [
            ("Versión del lenguaje", f"v{self.version}  ✅"),
            ("Directorio DevHelper", "~/.devhelper/ ✅" if os.path.exists(os.path.expanduser("~/.devhelper")) else "❌ No encontrado"),
            ("Comando 'devhelper'", "✅ Disponible" if any(os.path.exists(os.path.join(p, 'devhelper')) for p in os.getenv('PATH').split(':')) else "❌ No disponible"),
            ("Permisos almacenamiento", "✅ Concedidos" if os.path.exists("/storage/emulated/0") else "⚠️  Ejecuta: termux-setup-storage")
        ]

        for check, estado in checks:
            print(f"   {check:<25} {estado}")

        print("\n💡 SOLUCIÓN DE PROBLEMAS:")
        print("   Si hay problemas, ejecuta: termux-setup-storage")
        print("   O reinstala con el instalador oficial")

    def comando_ejemplo(self, args):
        """@ejemplo - Mostrar ejemplos prácticos"""
        ejemplos = """
🎯 EJEMPLOS PRÁCTICOS - DEVHELPER LANGUAGE

1. CREAR SITIO WEB COMPLETO:
   @proyecto mi_sitio_web
   @editar mi_sitio_web/index.html

2. CREAR COMPONENTES HTML:
   @crear html5 formulario_contacto
   @crear html5 tarjeta_producto

3. CREAR ESTILOS PROFESIONALES:
   @crear css3 estilos_principales
   @snippet css3

4. CREAR APLICACIÓN JAVASCRIPT:
   @crear javascript mi_aplicacion
   @snippet javascript

5. GESTIONAR ARCHIVOS:
   @listar
   @eliminar archivo_viejo.html
   @editar archivo_nuevo.js

💡 CONSEJO: Usa @snippet para ver código reusable
        """
        print(ejemplos)

    def comando_version(self, args):
        """@version - Información de la versión"""
        print(f"""
🏷️  INFORMACIÓN DE VERSIÓN:

   DevHelper Language v{self.version}
   Tipo: Lenguaje Específico de Dominio (DSL)
   Propósito: Desarrollo rápido en dispositivos móviles
   Autor: {self.author}
   Licencia: MIT Open Source

📦 CARACTERÍSTICAS:
   • Sistema de templates profesional
   • Editor de código integrado
   • Gestor de proyectos
   • Multi-lenguaje (HTML5, CSS3, JavaScript)
   • Optimizado para Termux/Android

🌍 COMUNIDAD:
   ¡Bienvenido a la comunidad DevHelper Language!
   Reporta problemas y sugiere mejoras.
        """)

    def editor_dhl(self, archivo):
        """Editor integrado de DevHelper Language"""
        # Cargar archivo si existe
        if os.path.exists(archivo):
            with open(archivo, 'r', encoding='utf-8') as f:
                self.contenido_actual = f.readlines()
        else:
            self.contenido_actual = []
            print(f"🆕 Creando nuevo archivo: {archivo}")

        self.archivo_actual = archivo

        print(f"\n📝 EDITOR DEVHELPER - {archivo}")
        print("═" * 50)

        while True:
            # Mostrar contenido actual
            for i, linea in enumerate(self.contenido_actual, 1):
                print(f"{i:3d} │ {linea.rstrip()}")

            print("═" * 50)
            print("💾 [g] Guardar | [q] Salir | [@] Comando DevHelper")
            print("📝 Escribe código o número de línea para editar:")
            print("   :d [n] Eliminar línea | :a [n] [texto] Agregar")

            entrada = input("\n📝 >> ").strip()

            if entrada == 'g':
                self.guardar_archivo()
                print("💾 Archivo guardado")
            elif entrada == 'q':
                if self.contenido_actual and input("¿Salir sin guardar? (s/n): ").lower() == 's':
                    break
                else:
                    self.guardar_archivo()
                    break
            elif entrada.startswith('@'):
                self.procesar_comando_linea(entrada[1:])
            elif entrada.startswith(':d '):
                try:
                    num = int(entrada[3:])
                    if 1 <= num <= len(self.contenido_actual):
                        self.contenido_actual.pop(num-1)
                        print(f"✅ Línea {num} eliminada")
                except:
                    print("❌ Número de línea inválido")
            elif entrada.startswith(':a '):
                try:
                    partes = entrada[3:].split(' ', 1)
                    num = int(partes[0])
                    texto = partes[1] if len(partes) > 1 else ""
                    if 1 <= num <= len(self.contenido_actual):
                        self.contenido_actual.insert(num, texto + '\n')
                        print(f"✅ Línea agregada después de {num}")
                except:
                    print("❌ Formato: :a [número] [texto]")
            elif entrada.isdigit():
                try:
                    num = int(entrada)
                    if 1 <= num <= len(self.contenido_actual):
                        nuevo_texto = input(f"📝 Editar línea {num}: ")
                        self.contenido_actual[num-1] = nuevo_texto + '\n'
                except:
                    print("❌ Número de línea inválido")
            else:
                # Agregar como nueva línea
                self.contenido_actual.append(entrada + '\n')

    def guardar_archivo(self):
        """Guardar archivo actual"""
        if self.archivo_actual and self.contenido_actual:
            with open(self.archivo_actual, 'w', encoding='utf-8') as f:
                f.writelines(self.contenido_actual)
            return True
        return False

    def procesar_comando_linea(self, comando):
        """Procesar comandos DevHelper desde el editor"""
        partes = comando.strip().split()
        if not partes:
            return

        cmd = partes[0]
        args = partes[1:] if len(partes) > 1 else []

        if cmd in self.sistema['comandos']:
            self.sistema['comandos'][cmd](args)
        else:
            print(f"❌ Comando '@{cmd}' no reconocido")
            print("💡 Usa @ayuda para ver comandos disponibles")

    def ejecutar_comando(self, comando):
        """Ejecutar un comando específico"""
        if comando.startswith('@'):
            self.procesar_comando_linea(comando[1:])
        else:
            print("❌ Los comandos deben empezar con @")
            print("💡 Ejemplo: @ayuda")

    def modo_interactivo(self):
        """Modo interactivo de DevHelper Language"""
        print("💻 MODO INTERACTIVO - DevHelper Language")
        print("Escribe comandos @ o 'salir' para terminar")
        print("Usa @ayuda para ver todos los comandos")
        print("═" * 50)

        while True:
            try:
                comando = input("DevHelper> ").strip()

                if comando.lower() in ['salir', 'exit', 'quit']:
                    print("👋 ¡Hasta luego!")
                    break
                elif comando:
                    self.ejecutar_comando(comando)

            except KeyboardInterrupt:
                print("\n👋 ¡Hasta luego!")
                break
            except Exception as e:
                print(f"❌ Error: {e}")

def main():
    """Función principal de DevHelper Language"""
    try:
        dhl = DevHelperLanguage()

        if len(sys.argv) > 1:
            # Modo comando directo
            comando_completo = ' '.join(sys.argv[1:])
            dhl.ejecutar_comando(comando_completo)
        else:
            # Modo interactivo
            dhl.modo_interactivo()

    except KeyboardInterrupt:
        print("\n👋 ¡Hasta luego!")
    except Exception as e:
        print(f"❌ Error crítico: {e}")
        print("💡 Ejecuta: devhelper @permisos para verificar instalación")

if __name__ == "__main__":
    main()
