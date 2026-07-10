from pathlib import Path
import base64, hashlib, json, lzma, sys

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / "artifact_manifest_v2.json").read_text())
parts = sorted((root / "payload").glob("chunk-*.b64"))

if len(parts) != manifest["chunk_count"]:
    print(f"Waiting for all parts: found {len(parts)} of {manifest['chunk_count']}")
    sys.exit(0)

encoded = "".join(p.read_text().strip() for p in parts)
if len(encoded) != manifest["base64_characters"]:
    raise SystemExit("Encoded payload length mismatch")

data = lzma.decompress(base64.b64decode(encoded, validate=True))
sha = hashlib.sha256(data).hexdigest()
if sha != manifest["original_sha256"]:
    raise SystemExit(f"SHA-256 mismatch: {sha}")

out = root / manifest["output_path"]
out.parent.mkdir(parents=True, exist_ok=True)
out.write_bytes(data)
print(f"Reconstructed {out} ({len(data)} bytes, SHA-256 {sha})")
