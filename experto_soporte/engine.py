from typing import List, Dict, Any
from pydantic import BaseModel, Field

# --- Modelos de Datos del Dominio (HECHOS) ---

class Sintomas(BaseModel):
    """Define los hechos (inputs) que el usuario puede reportar en la interfaz."""
    # Problemas de Aplicación
    app_lenta_o_congela: bool = Field(False)
    app_cierra_inesperadamente: bool = Field(False)
    
    # Problemas de Instalación/Sistema
    instalacion_o_actualizacion_fallida: bool = Field(False)
    pantalla_azul_o_negra_reciente: bool = Field(False)
    
    # Problemas de Hardware/Drivers
    periferico_no_detectado: bool = Field(False)

# --- Motor de Inferencia (Reglas SI... ENTONCES... Avanzadas) ---

def motor_reglas(sintomas: Sintomas) -> Dict[str, Any]:
    """
    Aplica las reglas lógicas y el conocimiento experto para generar un diagnóstico
    y sugerencias de solución.
    """
    recomendaciones: List[str] = []
    
    # 1. Regla de Máxima Prioridad: Fallo Crítico de Drivers/OS (Combinación Grave)
    if sintomas.pantalla_azul_o_negra_reciente or (sintomas.periferico_no_detectado and sintomas.instalacion_o_actualizacion_fallida):
        recomendaciones.append("Diagnóstico CRÍTICO: Corrupción a nivel de sistema operativo o drivers esenciales. La acción debe ser de bajo nivel.")
        recomendaciones.append("Reiniciar en Modo Seguro y verificar la integridad de los archivos del sistema (SFC /scannow).")
        recomendaciones.append("Si no resuelve, intentar desinstalar la última actualización de Windows o restaurar el sistema a un punto previo estable.")
        diagnostico_principal = "RESTAURAR_SISTEMA_O_DRIVERS_CRITICOS"
        
    # 2. Regla de Conflicto de Aplicaciones/Recursos (App + Sistema)
    elif sintomas.app_lenta_o_congela and sintomas.instalacion_o_actualizacion_fallida:
        recomendaciones.append("Diagnóstico: Conflicto de software o falta de recursos tras un cambio reciente. Una librería o driver está causando una disputa.")
        recomendaciones.append("Finalizar procesos innecesarios con el Administrador de Tareas (Ctrl+Shift+Esc).")
        recomendaciones.append("Revertir o desinstalar la última aplicación instalada que coincide con el momento de la falla.")
        diagnostico_principal = "CONFLICTO_DE_SOFTWARE_O_LIBRERIAS"

    # 3. Regla de Instalación Fallida (Problema de Permisos)
    elif sintomas.instalacion_o_actualizacion_fallida:
        recomendaciones.append("Diagnóstico: El proceso de instalación falló, indicando problemas de permisos o requisitos no cumplidos.")
        recomendaciones.append("Intentar la instalación nuevamente ejecutando el archivo como 'Administrador'.")
        recomendaciones.append("Desactivar temporalmente el antivirus o firewall antes de reintentar.")
        diagnostico_principal = "REINTENTAR_COMO_ADMINISTRADOR"
    
    # 4. Regla de Corrupción de Aplicación Específica
    elif sintomas.app_cierra_inesperadamente:
        recomendaciones.append("Diagnóstico: La aplicación está corrupta, obsoleta o tiene un error de memoria específico.")
        recomendaciones.append("Reinstalar la aplicación limpiando el caché (si es posible) y actualizando a la última versión.")
        recomendaciones.append("Verificar si hay otros programas de seguridad que puedan estar interfiriendo.")
        diagnostico_principal = "REINSTALAR_APLICACION_LIMPIANDO_CACHE"
        
    # 5. Regla de Rendimiento o Bloqueo Simple
    elif sintomas.app_lenta_o_congela:
        recomendaciones.append("Diagnóstico: Posible fuga de memoria o sobrecarga temporal de recursos del sistema.")
        recomendaciones.append("Cerrar la aplicación con el Administrador de Tareas o simplemente reiniciarla.")
        diagnostico_principal = "FINALIZAR_TAREA_Y_REINICIAR_APP"
        
    # 6. Regla de Periféricos Desconocidos
    elif sintomas.periferico_no_detectado:
        recomendaciones.append("Diagnóstico: Problema de detección de hardware o falta de drivers.")
        recomendaciones.append("Desconectar y reconectar el periférico en otro puerto USB.")
        recomendaciones.append("Ir al Administrador de Dispositivos y 'Actualizar Controlador' o 'Reinstalar' el dispositivo.")
        diagnostico_principal = "ACTUALIZAR_DRIVER_O_PUERTO"

    else:
        # Regla de respaldo/default
        recomendaciones.append("No se detectaron síntomas específicos. La acción más segura para resolver fallos intermitentes es un reinicio completo del equipo.")
        diagnostico_principal = "REINICIAR_SISTEMA_SIMPLE"

    return {
        "diagnostico_principal": diagnostico_principal,
        "detalles_recomendaciones": recomendaciones,
    }