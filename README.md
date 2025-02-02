# Usage Guidance
## REpresentational State Transfer

### Molar Mass
###### calculate/molar_mass/
##### payload
```json
{
    "formula": "H2O"
}
```
##### response
```json
{
    "message": "Success",
    "data": {
        "formula": "H2O",
        "molar_mass": 18.015
    }
}
```

### pH
###### calculate/ph/
##### payload
```json
{
    "concentration": 0.001
}
```
##### response
```json
{
    "message": "Success",
    "data": {
        "pH": 3.0, 
        "pOH": 11.0
    }
}
```

### Gas Law
###### calculate/gas_law/
##### payload
```json
{
    "pressure": 1.0,
    "volume": 22.4,
    "temperature": 273.15
}

```
##### response
```json
{
    "message": "Success",
    "data": {
        "n": 0.9988577793741664
    }
}
```

### Stoichiometry
###### calculate/stoichiometry/
##### payload
```json
{
  "reactants": {"H2": 2, "O2": 1},
  "products": {"H2O": 2}
}
```
##### response
```json
{
    "message": "Success",
    "data": {
        "molar_ratio": {
            "H2O": {
                "H2": 1.0,
                "O2": 2.0
            }
        }
    }
}
```


## GraphQL
