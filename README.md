# TrustSource SPDX import

> [!WARNING]
> **PLEASE NOTE:** We stopped further development on this tool. You may still use it, but it will not supported anymore as such. Starting Q4/2024 we decided to focus all efforts on developing [ts-scan](https://github.com/trustsource/ts-scan), which also covers all capabilities of this solution. 


# Installation

- Clone repository
```shell
git clone https://github.com/TrustSource/ts-spdx-upload.git
```

- Install using PIP from the local directory
```shell
pip3 install ./ts-spdx-upload 
```

# Usage

## Help

```shell
ts-spdx-import --help
```
```shell
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

```shell
ts-spdx-import --skipTransfer <path to an SPDX file> 
```

## Prepare data and transfer to the TrustSource application  

```shell
ts-spdx-import --apiKey <KEY> --projectName <NAME> <path to an SPDX file> 
```

# Questions & Support
Please see our [support offering](https://www.trustsource.io/support) or checkout the [knowledgebase](https://support.trustsource.io) for more information.
