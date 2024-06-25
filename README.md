# xcures_day
python wrapper for the xcures REST api.

## Status == UNSTABLEish
* The auth functionality is working.
* Subject API query is working, but not tested extensively.
* Other API hooks, ie: query, are not implemented in a trusted way quite yet.
* TODO: I'll benefit from a quick discussion w/the Xcures tech team.


# Configuruartion

## Environment
### Conda
* [Install Miniconda](https://docs.anaconda.com/miniconda/miniconda-install/)
* Create a new environment.
```bash
conda create -y -n XCDAY -c conda-forge python=3.10 ipython pytest pip pytz requests ipython && conda activate XCDAY && pip install yaml_config_day
```

* Activate the environment
```bash
conda activate XCDAY
```

## YAML File
* Located in `~/.config/xcures/xcures_$XCURES_ENV.yaml`, where `XCURES_ENV=` might be `prod` or `test`.
* Contents:
  
```bash
export XCURES_ENV=prod
more ~/.config/xcures/xcures_$XCURES_ENV.yaml
```


```yaml
---
base_url: "https://partner.xcures.com"
base_auth_url: "https://xcures-patient-registry-prod.us.auth0.com"
project_id: "PROJECTIDHERE"
client_id: "CLIENTIDHERE"
client_secret: "SECRETKEYHERE"
```


# Usage
_given the env is set and the yaml file is configured_

## Authenticate
```python
from xcures.xcures_api import XCuresAPI as xc_api

xc = xc_api()
print(xc)
# prints something like <xcures.xcures_api.XCuresAPI at 0x10cd814e0>

print(x.token)
# token printed
```


## Crude Test
```python
conda activate XCDAY
python xcures/xcures_api.py # just for quick dev, this will be moved to proper pytest.
```