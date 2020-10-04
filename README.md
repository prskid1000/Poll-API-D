# Poll-API-D
It is a poll system API based on graphql and Django

## Installation:
$cd Polls
$pip3 install pipenv
$pipenv shell
$pip3 install django
$pip3 install graphene-django
$python manage.py makemigrations
$python manage.py migrate
$python manage.py runserver

## Executing queries
//You will get an url append /graphql at end of it
//You will get into graphiql ide on entering the appended url
//For accessing API in other way view official documentation

## QUERY SYNTAX

mutation createArea {
  createArea(input: {name: "Sonari",winningParty:"None",oppositionParty:"None",winner:"None",opposition:"None"}) {
    ok
    area {
      id
      name
      winner
      winningParty
      oppositionParty
    }
  }
}

mutation deleteArea {
  deleteArea(id:2) {
    ok
    area {
      id
      name
      winningParty
      oppositionParty
    }
  }
}

mutation updateArea {
  updateArea(id:1,input: {name: "Anari",winningParty:"None",oppositionParty:"None",winner:"None",opposition:"None"}) {
    ok
    area {
      id
      name
      winner
      winningParty
      oppositionParty
    }
  }
}

mutation pollArea {
  pollArea(id:1,input: {name: "Sonari"}) {
    ok
   area {
      id
      name
      winningParty
      oppositionParty
      opposition
      winner
    }
  }
}

mutation createVoter {
  createVoter(input: {name: "Prithwiraj", partyPrefered: "Congress", place: "Sonari", age: 24}) {
    ok
   voter {
      id
      name
      partyPrefered
      place
      age
    }
  }
}

mutation updateVoter {
  updateVoter(id:5,input: {name: "Prithwiraj", partyPrefered: "Congress", place: "Sonari", age: 24}) {
    ok
   voter {
      id
      name
      partyPrefered
      place
      age
    }
  }
}

mutation deleteVoter {
  deleteVoter(id:4) {
    ok
    voter {
      id
      name
      partyPrefered
      place
    }
  }
}


mutation castVoter {
  castVoter(id:4,input: {name: "Prithwiraj", partyPrefered: "Congress", place: "Sonari", age: 22}) {
    ok
   voter {
      id
      name
      partyPrefered
      place
      age
    }
  }
}

mutation createCandidate {
  createCandidate(input: {name: "Prithwi", party: "Congress", place: "Sonari", age: 27,votes:0}) {
    ok
   candidate {
      id
      name
      party
      place
      age
    }
  }
}

mutation updateCandidate {
  updateCandidate(id:2,input: {name: "Prithwi", party: "Congress", place: "Sonari", age: 27,votes:0}) {
    ok
   candidate {
      id
      name
      party
      place
      age
    }
  }
}

mutation deleteCandidate {
  deleteCandidate(id:2) {
    ok
    candidate {
      id
      name
      party
      place
      votes
    }
  }
}

## Status
Repository status([badge](https://img.shields.io/badge/)):
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)
![Version](https://img.shields.io/badge/version-1.0.0-green)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

## Getting started

- Fork the repository.
- Clone it to your machine.

## Code of Conduct

We really appreciate the keen interest and the overall work culture we create by
working together as a team with various unique experiences and minds culminated
into a single project. This is only possible if we respect each other.

Kindly go through our
[Code of Conduct](https://github.com/prskid1000/Template/blob/main/.github/CODE_OF_CONDUCT_TEMPLATE/CODE_OF_CONDUCT.md)
to take a moment and familiarise with the spirit of opensource.

## Contributing Guide

If you're have worked on the front-end part make PR to the front-end branch
and same goes for the back-end too.

### PR rules:
- Kindly follow the Pull Request template provided.

For more details kindly go through our
[Contributing Guidelines.](https://github.com/prskid1000/Template/blob/main/.github/CONTRIBUTING_TEMPLATE/CONTRIBUTING.md)

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="http://biograph.dx.am/"><img src="https://avatars0.githubusercontent.com/prskid1000" width="100px;" alt=""/><br /><sub><b>prskid1000</b></sub></a><br /><a href="https://github.com/prskid1000/Template/commits?author=prskid1000" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!

