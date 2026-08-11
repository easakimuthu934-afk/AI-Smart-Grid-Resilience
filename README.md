# AI Smart Grid Resilience

## Project
Smart Grid Anomaly Detection Prototype

## SIH Problem Statement
SIH31 – AI-Driven Smart Grid Resilience

## Objective
This project is a basic software prototype for monitoring smart-grid parameters and detecting abnormal voltage and temperature conditions.

## Technologies Used
- Python
- CSV
- Basic data analysis
- Rule-based anomaly detection

## How It Works
1. The program reads voltage, current and temperature values from `sample_data.csv`.
2. It checks the values against simple predefined limits.
3. It displays an alert when an abnormal condition is detected.
4. Otherwise, it reports that the grid condition is normal.

## Run the Project
Make sure Python is installed, then run:

```bash
python smart_grid.py
```

## Files
- `smart_grid.py` – Main Python program
- `sample_data.csv` – Sample smart-grid data
- `README.md` – Project documentation

## Future Enhancements
- Machine-learning based anomaly detection
- Real-time sensor data
- Database integration
- Web dashboard
- Fault prediction
- Cloud deployment

## Note
This is an initial prototype for academic/SIH project development. It is not intended for direct control of a real electrical grid.
