#!/bin/bash
# DEVHELPER LANGUAGE - INSTALADOR OFICIAL DE UN CLIC
# ¡SOLO EJECUTAR ESTE ARCHIVO!                          
echo ""
echo "🚀 INICIANDO INSTALACIÓN DEVHELPER LANGUAGE..."
echo "=============================================="
echo "No necesitas escribir comandos, todo es automático"
echo ""                                                 
# Función para mostrar progreso                         mostrar_progreso() {
    echo "✅ $1"
}

# Función para errores
error() {
    echo "❌ $1"
    exit 1
}
                                                        # 1. Verificar Termux
echo "🔍 Verificando entorno..."                        if [ ! -d "/data/data/com.termux/files/home" ]; then
    error "Este instalador es solo para Termux"
fi
                                                        # 2. Actualizar sistema silenciosamente
echo "🔄 Actualizando sistema..."
pkg update -y > /dev/null 2>&1 && pkg upgrade -y > /dev/null 2>&1
mostrar_progreso "Sistema actualizado"

# 3. Instalar Python (requerido)
echo "🐍 Instalando Python..."
pkg install -y python > /dev/null 2>&1
mostrar_progreso "Python instalado"

# 4. Crear directorios necesarios
echo "📁 Creando estructura..."
mkdir -p ~/bin ~/.devhelper ~/.devhelper/ejemplos
mostrar_progreso "Directorios creados"

# 5. Copiar archivo principal
echo "📦 Instalando DevHelper Language..."
if [ -f "src/devhelper.py" ]; then
    cp src/devhelper.py ~/.devhelper/
    mostrar_progreso "Archivos copiados"
else
    error "No se encontró src/devhelper.py - Ejecuta desde la carpeta correcta"
fi

# 6. Crear comando ejecutable
echo "⚙️ Configurando comando 'devhelper'..."
cat > ~/bin/devhelper << 'EOF'
#!/bin/bash
python ~/.devhelper/devhelper.py "$@"
EOF

chmod +x ~/bin/devhelper
mostrar_progreso "Comando 'devhelper' creado"

# 7. Configurar PATH
echo "🔧 Configurando variables..."
if ! grep -q 'export PATH="$HOME/bin:$PATH"' ~/.bashrc; then
    echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
fi

# Cargar PATH inmediatamente
export PATH="$HOME/bin:$PATH"
mostrar_progreso "Variables configuradas"

# 8. Crear archivo de configuración
echo "🎯 Creando configuración..."
cat > ~/.devhelper/config.json << EOF
{
    "version": "2.0.0",
    "instalado_el": "$(date)",
    "tipo": "instalacion_un_clic",
    "estado": "completado"
}
EOF
mostrar_progreso "Configuración guardada"

# 9. Crear ejemplos
echo "📚 Creando ejemplos..."
cat > ~/.devhelper/ejemplos/primeros_pasos.dhl << 'EOF'
// EJEMPLOS DEVHELPER LANGUAGE - PRIMEROS PASOS

// 1. Crear un proyecto web completo
@proyecto mi_sitio_web

// 2. Crear componentes individuales
@crear html5 formulario_contacto
@crear css3 estilos_personalizados
@crear javascript mi_aplicacion

// 3. Ver snippets disponibles
@snippet html5
@snippet css3
@snippet javascript

// 4. Gestionar archivos
@listar
@editar mi_sitio_web/index.html

// 5. Obtener ayuda
@ayuda
@ejemplo
@version
EOF
mostrar_progreso "Ejemplos creados"

# 10. Probar instalación
echo "🔍 Probando instalación..."
if command -v devhelper > /dev/null 2>&1; then
    mostrar_progreso "Instalación verificada"
else
    echo "⚠️  El comando no está disponible inmediatamente"
    echo "   Ejecuta: source ~/.bashrc"
fi

# MENSAJE FINAL
echo ""
echo "🎉 ¡INSTALACIÓN COMPLETADA EXITOSAMENTE!"
echo "========================================"
echo ""
echo "🚀 PARA COMENZAR:"
echo "   devhelper @ayuda       - Ver sistema de ayuda"
echo "   devhelper @ejemplo     - Ver ejemplos prácticos"
echo "   devhelper @proyecto demo - Crear proyecto demo"
echo ""
echo "💡 CONSEJOS:"
echo "   • Reinicia Termux para mejor compatibilidad"
echo "   • Usa @snippet para ver código reusable"
echo "   • Los archivos .dhl contienen ejemplos"
echo ""
echo "📞 AYUDA:"
echo "   devhelper @permisos    - Verificar instalación"
echo "   devhelper @version     - Información de versión"
echo ""
echo "========================================"
echo "DevHelper Language v2.0 - Code Faster, Create Smarter"
echo ""

# Probar comando inmediatamente
echo "🎯 Probando comando..."
devhelper @version
