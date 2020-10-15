"""
Update Floruit management command
EH 26/5/2020

A command to apply the calculate folruit to all people
This was first written to correct some errors in the inital update
which led to bad floruits, it can now be rerun as needed if
for instance new roles are added to evidence.
"""


from django.core.management.base import BaseCommand, CommandError
from pomsapp.models import Person
from pomsapp.actions_models import build_floruits

class Command(BaseCommand):

    help = 'Update Person floruits using updateFloruitsFrom Transaction'

    def handle(self, *args, **options):
        # Get all people that are indexed
        people = Person.objects.filter(pk__gte=5176).order_by(
                'pk'
            )
        for person in people:
            print(
                'Person {}, {}\n '.format(person.pk, person))
            start_year = person.floruitstartyr
            end_year = person.floruitendyr
            # Run floruit
            build_floruits(person, False)
            import pdb
            pdb.set_trace()
            if (start_year != person.floruitstartyr or
                    end_year != person.floruitendyr):
                # if different, add to output
                msg='Person {}, {} floruit changed, '.format(person.pk, person)
                if start_year != person.floruitstartyr:
                    msg+=' start year from {} to {}'.format(
                        start_year,person.floruitstartyr
                    )
                if end_year != person.floruitendyr:
                    msg+=' end year from {} to {}'.format(
                        end_year,person.floruitendyr
                    )
                #msg+='\n'
                print(msg)
                person.save()