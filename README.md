## Zip Verifier CLI

A command-line utility to verify the contents of a ZIP file against a manifest file.

### Installation

```bash
pip install -r requirements.txt
```

### Usage

```bash
zip-verifier-cli /path/to/your/zipfile.zip /path/to/your/manifest.txt
```

The manifest file should contain one file path per line.

Example of a manifest file:
```
file1.txt
file2.txt
```

