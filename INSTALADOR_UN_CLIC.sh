#!/bin/bash
echo ""
echo "DEVHELPER LANGUAGE - INSTALADOR"
echo "================================"
echo "Instalacion automatica en progreso..."
echo ""

echo "Verificando Termux..."
if [ ! -d "/data/data/com.termux/files/home" ]; then
    echo "ERROR: Solo para Termux"
    exit 1
fi

echo "Actualizando sistema..."
pkg update -y > /dev/null 2>&1 
pkg upgrade -y > /dev/null 2>&1
echo "OK - Sistema actualizado"

echo "Instalando Python..."
pkg install -y python > /dev/null 2>&1
echo "OK - Python instalado"

echo "Creando directorios..."
mkdir -p ~/bin ~/.devhelper
echo "OK - Directorios creados"

echo "Copiando archivos..."
if [ -f "src/devhelper.py" ]; then
    cp src/devhelper.py ~/.devhelper/
    echo "OK - Archivos copiados"
else
    echo "ERROR: No se encontro src/devhelper.py"
    exit 1
fi

echo "Configurando comando..."
cat > ~/bin/devhelper << 'EOF'
#!/bin/bash
python ~/.devhelper/devhelper.py "$@"
EOF

chmod +x ~/bin/devhelper
echo "OK - Comando configurado"

echo "Configurando variables..."
if ! grep -q 'export PATH="$HOME/bin:$PATH"' ~/.bashrc; then
    echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
fi

export PATH="$HOME/bin:$PATH"
echo "OK - Variables configuradas"

echo "Probando instalacion..."
if command -v devhelper > /dev/null 2>&1; then
    echo "OK - Instalacion verificada"
else
    echo "INFO: Ejecuta 'source ~/.bashrc'"
fi

echo ""
echo "INSTALACION COMPLETADA"
echo "======================"
echo "Usa: devhelper @ayuda"
echo "Usa: devhelper @proyecto demo"
echo ""

devhelper @version
