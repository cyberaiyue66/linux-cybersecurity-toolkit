# Data Directory

This directory contains datasets and sample files used by the project.

## Contents

- `emails.csv`  
  Dataset containing labeled email messages for phishing detection.
  - `text` – email body text
  - `label` – `phishing` or `legit`

- `sample_logs/` (optional)  
  Sample system or authentication logs used for testing security scripts.

## Notes

- Real sensitive data is **not** included in this repository.
- All datasets are either synthetic or publicly available examples.
- This project is designed to work **offline**, which is suitable for restricted network environments.

## Future Improvements
- Add larger and more diverse datasets
- Support multilingual emails (English / Chinese)
- Include automated dataset validation scripts
