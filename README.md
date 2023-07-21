# ODMantic Many relations Model

This example show how to deal with Model Reference with ODMantic.

The goal here is to get full Reference datas when requesting the parent Model

## Install

```bash
docker compose up -d
# old style : docker-compose up -d
```

App is accessible at http://localhost:9800

Use `DbGate` at http://localhost:9801 to navigate into Mongo Database


## What ODMantic do

### 1 - Sub Model

```python
class Skill(Model):
    description:str = Field()

class Student(Model):
    skills: List[Skills] # Sub Model (nested)
```

NoSQL result in Database :
```MQL5
{
    _id: Object { $oid: "64baa62d315ab7b15551d0c4" }
    fullname: "John Doe"
    school: Object { $oid: "64baa62d315ab7b15551d0c0" }
    skills: [
        Object {
            id: Object { $oid: "64baa62d315ab7b15551d0c1" }
            description: "C++"
        }
        Object {
            id: Object { $oid: "64baa62d315ab7b15551d0c2" }
            description: "Python3"
        }
        Object {
            id: Object { $oid: "64baa62d315ab7b15551d0c3" }
            description: "MongoDB"
        }
    ]
}
```

JSON result through request :
```json
[
  {
    "id": "64baa62d315ab7b15551d0c4",
    "fullname": "John Doe",
    "skills": [
      {
        "description": "C++",
        "id": "64baa62d315ab7b15551d0c1"
      },
      {
        "description": "Python3",
        "id": "64baa62d315ab7b15551d0c2"
      },
      {
        "description": "MongoDB",
        "id": "64baa62d315ab7b15551d0c3"
      }
    ]
  }
]
```

>Pro/Con Sub Model
>* 💚 Model References can be created in a same time
>* 💔 No easy access to all Model References (Skill) created with this mode
>* 💔 Model References can not be created separately

ODMantic Documentation : https://art049.github.io/odmantic/modeling/#one-to-many

### 2 - Model Reference

```python
class Skill(Model):
    description:str = Field()

class Student(Model):
    skills: List[ObjectId] # Model Reference
```

NoSQL result in Database :
```MQL5
{
    _id: Object { $oid: "64ba99d15728708bb9aa2ba8"},
    fullname: "John Doe",
    skills: [
        Object { $oid: "64ba99d15728708bb9aa2ba4" },
        Object { $oid: "64ba99d15728708bb9aa2ba5" },
        Object { $oid: "64ba99d15728708bb9aa2ba6" },
    ]
}
```

JSON result through request :
```json
{
    "id": "64ba99d15728708bb9aa2ba8",
    "fullname": "John Doe",
    "skills": [
        "64ba99d15728708bb9aa2ba4",
        "64ba99d15728708bb9aa2ba5",
        "64ba99d15728708bb9aa2ba6"
    ]
}
```

>Pro/Con
>* 💛 Model References have to be created separately
>* 💚 Models can easely be requested separately through the engine
>* 💔 Reference Model fields are not displayed on the fly

ODMantic Documentation : https://art049.github.io/odmantic/modeling/#many-to-many-manual

## What we want

We want NoSQL both result of `1 - Sub Model` and JSON result of `2 - Model Reference`.

That what this example solve ✅

NoSQL result in Database :
```MQL5
{
    _id: Object { $oid: "64ba99d15728708bb9aa2ba8"},
    fullname: "John Doe",
    skills: [
        Object { $oid: "64ba99d15728708bb9aa2ba4" },
        Object { $oid: "64ba99d15728708bb9aa2ba5" },
        Object { $oid: "64ba99d15728708bb9aa2ba6" },
    ]
}
```

JSON result through request :
```json
[
  {
    "id": "64baa62d315ab7b15551d0c4",
    "fullname": "John Doe",
    "skills": [
      {
        "description": "C++",
        "id": "64baa62d315ab7b15551d0c1"
      },
      {
        "description": "Python3",
        "id": "64baa62d315ab7b15551d0c2"
      },
      {
        "description": "MongoDB",
        "id": "64baa62d315ab7b15551d0c3"
      }
    ]
  }
]
```

>Pro/Con
>* 💛 Model References have to be created separately
>* 💚 Models can easely be requested separately through the engine
>* 💚 Reference Model fields are displayed on the fly

## More informations

Related `art049/odmantic` topics
* https://github.com/art049/odmantic/issues/95
* https://github.com/art049/odmantic/issues/56

This Pydantic trick is also posted here
* https://github.com/pydantic/pydantic/issues/857#issuecomment-1644311858

