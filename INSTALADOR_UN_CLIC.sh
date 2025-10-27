#!/bin/bash
# DEVHELPER LANGUAGE - INSTALADOR CORREGIDO

echo ""
echo "🚀 INICIANDO INSTALACIÓN DEVHELPER LANGUAGE..."
echo "=============================================="
echo "No necesitas escribir comandos, todo es automático"
echo ""

# Función para mostrar progreso
mostrar_progreso() {
    echo "✅ $1"
}

# 1. Verificar Termux
echo "🔍 Verificando entorno..."
if [ ! -d "/data/data/com.termux/files/home" ]; then
    echo "❌ Este instalador es solo para Termux"
    exit 1
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
mostrar_progreso "Comando 'devhelper' creado"

# 7. Configurar PATH
echo "🔧 Configurando variables..."
if ! grep -q 'export PATH="$HOME/bin:$PATH"' ~/.bashrc; then
    echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
fi

# Cargar PATH inmediatamente
export PATH="$HOME/bin:$PATH"
mostrar_progreso "Variables configuradas"

# 8. Probar instalación
echo "🔍 Probando instalación..."
if command -v devhelper > /dev/null 2>&1; then
    mostrar_progreso "Instalación verificada"
else
    echo "⚠️ El comando no está disponible inmediatamente"
    echo "Ejecuta: source ~/.bashrc"
fi

# MENSAJE FINAL
echo ""
echo "🎉 ¡INSTALACIÓN COMPLETADA EXITOSAMENTE!"
echo "========================================"
echo ""
echo "🚀 PARA COMENZAR:"
echo "devhelper @ayuda       - Ver sistema de ayuda"
echo "devhelper @ejemplo     - Ver ejemplos prácticos"
echo "devhelper @proyecto demo - Crear proyecto demo"
echo ""
echo "💡 CONSEJOS:"
echo "Reinicia Termux para mejor compatibilidad"
echo "========================================"

# Probar comando inmediatamente
echo "🎯 Probando comando..."
devhelper @version
