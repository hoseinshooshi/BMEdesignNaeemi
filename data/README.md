# ANSUR II datasets

The two public-release ANSUR II working databases are included directly in this directory:

- `ANSUR II MALE Public.csv` — 4,082 participants
- `ANSUR II FEMALE Public.csv` — 1,986 participants

Both files contain the original participant-level anthropometric records and are stored as UTF-8 CSV text for consistent cross-platform loading. The project uses the following measurements for wrist-circumference prediction:

- `handlength`
- `handbreadth`
- `radialestylionlength`
- `forearmcircumferenceflexed`
- Target: `wristcircumference`

Run the machine-learning example from the repository root:

```bash
python examples/train_ansur_ml.py
```

The downloader remains available for refreshing local copies:

```bash
python scripts/download_ansur.py --force
```

## Provenance and limitations

ANSUR II was conducted by the U.S. Army Natick Soldier Research, Development and Engineering Center. The public working databases contain 93 directly measured anthropometric dimensions and were cleared for unlimited public release.

- [U.S. Army Defense Centers for Public Health — ANSUR II database and variable definitions](https://ph.health.mil/topics/workplacehealth/ergo/Pages/Anthropometric-Database.aspx)
- [Penn State OPEN Design Lab — ANSUR II dataset](https://www.openlab.psu.edu/ansur2/)

The sample represents U.S. Army personnel, not the U.S. civilian population or a universal clinical population. Do not use the resulting model for clinical sizing or patient-specific treatment without independent validation.
