#!/bin/bash
# DEVHELPER LANGUAGE - INSTALADOR OFICIAL DE UN CLIC

echo ""
echo "🚀 INICIANDO INSTALACIÓN DEVHELPER LANGUAGE..."
echo "=============================================="
echo "No necesitas escribir comandos, todo es automático"
echo ""

mostrar_progreso() {
    echo "✅ $1"
}

# 1. Verificar Termux
echo "🔍 Verificando entorno..."
if [ ! -d "/data/data/com.termux/files/home" ]; then
    echo "❌ Este instalador es solo para Termux"
    exit 1
fi

# 2. Actualizar sistema
echo "🔄 Actualizando sistema..."
pkg update -y > /dev/null 2>&1 
pkg upgrade -y > /dev/null 2>&1
echo "✅ Sistema actualizado"

# 3. Instalar Python
echo "🐍 Instalando Python..."
pkg install -y python > /dev/null 2>&1
echo "✅ Python instalado"

# 4. Crear directorios
echo "📁 Creando estructura..."
mkdir -p ~/bin ~/.devhelper ~/.devhelper/ejemplos
echo "✅ Directorios creados"

# 5. Copiar archivo principal
echo "📦 Instalando DevHelper Language..."
if [ -f "src/devhelper.py" ]; then
    cp src/devhelper.py ~/.devhelper/
    echo "✅ Archivos copiados"
else
    echo "❌ No se encontró src/devhelper.py"
    exit 1
fi

# 6. Crear comando ejecutable
echo "⚙️ Configurando comando 'devhelper'..."
cat > ~/bin/devhelper << 'EOF'
#!/bin/bash
python ~/.devhelper/devhelper.py "$@"
EOF

chmod +x ~/bin/devhelper
echo "✅ Comando 'devhelper' creado"

# 7. Configurar PATH
echo "🔧 Configurando variables..."
if ! grep -q 'export PATH="$HOME/bin:$PATH"' ~/.bashrc; then
    echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
fi

export PATH="$HOME/bin:$PATH"
echo "✅ Variables configuradas"

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
echo "✅ Configuración guardada"

# 9. Probar instalación
echo "🔍 Probando instalación..."
if command -v devhelper > /dev/null 2>&1; then
    echo "✅ Instalación verificada"
else
    echo "⚠️ Ejecuta: source ~/.bashrc"
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
echo "💡 CONSEJO: Reinicia Termux o ejecuta: source ~/.bashrc"
echo "========================================"

# Probar comando
echo "🎯 Probando comando..."
devhelper @version
