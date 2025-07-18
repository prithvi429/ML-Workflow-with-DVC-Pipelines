# ML-Workflow-with-DVC-Pipelines
A reproducible ML pipeline using DVC to track data, code, and model stages. Includes steps like preprocessing, training, and evaluation with version control for all components using Git and DVC.

## Project Overview
This project demonstrates a complete machine learning workflow for chicken disease detection using image data. The workflow is modular, reproducible, and version-controlled using DVC and Git.

## Workflow Steps
1. **Data Ingestion**: Collect and organize chicken fecal images into labeled folders (Coccidiosis, Healthy).
2. **Preprocessing**: Prepare and clean the data for modeling.
3. **Model Building**: Define and configure the base model using parameters from YAML files.
4. **Training**: Train the model on the processed data.
5. **Evaluation**: Assess model performance and log results.

## Tools Used
- **DVC**: For tracking datasets, models, and pipeline stages.
- **Git**: For source code and pipeline version control.
- **Python**: For all scripts and notebooks.

## Folder Structure
- `artifacts/`: Stores data and model artifacts.
- `config/`: Contains configuration files.
- `logs/`: Stores log files.
- `research/`: Jupyter notebooks for experimentation.
- `src/`: Source code for pipeline components.
- `templates/`: HTML templates (if any).

## How to Run
1. Clone the repository.
2. Install dependencies from `requirements.txt`.
3. Use DVC commands to reproduce pipeline stages.
4. Run notebooks in the `research/` folder for experiments.

## Version Control
All data, code, and models are tracked using DVC and Git for full reproducibility.
