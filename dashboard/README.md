# Dashboard Source File

Upload the original Power BI file to this folder with the exact name:

```text
ESG_Score_Dashboard.pbix
```

## Verified Integrity Values

- Expected size: `299924` bytes
- Expected SHA-256: `3f2932694ac34e41e18ffa68ab1109d88cbaaa8819654725d4418f8de593ab4c`

## Safe Manual Upload

1. Download and extract the prepared ESG project package from the ChatGPT conversation.
2. Open this repository on GitHub.
3. Select **Add file → Upload files**.
4. Upload only `ESG_Score_Dashboard.pbix` into the `dashboard` folder.
5. Commit the file to `main`.
6. Verify the local file before upload:

```powershell
Get-FileHash .\ESG_Score_Dashboard.pbix -Algorithm SHA256
```

The reported hash must match the expected value above. Do not publish a different file under the same filename.

## Source Connection Note

The report uses a remotely connected Power BI semantic model. Opening or refreshing it may require authorised access to the original Power BI Service workspace and dataset.
