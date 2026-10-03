import folium

# 1. Crear el mapa táctico centrado en el Atlántico Sur
mapa = folium.Map(
    location=[-52.5, -63.5], 
    zoom_start=5, 
    tiles="https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png",
    attr="Map data: &copy; OpenStreetMap contributors, SRTM | Map style: &copy; OpenTopoMap (CC-BY-SA)",
    control_scale=True
)

# 2. Lista de etiquetas unificadas para las bases terrestres
puntos_estaticos = [
    {"coordenadas": [-51.68, -57.78], "etiqueta": "MALVINAS (ESTACIÓN UK)"},
    {"coordenadas": [-53.77, -67.74], "etiqueta": "B.A. RÍO GRANDE (ARG)"},
    {"coordenadas": [-51.55, -69.35], "etiqueta": "BASE AÉREA / NAVAL RÍO GALLEGOS (ARG)"},
    {"coordenadas": [-54.81, -68.30], "etiqueta": "BASE AÉREA / NAVAL USHUAIA (KOR/ARG)"}
]

for punto in puntos_estaticos:
    folium.Marker(
        location=punto["coordenadas"],
        icon=folium.DivIcon(
            html=f"""<div style="
                font-family: 'Courier New', Courier, monospace; font-weight: bold; font-size: 9px; 
                color: #fff; background-color: rgba(20, 25, 30, 0.85); padding: 3px 6px; 
                border: 1px solid rgba(255,255,255,0.2); border-radius: 2px; white-space: nowrap;
                box-shadow: 1px 1px 4px rgba(0,0,0,0.5); text-align: center;
            ">{punto['etiqueta']}</div>""",
            icon_size=(140, 18), icon_anchor=(70, 9)
        )
    ).add_to(mapa)

# =========================================================================
# 3. CUADROS DE INVENTARIO EN EL OCÉANO (UK y ARG/TDF)
# =========================================================================
# Cuadro Británico (Rojo)
folium.Marker(
    location=[-49.0, -58.5], 
    icon=folium.DivIcon(
        html="""<div style="
            font-family: 'Courier New', Courier, monospace; font-size: 10px; color: #fff; 
            background-color: rgba(20, 25, 30, 0.90); padding: 8px 12px; border: 1px solid #d9534f;
            border-radius: 4px; width: 440px; box-shadow: 2px 2px 6px rgba(0,0,0,0.6); line-height: 1.4;
        ">
            <b style="color: #d9534f; font-size: 11px; font-family: 'Arial Black', sans-serif;">CARRIER STRIKE GROUP (UK)</b><br>
            <span style="color: #ffaa66; font-size: 8.5px; font-weight: bold;">[AIR EMBARKED - HMS QUEEN ELIZABETH GROUP]</span><br>
            • <span id="txt-cazas-uk" style="color:#ffaa66; font-weight:bold;">18</span> Cazas Furtivos 5.ª Gen (F-35B Lightning II)<br>
            • 6 Helis Crowsnest AEW&C | <span id="txt-helis-uk" style="color:#ffaa66; font-weight:bold;">14</span> Helis Merlin/Wildcat ASW<br>
            <span style="color: #ffaa66; font-size: 8.5px; font-weight: bold;">[SURFACE FLOTA DE ESCOLTAS]</span><br>
            • <span id="txt-dest-uk" style="color:#ffaa66; font-weight:bold;">3</span> Destructores Antiaéreos Tipo 45 | 1 Fragata Tipo 26<br>
            • <span id="txt-frag-uk" style="color:#ffaa66; font-weight:bold;">2</span> Fragatas Tipo 23 | 11 Helicópteros Chinook<br>
            <span style="color: #ffaa66; font-size: 8.5px; font-weight: bold;">[SUB-SURFACE & LOGISTICS]</span><br>
            • <span id="txt-sub-uk" style="color:#ffaa66; font-weight:bold;">2</span> Submarinos Nucleares de Ataque Clase Astute<br>
            • <span id="txt-log-uk" style="color:#ffaa66; font-weight:bold;">2</span> Buques Tanque de Reabastecimiento (Clase Tide)
        </div>""",
        icon_size=(460, 140), icon_anchor=(230, 70)
    )
).add_to(mapa)

# Cuadro Argentino (Azul)
folium.Marker(
    location=[-54.5, -55.0], 
    icon=folium.DivIcon(
        html="""<div style="
            font-family: 'Courier New', Courier, monospace; font-size: 10px; color: #fff; 
            background-color: rgba(20, 25, 30, 0.90); padding: 8px 12px; border: 1px solid #337ab7;
            border-radius: 4px; width: 440px; box-shadow: 2px 2px 6px rgba(0,0,0,0.6); line-height: 1.4;
        ">
            <b style="color: #337ab7; font-size: 11px; font-family: 'Arial Black', sans-serif;">FLOTA DE MAR ARGENTINA (ARA)</b><br>
            <span style="color: #66ccff; font-size: 8.5px; font-weight: bold;">[FUERZA DE SUPERFICIE ESCENARIO NUEVA GEN]</span><br>
            • <span id="txt-cazas-arg" style="color:#66ccff; font-weight:bold;">50</span> Cazas de Combate Operativos (F-16 / FA-50)<br>
            • <span id="txt-dw-arg" style="color:#66ccff; font-weight:bold;">1</span> Fragata Pesada Tecnológica Clase DW3000F (TDF)<br>
            • <span id="txt-meko-arg" style="color:#66ccff; font-weight:bold;">2</span> Fragatas Clase MEKO A200 (ARA)<br>
            • <span id="txt-hdc-arg" style="color:#66ccff; font-weight:bold;">4</span> Corbetas de Ataque Rápido Clase HDC-2200 (TDF)<br>
            <span style="color: #66ccff; font-size: 8.5px; font-weight: bold;">[LOGÍSTICA PESADA Y PROYECCIÓN]</span><br>
            • <span id="txt-soy-arg" style="color:#66ccff; font-weight:bold;">2</span> Buques de Combate Clase Soyang AOE-II (TDF)<br>
            • <span id="txt-lst-arg" style="color:#66ccff; font-weight:bold;">1</span> Buque de Desembarco de Tanques Clase LST-II (TDF)<br>
            <span style="color: #66ccff; font-size: 8.5px; font-weight: bold;">[COMPONENTE SUBSUPERFICIAL OPERATIVO]</span><br>
            • <span id="txt-sub-arg" style="color:#66ccff; font-weight:bold;">3</span> Submarinos de Ataque Diésel-Eléctricos Clase 209 (ARA)<br>
            • Patrulleros Oceánicos Clase Gowind (OPV 87 - ARA)
        </div>""",
        icon_size=(460, 140), icon_anchor=(230, 70)
    )
).add_to(mapa)

# =========================================================================
# 4. INTERFAZ INTERACTIVA COMPLETA (Con modificador simple de Helis ASW)
# =========================================================================
interfaz_dinamica_html = """
<div class="tactical-status-bar">
    <div class="status-item">
        <span class="status-title">🦅 CAPACIDAD AÉREA:</span>
        <div class="power-bar-container">
            <div id="bar-aerea-uk" class="power-bar uk-bar" style="width: 47%;">🇬🇧 UK 47%</div>
            <div id="bar-aerea-arg" class="power-bar arg-bar" style="width: 53%;">53% ARG/TDF</div>
        </div>
    </div>
    <div class="status-item">
        <span class="status-title">⚓ CAPACIDAD NAVAL:</span>
        <div class="power-bar-container">
            <div id="bar-naval-uk" class="power-bar uk-bar" style="width: 44%;">🇬🇧 UK 44%</div>
            <div id="bar-naval-arg" class="power-bar arg-bar" style="width: 56%;">56% ARG/TDF</div>
        </div>
    </div>
    <div class="status-item">
        <span class="status-title">🌊 CAPACIDAD SUBMARINA / ASW:</span>
        <div class="power-bar-container">
            <div id="bar-sub-uk" class="power-bar uk-bar" style="width: 64%;">🇬🇧 UK 64%</div>
            <div id="bar-sub-arg" class="power-bar arg-bar" style="width: 36%;">36% ARA</div>
        </div>
    </div>
</div>

<div class="reinforcement-panel">
    <div class="panel-header">🕹️ CONFIGURADOR DE FLOTAS</div>
    
    <div class="faction-box blue-faction">
        <h4>ARGENTINA / TDF</h4>
        <div class="control-row"><span>Cazas Totales:</span><input type="number" id="inp-cazas-arg" value="50" min="0" max="99" oninput="actualizarSimulador()"></div>
        <div class="control-row"><span>Frag. DW3000F:</span><input type="number" id="inp-dw-arg" value="1" min="0" max="10" oninput="actualizarSimulador()"></div>
        <div class="control-row"><span>Frag. MEKO A200:</span><input type="number" id="inp-meko-arg" value="2" min="0" max="10" oninput="actualizarSimulador()"></div>
        <div class="control-row"><span>Corv. HDC-2200:</span><input type="number" id="inp-hdc-arg" value="4" min="0" max="20" oninput="actualizarSimulador()"></div>
        <div class="control-row"><span>Log. Soyang:</span><input type="number" id="inp-soy-arg" value="2" min="0" max="10" oninput="actualizarSimulador()"></div>
        <div class="control-row"><span>Anfibio LST-II:</span><input type="number" id="inp-lst-arg" value="1" min="0" max="5" oninput="actualizarSimulador()"></div>
        <div class="control-row"><span>Sub. Clase 209:</span><input type="number" id="inp-sub-arg" value="3" min="0" max="10" oninput="actualizarSimulador()"></div>
    </div>

    <div class="faction-box red-faction">
        <h4>REINO UNIDO (UK)</h4>
        <div class="control-row"><span>Cazas F-35B:</span><input type="number" id="inp-cazas-uk" value="18" min="0" max="99" oninput="actualizarSimulador()"></div>
        <div class="control-row"><span>Helis ASW UK:</span><input type="number" id="inp-helis-uk" value="14" min="0" max="30" oninput="actualizarSimulador()"></div>
        <div class="control-row"><span>Dest. Tipo 45:</span><input type="number" id="inp-dest-uk" value="3" min="0" max="12" oninput="actualizarSimulador()"></div>
        <div class="control-row"><span>Frag. Tipo 23:</span><input type="number" id="inp-frag-uk" value="2" min="0" max="12" oninput="actualizarSimulador()"></div>
        <div class="control-row"><span>Sub. Nucleares:</span><input type="number" id="inp-sub-uk" value="2" min="0" max="8" oninput="actualizarSimulador()"></div>
        <div class="control-row"><span>Log. Clase Tide:</span><input type="number" id="inp-log-uk" value="2" min="0" max="6" oninput="actualizarSimulador()"></div>
    </div>
</div>

<style>
    .tactical-status-bar {
        position: absolute; top: 10px; left: 5%; width: 90%; height: auto;
        background-color: rgba(15, 20, 25, 0.90); border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 4px; padding: 8px 15px; box-sizing: border-box; z-index: 1000;
        display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.5);
    }
    .status-item { flex: 1; min-width: 250px; margin: 4px 10px; display: flex; flex-direction: column; }
    .status-title { font-family: 'Courier New', Courier, monospace; font-weight: bold; font-size: 10px; color: #ddd; margin-bottom: 4px; }
    .power-bar-container { width: 100%; height: 16px; background-color: #333; border-radius: 2px; overflow: hidden; display: flex; border: 1px solid rgba(255,255,255,0.1); }
    .power-bar { height: 100%; display: flex; align-items: center; justify-content: center; font-family: Arial, sans-serif; font-size: 8.5px; font-weight: bold; color: white; text-shadow: 1px 1px 2px black; transition: all 0.3s ease-in-out; }
    .uk-bar { background: linear-gradient(90deg, #8b2522, #d9534f); }
    .arg-bar { background: linear-gradient(90deg, #24527a, #337ab7); text-align: right; }

    /* Estilos panel numérico izquierdo */
    .reinforcement-panel {
        position: absolute; top: 110px; left: 10px; width: 230px;
        background-color: rgba(20, 25, 30, 0.94); border: 1px solid rgba(255,255,255,0.15);
        border-radius: 4px; padding: 10px; z-index: 1000; color: #fff;
        font-family: 'Courier New', Courier, monospace; box-shadow: 3px 3px 10px rgba(0,0,0,0.6);
    }
    .panel-header { font-size: 11px; font-weight: bold; border-bottom: 1px solid rgba(255,255,255,0.2); padding-bottom: 5px; margin-bottom: 8px; color: #ffaa66; text-align: center; }
    .faction-box { background-color: rgba(255,255,255,0.03); padding: 6px; border-radius: 3px; margin-bottom: 8px; border-left: 3px solid #fff; }
    .blue-faction { border-left-color: #337ab7; }
    .red-faction { border-left-color: #d9534f; }
    .faction-box h4 { margin: 0 0 6px 0; font-size: 10px; font-weight: bold; letter-spacing: 0.5px; }
    .control-row { display: flex; justify-content: space-between; align-items: center; font-size: 9.5px; margin-bottom: 4px; color: #ccc; }
    .control-row input { width: 45px; background: #111; border: 1px solid #444; color: #fff; border-radius: 3px; text-align: center; font-size: 10px; font-weight: bold; padding: 1px 0; }
    .control-row input:focus { border-color: #ffaa66; outline: none; }
</style>

<script>
function actualizarSimulador() {
    let czArg = parseInt(document.getElementById('inp-cazas-arg').value) || 0;
    let dwArg = parseInt(document.getElementById('inp-dw-arg').value) || 0;
    let mkArg = parseInt(document.getElementById('inp-meko-arg').value) || 0;
    let hdArg = parseInt(document.getElementById('inp-hdc-arg').value) || 0;
    let syArg = parseInt(document.getElementById('inp-soy-arg').value) || 0;
    let lsArg = parseInt(document.getElementById('inp-lst-arg').value) || 0;
    let sbArg = parseInt(document.getElementById('inp-sub-arg').value) || 0;

    let czUk = parseInt(document.getElementById('inp-cazas-uk').value) || 0;
    let hlUk = parseInt(document.getElementById('inp-helis-uk').value) || 0;
    let dtUk = parseInt(document.getElementById('inp-dest-uk').value) || 0;
    let frUk = parseInt(document.getElementById('inp-frag-uk').value) || 0;
    let sbUk = parseInt(document.getElementById('inp-sub-uk').value) || 0;
    let lgUk = parseInt(document.getElementById('inp-log-uk').value) || 0;

    document.getElementById('txt-cazas-uk').innerText = czUk;
    document.getElementById('txt-helis-uk').innerText = hlUk;
    document.getElementById('txt-dest-uk').innerText = dtUk;
    document.getElementById('txt-frag-uk').innerText = frUk;
    document.getElementById('txt-sub-uk').innerText = sbUk;
    document.getElementById('txt-log-uk').innerText = lgUk;

    document.getElementById('txt-cazas-arg').innerText = czArg;
    document.getElementById('txt-dw-arg').innerText = dwArg;
    document.getElementById('txt-meko-arg').innerText = mkArg;
    document.getElementById('txt-hdc-arg').innerText = hdArg;
    document.getElementById('txt-soy-arg').innerText = syArg;
    document.getElementById('txt-lst-arg').innerText = lsArg;
    document.getElementById('txt-sub-arg').innerText = sbArg;

    // CÁLCULO VECTOR AÉREO
    let ptsAeroUk = czUk * 2.5;
    let ptsAeroArg = czArg * 1.0;
    let totalAero = ptsAeroUk + ptsAeroArg;
    let pctAeroUk = totalAero > 0 ? Math.round((ptsAeroUk / totalAero) * 100) : 50;
    let pctAeroArg = 100 - pctAeroUk;

    // CÁLCULO VECTOR NAVAL
    let ptsNavUk = (dtUk * 4.0) + (frUk * 3.0) + 3.5 + (lgUk * 1.0);
    let ptsNavArg = (dwArg * 4.2) + (mkArg * 3.0) + (hdArg * 1.5) + (syArg * 1.0) + (lsArg * 1.0);
    let totalNav = ptsNavUk + ptsNavArg;
    let pctNavUk = totalNav > 0 ? Math.round((ptsNavUk / totalNav) * 100) : 50;
    let pctNavArg = 100 - pctNavUk;

    // CÁLCULO VECTOR SUBMARINO / ASW (Se añaden los helicópteros de caza)
    let ptsSubUk = (sbUk * 4.0) + (hlUk * 0.8);
    let ptsSubArg = sbArg * 1.5;
    let totalSub = ptsSubUk + ptsSubArg;
    let pctSubUk = totalSub > 0 ? Math.round((ptsSubUk / totalSub) * 100) : 50;
    let pctSubArg = 100 - pctSubUk;

    pctAeroUk = Math.max(10, Math.min(90, pctAeroUk)); pctAeroArg = 100 - pctAeroUk;
    pctNavUk = Math.max(10, Math.min(90, pctNavUk)); pctNavArg = 100 - pctNavUk;
    pctSubUk = Math.max(10, Math.min(90, pctSubUk)); pctSubArg = 100 - pctSubUk;

    document.getElementById('bar-aerea-uk').style.width = pctAeroUk + '%';
    document.getElementById('bar-aerea-uk').innerText = '🇬🇧 UK ' + pctAeroUk + '%';
    document.getElementById('bar-aerea-arg').style.width = pctAeroArg + '%';
    document.getElementById('bar-aerea-arg').innerText = pctAeroArg + '% ARG/TDF';

    document.getElementById('bar-naval-uk').style.width = pctNavUk + '%';
    document.getElementById('bar-naval-uk').innerText = '🇬🇧 UK ' + pctNavUk + '%';
    document.getElementById('bar-naval-arg').style.width = pctNavArg + '%';
    document.getElementById('bar-naval-arg').innerText = pctNavArg + '% ARG/TDF';

    document.getElementById('bar-sub-uk').style.width = pctSubUk + '%';
    document.getElementById('bar-sub-uk').innerText = '🇬🇧 UK ' + pctSubUk + '%';
    document.getElementById('bar-sub-arg').style.width = pctSubArg + '%';
    document.getElementById('bar-sub-arg').innerText = pctSubArg + '% ARA';
}
</script>
"""
# =========================================================================
# 5. INYECCIÓN DE LA INTERFAZ Y GENERACIÓN DEL ARCHIVO HTML
# =========================================================================

# ESTA ES LA LÍNEA QUE TE FALTA (Va acá para unir todo antes de guardar) [1]
mapa.get_root().html.add_child(folium.Element(interfaz_dinamica_html))

# 6. Guardar el mapa final unificado [1]
mapa.save("mapa_atlantico_sur.html")

print("¡Simulador interactivo avanzado completado! Podés cambiar los números libremente en el panel.")
