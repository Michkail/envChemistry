# Usage Guidance
## GraphQL
### List Element
###### graphql/
##### mutation
```graphql
mutation {
  getElementList {
    atomicMass
    atomicNumber
    symbol
    name
    category
    density
    meltingPoint
    boilingPoint
  }
}
```
##### response
```json
{
  "data": {
    "getElementList": [
      {
        "atomicMass": 1.008,
        "atomicNumber": 1,
        "symbol": "H",
        "name": "Hydrogen",
        "category": "Nonmetal",
        "density": 0.00008988,
        "meltingPoint": -259.16,
        "boilingPoint": -252.87
      },
      {
        "atomicMass": 6.94,
        "atomicNumber": 3,
        "symbol": "Li",
        "name": "Lithium",
        "category": "Alkali Metal",
        "density": 0.534,
        "meltingPoint": 180.54,
        "boilingPoint": 1342
      },
      ...
    ]
  }
}
```


### Molar Mass
###### graphql/
##### mutation
```graphql
mutation {
  calculateMolarMass(input: {
    formula: "H2O"
  }) {
    molarMass
  }
}
```
##### response
```json
{
  "data": {
    "calculateMolarMass": {
      "molarMass": "{\"H2O\": 18.015}"
    }
  }
}
```

### Stoichiometry **Reactant | Product**
###### graphql/
##### mutation
```graphql
mutation {
  calculateStoichiometry(input: {
    reactants: "{\"H2\":2,\"O2\":1}",
    products: "{\"H2O\":2}"
  }) {
    molarRatio
  }
}
```
##### response
```json
{
  "data": {
    "calculateStoichiometry": {
      "molarRatio": "{\"H2O\": {\"H2\": 1.0, \"O2\": 2.0}}"
    }
  }
}
```

### pH
###### graphql/
##### mutation
```graphql
mutation {
  calculatePh(input: { concentration: 0.001 }) {
    ph
  }
}
```
##### response
```json
{
  "data": {
    "calculatePh": {
      "ph": -1000
    }
  }
}
```

### Gas Law
###### graphql/
##### mutation
```graphql
mutation {
  calculateIdealGasLaw(input: {
    pressure: 1,
    volume: 22.4,
    temperature: 273
  }) {
    n
  }
}
```
##### response
```json
{
  "data": {
    "calculateIdealGasLaw": {
      "n": 0.9994066023298664
    }
  }
}
```