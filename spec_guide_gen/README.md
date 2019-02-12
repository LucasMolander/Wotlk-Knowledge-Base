# Spec Guide Gen

This directory serves four main purposes:
  1) Storing the contents of Warmane spec guides (in JSON format)
  2) Defining the structure of a guide
  3) Validating the structures of stored guides
  4) Generating HTML for a guide

## Storage
Each guide is stored in its own JSON file, e.g.:
```
{
  "Spec": "Combat Rogue",
  "Original Author": "Fluffybully",
  "Original Link":   "http://forum.warmane.com/showthread.php?t=332641",
  "Strengths": [
    "Sustained single-target DPS",
    "Burst AoE DPS"
  ],
  "Weaknesses": [
    "Switching targets frequently"
  ]
}
```

## Structure Definition
`validate.py` is the source of truth for what content a guide should have.
It uses [jsonschema](https://github.com/Julian/jsonschema) to define this in an abstract way.


This is an example of a structure definition that matches the JSON from [Storage](#storage):
```
{
  'type': 'object',
  'properties': {
    'Spec':            {'type': 'string'},
    'Original Author': {'type': 'string'},
    'Original Link':   {'type': 'string'},
    'Strengths':       {'type': 'array', 'items': {'type': 'string'}},
    'Weaknesses':      {'type': 'array', 'items': {'type': 'string'}}
  }
}
```

## Structure Validation
Run `python validate.py` to validate the structure of each guide. It'll output which guides were valid and which weren't, along with verbose explanations for invalid guides.

If `python validate.py` doesn't work, install Python 2.7+ and run `pip install -r requirements.txt` wihle in this directory.

## HTML Generation

`<UNDER CONSTRUCTION>`

