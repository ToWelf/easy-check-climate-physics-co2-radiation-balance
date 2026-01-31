# Quick Start Guide

## 1. Install Dependencies

```bash
pip install -r requirements.txt
```

## 2. Launch Jupyter Notebook

```bash
jupyter notebook
```

## 3. Open the Notebook

In your browser, click on `climate_physics_model.ipynb`

## 4. Run the Notebook

- **Option A**: Run all cells at once
  - Click `Cell` → `Run All`
  
- **Option B**: Step through cells one by one
  - Click in a cell and press `Shift + Enter`

## 5. Verify Calculations (Optional)

To verify the scientific accuracy of calculations:

```bash
python verify_calculations.py
```

## What You'll See

The notebook generates comprehensive visualizations showing:

1. **CO2 Trends**: 51% increase from pre-industrial times (278 → 421 ppm)
2. **Carbon Budget**: Where emitted CO2 goes (atmosphere, ocean, land)
3. **Ocean Acidification**: 48% increase in H+ ions (pH 8.25 → 8.08)
4. **Radiation Balance**: Solar input vs. terrestrial output
5. **Greenhouse Effect**: Natural +33°C warming explained
6. **Radiative Forcing**: +2.22 W/m² energy imbalance from CO2
7. **Temperature Response**: 1.7°C expected warming, 1.2°C observed
8. **Future Scenarios**: Projected warming at different CO2 levels

## Expected Runtime

- Complete notebook execution: ~10-15 seconds
- Individual cells: < 1 second each

## Troubleshooting

### Matplotlib plots not showing
- Make sure `%matplotlib inline` is executed in the first code cell
- Restart kernel and run all cells again

### Import errors
- Ensure all packages in `requirements.txt` are installed
- Try: `pip install --upgrade -r requirements.txt`

### Jupyter not found
- Install Jupyter: `pip install jupyter notebook`
- Or use JupyterLab: `pip install jupyterlab` then `jupyter lab`

## Learn More

Read the full README.md for:
- Detailed scientific background
- Data sources and references
- Educational use cases
- Contributing guidelines
