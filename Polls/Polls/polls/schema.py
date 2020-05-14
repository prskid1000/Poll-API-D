import graphene

from graphene_django.types import DjangoObjectType

from Polls.polls.models import Area, Voter, Candidate


class AreaType(DjangoObjectType):
    class Meta:
        model = Area


class VoterType(DjangoObjectType):
    class Meta:
        model = Voter

class CandidateType(DjangoObjectType):
    class Meta:
        model = Candidate


class Query(object):

    all_areas = graphene.List(AreaType)
    areas_by_ruling_party=graphene.List(AreaType)
    areas_by_opposition_party=graphene.List(AreaType)

    all_voters = graphene.List(VoterType)
    voters_by_name = graphene.List(VoterType)
    voters_by_party_prefered = graphene.List(VoterType)
    voters_by_place = graphene.List(VoterType)
    voters_by_age = graphene.List(VoterType)


    all_candidates = graphene.List(CandidateType)
    candidate_by_name = graphene.List(CandidateType)
    candidate_by_party = graphene.List(CandidateType)
    candidate_by_place = graphene.List(CandidateType)
    candidate_by_age = graphene.List(CandidateType)

    def resolve_all_areas(self, info, **kwargs):
        return Area.objects.all()

    def resolve_areas_by_name(self, info, **kwargs):
        return Area.objects.all().filter(name=kwargs.get('name'))

    def resolve_areas_by_ruling_party(self, info, **kwargs):
        return Area.objects.all().filter(winning_party=kwargs.get('winning_party'))

    def resolve_areas_by_opposition_party(self, info, **kwargs):
        return Area.objects.all().filter(opposition_party=kwargs.get('opposition_party'))


    def resolve_all_voters(self, info, **kwargs):
        return Voter.objects.all()

    def resolve_voters_by_name(self, info, **kwargs):
        return Voter.objects.all().filter(name=kwargs.get('name'))

    def resolve_voters_by_party_prefered(self, info, **kwargs):
        return Voter.objects.all().filter(party_prefered=kwargs.get('party_prefered'))

    def resolve_voters_by_place(self, info, **kwargs):
        return Voter.objects.all().filter(place=kwargs.get('place'))

    def resolve_voters_by_age(self, info, **kwargs):
        return Voter.objects.all().filter(age=kwargs.get('age'))



    def resolve_all_Candidate(self, info, **kwargs):
        return Candidate.objects.all()

    def resolve_candidate_by_name(self, info, **kwargs):
        return Voter.objects.all().filter(name=kwargs.get('name'))

    def resolve_candidate_by_party(self, info, **kwargs):
        return Voter.objects.all().filter(party=kwargs.get('party_prefered'))

    def resolve_candidate_by_place(self, info, **kwargs):
        return Voter.objects.all().filter(place=kwargs.get('place'))

    def resolve_candidate_by_age(self, info, **kwargs):
        return Voter.objects.all().filter(age=kwargs.get('age'))


class CandidateInput(graphene.InputObjectType):
    name = graphene.String()
    party = graphene.String()
    place = graphene.String()
    age = graphene.Int()
    votes = graphene.Int()

class VoterInput(graphene.InputObjectType):
    name = graphene.String()
    party_prefered = graphene.String()
    place = graphene.String()
    age = graphene.Int()


class AreaInput(graphene.InputObjectType):
    name = graphene.String()
    winning_party = graphene.String()
    opposition_party = graphene.String()
    winner = graphene.String()
    opposition = graphene.String()

class CreateVoter(graphene.Mutation):
    class Arguments:
        input = VoterInput(required=True)

    ok = graphene.Boolean()
    voter = graphene.Field(VoterType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        voter_instance = Voter(name=input.name,party_prefered=input.party_prefered,place=input.place,age=input.age)
        voter_instance.save()
        return CreateVoter(ok=ok, voter=voter_instance)

class CreateArea(graphene.Mutation):
    class Arguments:
        input = AreaInput(required=True)

    ok = graphene.Boolean()
    area = graphene.Field(AreaType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        area_instance = Area(name=input.name,winning_party=input.winning_party,opposition_party=input.opposition_party)
        area_instance.save()
        return CreateArea(ok=ok, area=area_instance)

class CreateCandidate(graphene.Mutation):
    class Arguments:
        input = CandidateInput(required=True)

    ok = graphene.Boolean()
    candidate = graphene.Field(CandidateType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        candidate_instance = Candidate(name=input.name,party=input.party,place=input.place,age=input.age,votes=input.votes)
        candidate_instance.save()
        return CreateCandidate(ok=ok, candidate=candidate_instance)

class UpdateCandidate(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = CandidateInput(required=True)

    ok = graphene.Boolean()
    candidate = graphene.Field(CandidateType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        candidate_instance = Candidate.objects.get(pk=id)
        if candidate_instance:
            ok = True
            candidate_instance.name = input.name
            candidate_instance.party = input.party
            candidate_instance.place = input.place
            candidate_instance.age = input.age
            candidate_instance.save()
            return UpdateCandidate(ok=ok, candidate=candidate_instance)
        return UpdateCandidate(ok=ok, candidate=None)

class UpdateVoter(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = VoterInput(required=True)

    ok = graphene.Boolean()
    voter = graphene.Field(VoterType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        voter_instance = Voter.objects.get(pk=id)
        if voter_instance:
            ok = True
            voter_instance.name = input.name
            voter_instance.party_prefered = input.party_prefered
            voter_instance.place = input.place
            voter_instance.age = input.age
            voter_instance.save()
            return UpdateVoter(ok=ok, voter=voter_instance)
        return UpdateVoter(ok=ok, voter=None)

class CastVoter(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = VoterInput(required=True)

    ok = graphene.Boolean()
    voter = graphene.Field(VoterType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        choice = Candidate.objects.all().filter(party=input.party_prefered)
        voter_instance = Voter.objects.get(pk=id)
        if voter_instance:
            ok = True
            for i in choice:
                i.votes=i.votes+1
                i.save()
            return CastVoter(ok=ok, voter=voter_instance)
        return CastVoter(ok=ok, voter=None)

class UpdateArea(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = AreaInput(required=True)

    ok = graphene.Boolean()
    area = graphene.Field(AreaType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        area_instance = Area.objects.get(pk=id)
        if area_instance:
            ok = True
            area_instance.name = input.name
            area_instance.winning_party = input.winning_party
            area_instance.winner = input.winner
            area_instance.opposition_party = input.opposition_party
            area_instance.opposition = input.opposition
            area_instance.save()
            return UpdateArea(ok=ok, area=area_instance)
        return UpdateArea(ok=ok, area=None)

class DeleteCandidate(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    ok = graphene.Boolean()
    candidate = graphene.Field(CandidateType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        candidate_instance = Candidate.objects.get(pk=id)
        if candidate_instance:
            ok = True
            candidate_instance.delete()
            return DeleteCandidate(ok=ok, candidate=None)
        return DeleteCandidate(ok=ok, candidate=None)

class DeleteVoter(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    ok = graphene.Boolean()
    voter = graphene.Field(VoterType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        voter_instance = Voter.objects.get(pk=id)
        if voter_instance:
            ok = True
            voter_instance.delete()
            return DeleteVoter(ok=ok, voter=None)
        return DeleteVoter(ok=ok, voter=None)

class DeleteArea(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    ok = graphene.Boolean()
    area = graphene.Field(AreaType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        area_instance = Area.objects.get(pk=id)
        if area_instance:
            ok = True
            area_instance.delete()
            return DeleteArea(ok=ok, area=None)
        return DeleteArea(ok=ok, area=None)

class PollArea(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = AreaInput(required=True)

    ok = graphene.Boolean()
    area = graphene.Field(AreaType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        area_instance = Area.objects.get(pk=id)
        if area_instance:
            ok = True
            area_instance.name = input.name
            eligible_candidate=Candidate.objects.all().filter(place=input.name)
            area_instance.winning_party=eligible_candidate[len(eligible_candidate)-1].party
            area_instance.opposition_party="None"
            area_instance.winner=eligible_candidate[len(eligible_candidate)-1].name
            area_instance.opposition="None"
            mxvotes=-1

            for i in eligible_candidate:
                if i.votes>mxvotes and i.age>=18:
                    area_instance.opposition_party=area_instance.winning_party
                    area_instance.winning_party=i.party
                    area_instance.opposition=area_instance.winner
                    area_instance.winner=i.name
                    mxvotes=i.votes
            area_instance.save()
            return PollArea(ok=ok, area=area_instance)
        return PollArea(ok=ok, area=None)

class Mutation(graphene.ObjectType):
    create_candidate = CreateCandidate.Field()
    update_candidate = UpdateCandidate.Field()
    delete_candidate = DeleteCandidate.Field()

    create_voter = CreateVoter.Field()
    update_voter = UpdateVoter.Field()
    delete_voter = DeleteVoter.Field()
    cast_voter = CastVoter.Field()

    create_area = CreateArea.Field()
    update_area = UpdateArea.Field()
    delete_area = DeleteArea.Field()
    poll_area = PollArea.Field()
