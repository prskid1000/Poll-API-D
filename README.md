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
