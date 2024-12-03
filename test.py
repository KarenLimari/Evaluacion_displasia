import pandas as pd
import numpy as np

num_pacientes = 100

edades_meses = pd.Series(
    np.random.randint(0, 61, size=num_pacientes), name="edad_meses"
)
sexos = pd.Series(
    np.random.choice([0, 1], size=num_pacientes), name="sexo"
)  # 0 = Femenino, 1 = Masculino
angulos_acetabulares = pd.Series(
    np.random.uniform(20, 40, size=num_pacientes), name="angulo_acetabular"
)
cuadrantes = pd.Series(
    np.random.choice(
        ["superomedial", "superolateral", "inferomedial", "inferolateral"],
        size=num_pacientes,
    ),
    name="cuadrante_cabeza_femoral",
)
lineas_shenton = pd.Series(
    np.random.choice(["continua", "discontinua"], size=num_pacientes),
    name="linea_shenton",
)
hospitales = pd.Series(
    np.random.choice(["Hospital A", "Hospital B", "Hospital C"], size=num_pacientes),
    name="hospital",
)

df = pd.concat(
    [edades_meses, sexos, angulos_acetabulares, cuadrantes, lineas_shenton, hospitales],
    axis=1,
)


# Función para evaluar displasia. Este viene del caso de uso anterior, módulo Fundamentos de python.
def evaluar_displasia(row):
    medidas_normales = {
        "acetabular": 30,
        "cuadrante": "inferomedial",
        "shenton": "continua",
    }
    alertas = []

    # Verifica el ángulo acetabular
    if row["angulo_acetabular"] >= medidas_normales["acetabular"]:
        alertas.append(f"Ángulo acetabular elevado ({row['angulo_acetabular']}°).")

    # Verifica la posición de la cabeza femoral en el cuadrante inferomedial
    if row["cuadrante_cabeza_femoral"] != medidas_normales["cuadrante"]:
        alertas.append(
            f"Cabeza femoral fuera del cuadrante correspondiente (actual: {row['cuadrante_cabeza_femoral']})."
        )

    # Evalúa la línea de Shenton
    if row["linea_shenton"] != medidas_normales["shenton"]:
        alertas.append(f"Línea de Shenton alterada (actual: {row['linea_shenton']}).")

    return "Displasia" if alertas else "Normal"


df["diagnostico_displasia"] = df.apply(evaluar_displasia, axis=1)

df.head()
