# Technical Evidence and Verification

## Verification Method

The Power BI file was treated as a read-only package. Its internal metadata was inspected to verify page names, visual containers, visual types, referenced fields and connection characteristics. The dashboard was not modified during this verification.

## File Integrity

- Repository file: `dashboard/ESG_Score_Dashboard.pbix`
- Size: `299,924` bytes
- SHA-256: `3f2932694ac34e41e18ffa68ab1109d88cbaaa8819654725d4418f8de593ab4c`

Anyone can independently compute the same hash after downloading the file.

## Report Inventory

| Page | Visual count | Visual types |
|---|---:|---|
| ESG Score HW | 1 | `clusteredColumnChart` × 1 |
| ESG Score HM | 1 | `clusteredColumnChart` × 1 |
| ESG Score Student | 1 | `clusteredColumnChart` × 1 |
| ESG Score Farmer | 1 | `clusteredColumnChart` × 1 |
| ESG Score Teacher | 1 | `clusteredColumnChart` × 1 |
| ESG Score Shirpur | 1 | `clusteredColumnChart` × 1 |
| Duplicate of ESG Score Shirpur | 2 | `clusteredColumnChart` × 2 |

**Total:** 7 pages and 8 visual containers.

## Referenced Fields

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

## Data-Lineage Evidence

The PBIX is a Power BI Service-connected report. It contains report layout and connection metadata, while refresh may require access to the original remote semantic model.

## Interpretation Boundary

This document proves what is present in the Power BI artefact. It does not claim that the underlying source is complete, current or suitable for policy decisions. Any public presentation should include the dataset owner, collection method, reporting period and licence.
