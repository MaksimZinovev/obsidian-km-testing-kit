Files, paths
- File name: valid filename, filenames with reserved special characters (space * ? / \ | < > , . ( ) [ ] { } ; : ‘ “ ! @ # $ % ^ &), short filename, long filename (>255 chars), short filename (<3 chars)
- File kind: valid file kind, invalid file kind (not supported)
- File size: empty (no data), small, medium, large, extra large
- Validation messages: various actions, e.g. when unsupported file is uploaded, when supported file is uploaded
- State and attribute: Write-Protected,  Unavailable,  Locked, On Remote Machine, Corrupted, With virus, Non-Existent, Already Exists
- Available space: No Space,  Minimal Space
- File security security: clicking on link with JS should block popups and redirects (Reference: [link](https://portswigger.net/research/portable-data-exfiltration) , [github-pdf-samples-injection](https://github.com/PortSwigger/portable-data-exfiltration/tree/main/PDF-research-samples))
- File upload: upload multiple files when only one file per-upload is supported.