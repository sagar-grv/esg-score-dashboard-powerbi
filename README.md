# ESG Score Analysis Dashboard | Power BI

> Stakeholder-level Environmental, Social and Governance score comparison for Shirpur.

[![Power BI](https://img.shields.io/badge/Microsoft-Power%20BI-F2C811?logo=powerbi&logoColor=black)](https://powerbi.microsoft.com/)
[![Portfolio Project](https://img.shields.io/badge/Project-Portfolio-blue)](https://github.com/sagar-grv/esg-score-dashboard-powerbi)
[![Verification](https://img.shields.io/badge/Report-Verified-success)](docs/technical-evidence.md)

## Why This Project Exists

Static spreadsheets make it difficult to move from a broad sustainability question to the stakeholder group that explains the result. This report turns that comparison into an interactive Power BI experience with a deliberate analytical sequence.

## Analytical Story

This report follows a **stakeholder-to-community** storyline:

1. **Start with stakeholder voices** — dedicated pages isolate Health Workers, Homemakers, Students, Farmers and Teachers so each group can be reviewed without mixing populations.
2. **Move to the Shirpur view** — the community-level page brings the three ESG dimensions together.
3. **Close with risk context** — the final page places ESG scores beside the overall risk score, enabling a discussion of where sustainability performance may need attention.

The repository deliberately avoids claiming specific numerical conclusions because the original semantic model is remotely connected and the source data was not supplied separately.

## Verified Project Evidence

The supplied Power BI artefact was inspected in read-only mode by parsing its internal `Report/Layout` metadata. This verifies the project structure independently of screenshots.

| Evidence | Verified value |
|---|---:|
| Power BI pages | **7** |
| Visual containers | **8** |
| Dashboard file size | **299,924 bytes** |
| SHA-256 | `3f2932694ac34e41e18ffa68ab1109d88cbaaa8819654725d4418f8de593ab4c` |

### Page and Visual Inventory

| Report page | Visuals | Verified visual types |
|---|---:|---|
| ESG Score HW | 1 | `clusteredColumnChart` × 1 |
| ESG Score HM | 1 | `clusteredColumnChart` × 1 |
| ESG Score Student | 1 | `clusteredColumnChart` × 1 |
| ESG Score Farmer | 1 | `clusteredColumnChart` × 1 |
| ESG Score Teacher | 1 | `clusteredColumnChart` × 1 |
| ESG Score Shirpur | 1 | `clusteredColumnChart` × 1 |
| Duplicate of ESG Score Shirpur | 2 | `clusteredColumnChart` × 2 |

Full proof is available in [`docs/technical-evidence.md`](docs/technical-evidence.md) and the machine-readable [`evidence/report-inventory.json`](evidence/report-inventory.json).

## Data Fields Referenced by the Report

- Environmental, Social and Governance score fields for Health Workers, Homemakers, Students, Farmers and Teachers
- Shirpur-level Environmental, Social and Governance score fields
- `Overall Risk Score_Shirpur`

The complete field inventory is recorded in the technical evidence document.

## Data Lineage

The PBIX is connected to a Power BI Service semantic model. It contains report layout and connection metadata, while refreshing or editing the underlying model may require authorised access to the original remote source.

## Dashboard Artefact Status

The original PBIX is **not currently committed to this repository**. The connected GitHub interface did not preserve large binary payloads byte-for-byte, so no corrupted dashboard was published.

The report structure, referenced fields, file size and SHA-256 checksum were verified from the original local PBIX. To add the source file safely, follow [`dashboard/README.md`](dashboard/README.md) and confirm that the uploaded file matches the published checksum.

## Skills Demonstrated

Power BI • ESG analytics • stakeholder segmentation • KPI comparison • risk-score analysis • data storytelling

## Repository Structure

```text
.
├── dashboard/          # Manual PBIX upload target and integrity instructions
├── docs/               # Narrative, technical proof and quality notes
├── evidence/           # Machine-readable report inventory and checksum
├── screenshots/        # Add validated report-page images here
├── LINKEDIN_POST.md     # Ready-to-edit portfolio post
├── LICENSE
└── README.md
```

## How to Review the Work

1. Read the verified report inventory in [`docs/technical-evidence.md`](docs/technical-evidence.md).
2. Review the checksum in [`evidence/SHA256SUMS.txt`](evidence/SHA256SUMS.txt).
3. Follow [`dashboard/README.md`](dashboard/README.md) to upload or verify `ESG_Score_Dashboard.pbix`.
4. Open the validated PBIX using Microsoft Power BI Desktop.
5. Review the stakeholder-to-community sequence described above.
6. Reconnect or refresh the semantic model only when authorised.

## Evidence Limitations

GitHub cannot render `.pbix` files in the browser. This repository therefore separates **verified structural evidence** from screenshots and numerical interpretation. Numerical findings are intentionally not fabricated where the source rows are unavailable or the report depends on a remote semantic model.

## Author

**Sagar Gurav**  
AI/ML and Data Analytics Student
