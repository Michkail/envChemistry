# Usage Guidance
## GraphQL
### List Element
###### graphql/
##### mutation
```graphql
mutation {
  getElementList {
    message
    data
  }
}
```
##### response
```json
{
  "data": {
    "getElementList": {
      "message": "Success",
      "data": [
        {
          "atomic_number": 1,
          "atomic_mass": 1.008,
          "symbol": "H",
          "name": "Hydrogen",
          "category": "Nonmetal",
          "density": 0.08988,
          "melting_point": 13.99,
          "boiling_point": 20.271
        },
        ...
        {
          "atomic_number": 118,
          "atomic_mass": 294,
          "symbol": "Og",
          "name": "Oganesson",
          "category": "Noble Gas",
          "density": 47,
          "melting_point": 2800,
          "boiling_point": 7100
        }
      ]
    }
  }
}
```

### Molar Mass
###### graphql/
##### mutation
```graphql
mutation {
  calculateMolarMass(input: { formula: "H2O" }) {
    message
    data
  }
}
```
##### response
```json
{
  "data": {
    "calculateMolarMass": {
      "message": "Success",
      "data": {
        "H2O": 18.015
      }
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
    reactants: "{ \"H2\": 2, \"O2\": 1 }",
    products: "{ \"H2O\": 2 }"
  }) {
    message
    data
  }
}
```
##### response
```json
{
  "data": {
    "calculateStoichiometry": {
      "message": "Success",
      "data": {
        "molar_ratio": {
          "H2O": {
            "H2": 1,
            "O2": 2
          }
        }
      }
    }
  }
}
```

### pH
###### graphql/
##### mutation
```graphql
mutation {
  calculatePh(input: { concentration: 0.0001 }) {
    message
    data
  }
}
```
##### response
```json
{
  "data": {
    "calculatePh": {
      "message": "Success",
      "data": {
        "pH": 4,
        "pOH": 10
      }
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
    pressure: 1.0,
    volume: 22.4,
    temperature: 273.15
  }) {
    message
    data
  }
}
```
##### response
```json
{
  "data": {
    "calculateIdealGasLaw": {
      "message": "Success",
      "data": {
        "n": 0.9988577793741664
      }
    }
  }
}
```