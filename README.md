[![Gitter](https://badges.gitter.im/TrustSource/community.svg)](https://gitter.im/TrustSource/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

# TrustSource SPDX import


# Installation

Install from PyPI

```
pip install ts-spdx-import 
```

# Usage

## Help

```
ts-spdx-import --help

Usage: ts-spdx-import [OPTIONS] PATH

Options:
  --apiKey TEXT        API Key.
  --projectName TEXT   Project name.
  --skipTransfer       Skip transfer of results to the application.
  --settingsFile TEXT  Path to a settings file.
  --outputFile TEXT    Path to an output file.
  --help               Show this message and exit. 
```

## Prepare data without transfering 

```
ts-spdx-import --skipTransfer <path to an SPDX file> 
```

## Prepare data and transfer to the TrustSource application  

```
ts-spdx-import --apiKey <KEY> --projectName <NAME> <path to an SPDX file> 
```

# Questions & Support
Please see our [support offering](https://www.trustsource.io/support) or checkout the [knowledgebase](https://support.trustsource.io) for more information.
