# ESG Score Analysis Dashboard | Power BI

> Stakeholder-level Environmental, Social and Governance score comparison for Shirpur.

[![Power BI](https://img.shields.io/badge/Microsoft-Power%20BI-F2C811?logo=powerbi&logoColor=black)](https://powerbi.microsoft.com/)
[![Portfolio Project](https://img.shields.io/badge/Project-Portfolio-blue)](https://github.com/sagar-grv/esg-score-dashboard-powerbi)
[![Verification](https://img.shields.io/badge/Report-Verified-success)](docs/technical-evidence.md)

## Why This Project Exists

Static spreadsheets make it difficult to move from a broad question to the exact segment, department, state or district that explains the result. This report converts that exploration into an interactive Power BI experience with a deliberate analytical sequence.

## Analytical Story

This report follows a **segment-to-community** storyline:

1. **Start with stakeholder voices** — dedicated pages isolate Health Workers, Homemakers, Students, Farmers and Teachers so each group can be reviewed without mixing populations.
2. **Move to the Shirpur view** — the community-level page brings the three ESG dimensions together.
3. **Close with risk context** — the final page places ESG scores beside the overall risk score, enabling a discussion of where sustainability performance may need attention.

The repository deliberately avoids claiming specific numerical conclusions because the original semantic model is remotely connected and the source data was not supplied separately. The evidence below proves the report structure and fields present in the submitted PBIX.

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

- `E Score_HW`
- `S Score_HW`
- `G Score_HW`
- `E Score_HM`
- `S Score_HM`
- `G Score_HM`
- `E Score_Student`
- `S Score_Student`
- `G Score_Student`
- `E Score_Farmer`
- `S Score_Farmer`
- `G Score_Farmer`
- `E Score_Teacher`
- `S Score_Teacher`
- `G Score_Teacher`
- `E Score_Shirpur`
- `S Score_Shirpur`
- `G Score_Shirpur`
- `Overall Risk Score_Shirpur`

## Data Lineage

Power BI Service connected report; the PBIX contains report layout and connection metadata, while refresh may require access to the original remote semantic model.

## Skills Demonstrated

Power BI • ESG analytics • stakeholder segmentation • KPI comparison • risk-score analysis • data storytelling

## Repository Structure

```text
.
├── dashboard/          # Original Power BI PBIX/PBIT artefact
├── docs/               # Narrative, technical proof and quality notes
├── evidence/           # Machine-readable report inventory and checksums
├── screenshots/        # Add exported report-page images here
├── LINKEDIN_POST.md     # Ready-to-edit portfolio post
├── LICENSE
└── README.md
```

## How to Review the Work

1. Download the file from [`dashboard/`](dashboard/ESG_Score_Dashboard.pbix).
2. Open it with Microsoft Power BI Desktop.
3. Review the page sequence described above.
4. Reconnect or refresh the source only when authorised.
5. Compare the file hash with `evidence/SHA256SUMS.txt` to confirm integrity.

## Evidence Limitations

GitHub cannot render `.pbix` or `.pbit` files in the browser. The repository therefore provides structural metadata, hashes, field inventories and source notes as proof. Exported Power BI screenshots can be added later without changing the underlying evidence. Numerical findings are intentionally not fabricated where the original source data is unavailable or remotely connected.

## Author

**Sagar Gurav**  
AI/ML and Data Analytics Student
