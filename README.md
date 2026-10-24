# RoadGuard

RoadGuard is a machine-learning-based road deterioration prediction
and maintenance decision-support system.

## Objectives

- Analyse pavement condition and historical road performance.
- Predict future deterioration when longitudinal observations support it.
- Visualise road sections using verified geographic coordinates.
- Support transparent, evidence-based maintenance prioritisation.
- Present results through an interactive dashboard.

## Technology

- Python
- pandas and NumPy
- scikit-learn
- Streamlit
- Plotly and Folium
- Git and GitHub

## Project Structure

- `src/`: data processing, modelling, and application logic
- `tests/`: automated tests
- `data/raw/`: local raw datasets (not committed)
- `data/processed/`: locally generated datasets (not committed)
- `data/sample/`: small approved sample data
- `models/`: locally generated model artefacts (not committed)
- `reports/`: project reports
- `docs/`: technical documentation

## Getting Started

Create and activate a Python virtual environment, then install the
dependencies listed in `requirements.txt`.

Keep the original LTPP dataset outside GitHub. Document the source,
selected tables, data dictionary, and processing steps before modelling.

## Research Integrity

RoadGuard predictions are decision-support outputs, not substitutes
for professional road inspections. Model performance must be evaluated
on held-out data, with leakage avoided.
