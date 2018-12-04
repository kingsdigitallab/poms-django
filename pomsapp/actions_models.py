from django.utils.encoding import smart_text
import datetime
from django.conf import settings
from pomsapp.models_authlists import (GrantorCategory, Proanimagenerictypes,
                                      DocTickboxes, TransTickboxes)


######################
# MODELS UTILS
######################

if settings.LOCAL_SERVER:
    EXTRA_SAVING_ACTIONS = False
else:
    EXTRA_SAVING_ACTIONS = True


def create_helperDateRange(obj):
    """
    hard-code a date range string representation to certain objects
    (for the faceted search)
    """

    def assignRangeFromSelection(int1, int2):
        RANGES = [(1093, 1124), (1124, 1153), (1153, 1165), (1165, 1214),
                  (1214, 1249), (1249, 1286), (1286, 1296), (1296, 1314), ]
        # in reality, we're only checking the first date, otherwise we'll have
        # to assing multiple ranges to the same item
        if int1:
            if int1 == 1314:  # cause the last one is left out by range()
                return "1296-1314"
            else:
                for x in RANGES:
                    if int1 in range(x[0], x[1]):
                        return "%d-%d" % (x[0], x[1])
        return None

    if obj.__class__.__name__ == 'Person':
        print(
            "Creating create_helperDateRange\
            text for person id[%d]" % obj.id)
        try:
            test = assignRangeFromSelection(
                obj.floruitstartyr, obj.floruitendyr)
            if test:
                obj.helper_daterange = test
                print("helperDateRange	 = [%s]" % smart_text(test))
        except BaseException:
            print(
                "************\nProblem with\
                person id[%d]\n************" % (obj.id))
            pass
        return obj

    elif obj.__class__.__name__ in ('Source', 'Charter'):

        print(
            "Saving create_helperDateRange text for source id[%d]" % obj.id)
        try:
            test = assignRangeFromSelection(obj.from_year, obj.to_year)
            if test:
                obj.helper_daterange = test
                print("helperDateRange	 = [%s]" % smart_text(test))
        except BaseException:
            print(
                "************\nProblem with source\
                id[%d]\n************" % (obj.id))
            pass
        return obj

    elif obj.__class__.__name__ in ('FactTitle', 'FactPossession',
                                    'FactTransaction', 'FactRelationship',
                                    'FactReference'):
        print("Saving create_helperDateRange text for %s id[%d]" % (
            obj.__class__.__name__, obj.id))
        try:
            test = assignRangeFromSelection(obj.from_year, obj.to_year)
            if test:
                obj.helper_daterange = test
                print("helperDateRange	 = [%s]" % smart_text(test))
        except BaseException:
            print(
                "************\nProblem with\
                factoid id[%d]\n************" % (obj.id))
            pass
        return obj

    else:
        raise TypeError(
            "create_helperDateRange error: you didn't pass the right\
            object! (I accept only Person, Source or "
            "Factoid-s- instances...)")
    return obj


def all_dates_blank(obj):
    """helper method for checking whether all dates have been
            left empty in the
            pre-saved factoid instance. We put the method here so
            that it can be called by all the
            subclasses of factoid """

    datefields = {	 'has_firmdate': False, 'has_firmdayonly': False,
                    'undated': False, 'eitheror': False,
                    'from_modifier': "", 'from_weekday': None,
                    'from_day': None,
                    'from_modifier2': "", 'from_month': None,
                    'from_season': None, 'from_year': None,
                    'to_modifier': "", 'to_weekday': None, 'to_day': None,
                    'to_modifier2': "", 'to_month': None,
                    'to_season': None, 'to_year': None,
                                    'datingnotes': "", 'probabledate': ""}

    for x in datefields.items():
        if getattr(obj, x[0]) != x[1]:
            return False
    return True


def copy_dates_over(obj_from, obj_to):
    """ copies all the dates from one obj (=charter) to another (=factoid)"""

    datefields = {	'has_firmdate': False, 'has_firmdayonly': False,
                   'undated': False, 'eitheror': False,
                   'from_modifier': "", 'from_weekday': None,
                   'from_day': None,
                                    'from_modifier2': "", 'from_month': None,
                                    'from_season': None, 'from_year': None,
                                    'to_modifier': "", 'to_weekday': None,
                                    'to_day': None,
                                    'to_modifier2': "", 'to_month': None,
                                    'to_season': None, 'to_year': None,
                                    'firmdate': "", 'datingnotes': "",
                                    'probabledate': ""}
    try:
        for x in datefields.items():
            setattr(obj_to, x[0], getattr(obj_from, x[0]))
        return True
    except BaseException:
        return "error with copying over the object dates"


# valid for charters && factoids
def create_firmdate(obj):
    """ gets an objects, extracts the dates and makes a nice firmdate
    string representation"""
    if not all_dates_blank(obj):
        if obj.undated:
            return "undated"
        print(".....creating firmdate for %s" % obj)
        datefrom = ""
        dateto = ""

        if obj.has_firmdayonly:	 # '15 Dec, 1154 x 1159'
            year1 = ""
            year2 = ""
            if obj.from_modifier:
                datefrom += "%s " % obj.get_from_modifier_display()
            if obj.from_weekday:
                datefrom += "%s " % obj.get_from_weekday_display()
            if obj.from_day:
                datefrom += "%s " % obj.get_from_day_display()
            if obj.from_modifier2:
                datefrom += "%s " % obj.get_from_modifier2_display()
            if obj.from_month:
                datefrom += "%s " % obj.get_from_month_display()
            if obj.from_season:
                datefrom += "%s " % obj.get_from_season_display()
            if obj.from_year:
                year1 = "%s" % str(obj.from_year)
            if obj.to_year:
                year2 = "%s" % str(obj.to_year)

            return "%s, %s X %s" % (datefrom.strip(), year1, year2)

        if obj.from_modifier:
            datefrom += "%s " % obj.get_from_modifier_display()
        if obj.from_weekday:
            datefrom += "%s " % obj.get_from_weekday_display()
        if obj.from_day:
            datefrom += "%s " % obj.get_from_day_display()
        if obj.from_modifier2:
            datefrom += "%s " % obj.get_from_modifier2_display()
        if obj.from_month:
            datefrom += "%s " % obj.get_from_month_display()
        if obj.from_season:
            datefrom += "%s " % obj.get_from_season_display()
        if obj.from_year:
            datefrom += "%s " % str(obj.from_year)

        if not obj.has_firmdate:
            if obj.to_modifier:
                dateto += "%s " % obj.get_to_modifier_display()
            if obj.to_weekday:
                dateto += "%s " % obj.get_to_weekday_display()
            if obj.to_day:
                dateto += "%s " % obj.get_to_day_display()
            if obj.to_modifier2:
                dateto += "%s " % obj.get_to_modifier2_display()
            if obj.to_month:
                dateto += "%s " % obj.get_to_month_display()
            if obj.to_season:
                dateto += "%s " % obj.get_to_season_display()
            if obj.to_year:
                dateto += "%s " % str(obj.to_year)

        if not obj.has_firmdate:
            return "%sX %s" % (datefrom, dateto)
        else:
            return "%s" % (datefrom)


def fix_spiritualBenefits(transaction_instance):
    """
    Adds a 'generic' spriritual benefit so that in searches we
    can simulate a top-level
    hiearchy kind of value.
    """
    if EXTRA_SAVING_ACTIONS:
        generic_benefit = Proanimagenerictypes.objects.get(id=75)
        try:
            if transaction_instance.spiritualbenefits.all():
                transaction_instance.spiritualbenefits.add(generic_benefit)
        except BaseException:
            print("Error with <fix_spiritualBenefits>!!")
    return transaction_instance


def fix_inferredType(factoid_instance):
    """Makes sure the inferred type field is filled in..
    Used to be done in signals but it was a bit weak .. need to dbcheck it
    """
    if not factoid_instance.inferred_type and EXTRA_SAVING_ACTIONS:
        try:
            if factoid_instance.get_right_subclass()[0]:
                factoid_instance.inferred_type =\
                    factoid_instance.get_right_subclass()[0]
        except BaseException:
            print("Error!!!!")
    return factoid_instance


def copy_charter_dates2factoids(charter):
    for factoid in charter.get_factoids():
        if factoid.inferred_type == 'transaction':
            transaction = factoid.facttransaction
            if transaction.isprimary:
                copy_dates_over(charter, transaction)
                transaction.save()
                print("====copied to transaction dates =====")
        else:
            copy_dates_over(charter, factoid)
            factoid.save()
            print("====copied to factoid dates =====")


def updateFloruitsFromTransaction(trans):
    """
    2012-08-20: extracted from model methods
    """
    # if trans.helper_floruits:
    if False:  # 2012-08-20: disabled because of an 'operational error'
                # cropping up - needs to be debugged properly
                # might have to do with several users working on same model
                # instance with multiple related rows..
        print("++ transaction requested to SAVE FLORUITS")
        person_candidates = []
        # 2012-06-22: updated
        valid_roles = ['Grantor', 'Beneficiary', 'Addressor', 'Addressee',
                       'Party 1',
                       'Party 2', 'Party 3', 'Consentor', 'Dated by hand of',
                       'Inspector', 'Scribe', 'Sealer', 'Signatory',
                       'Witness',
                       'Judge', 'Recipient of fealty', 'Performer of fealty',
                       'Bearer of letters', 'Juror']

        for x in trans.witnesses.all():
            person_candidates.append(x)
        for x in trans.assocfactoidperson_set.all():
            if x.role:
                if x.role.name in valid_roles:
                    person_candidates.append(x.person)
        if person_candidates:
            for person in list(set(person_candidates)):
                person.helper_floruits = True  # otherwise it won't save
                person.save()
    else:
        print(
            "++ transaction requested to save FLORUITS -\
            DENIED cause trans.helper_floruits = False..")


def build_floruits(person_instance):
    """Helper method for constructing the floruits.
    Rule: In transactions, each dates-pair is expressed in the form A x B.
              Select the highest A and the lowest B.
              Then, if the highest-A is bigger that the lowest-B, invert them.
    """

    valid_roles = ['Grantor', 'Beneficiary', 'Addressor', 'Addressee',
                   'Party 1', 'Party 2',
                   'Party 3', 'Consentor', 'Dated by hand of', 'Inspector',
                   'Scribe', 'Sealer',
                   'Signatory', 'Witness', 'Judge', 'Recipient of fealty',
                   'Performer of fealty',
                   'Bearer of letters', 'Juror']
    candidates_from = []
    candidates_to = []

    print("====FLORUITS: ===== [person %d]" % person_instance.id)

    # load all candidates:
    #  witnesses are in there through a dedicated M2M
    for x in person_instance.assocfactoidwitness_set.all():
        if x.factoid.get_right_subclass():
            if x.factoid.get_right_subclass()[0] == "transaction":
                transaction = x.factoid.get_right_subclass()[1]
                if transaction.isprimary is True and\
                        transaction.eitheror is False and\
                        transaction.undated is False:
                    print("FLORUITS: witness in transaction %s" %
                          transaction)
                    candidates_from.append(transaction.from_year)
                    if transaction.from_year:
                        candidates_to.append(transaction.from_year)
                    else:
                        candidates_to.append(transaction.to_year)
    # now all the other AssocFactoid
    for x in person_instance.assoc_factoid_person.all():
        if x.factoid.get_right_subclass():
            if x.factoid.get_right_subclass()[0] == "transaction":
                if x.role:
                    if x.role.name in valid_roles:
                        transaction = x.factoid.get_right_subclass()[1]
                        if transaction.isprimary is True and\
                                transaction.eitheror is False and\
                                transaction.undated is False:
                            print("FLORUITS: %s in transaction %s" %
                                  (x.role.name, transaction))
                            candidates_from.append(transaction.from_year)
                            if transaction.has_firmdate:
                                candidates_to.append(transaction.from_year)
                            else:
                                candidates_to.append(transaction.to_year)

    if (len(candidates_from) > 0 and len(candidates_to) > 0):
        #  filtering out 0 and None
        """
        candidates_from = filter(lambda x: x != 0, candidates_from)
        candidates_from = filter(lambda x: x != None, candidates_from)
        candidates_to = filter(lambda x: x != 0, candidates_to)
        candidates_to = filter(lambda x: x != None, candidates_to)"""

        candidates_from = [x for x in candidates_from if x is not None]
        candidates_to = [x for x in candidates_to if x is not None]
        # if empty, just put a 0 in:
        if not candidates_from:
            candidates_from.append(0)
        if not candidates_to:
            candidates_to.append(0)
        print("====fromCandidates: = %s =	... highest is *%d*" %
              (candidates_from, max(candidates_from)))
        print("====toCandidates: = %s = ... lowest is *%d*" %
              (candidates_to, min(candidates_to)))

        if max(candidates_from) > min(candidates_to):
            print("FLORUITS: swapping values!")
            person_instance.floruitstartyr = min(candidates_to)
            person_instance.floruitendyr = max(candidates_from)
        else:
            person_instance.floruitstartyr = max(candidates_from)
            person_instance.floruitendyr = min(candidates_to)

        # the instance is saved in the main Person save() method
    return person_instance


def merge_persons_inner(main_person, person_list):
    """ given a list of people, it merges them into a pre-selected one """
    person_list_string = "%s" % person_list
    txt = main_person.internal_notes
    if person_list:
        for p in person_list:
            txt += "\n**********\n%s: Merged Person [%s]\nSurface\
                    name:%s\nMedieval name:%s\nModern name:%s\n\
                    Bio: %s\n" % (datetime.date.today(),
                                  p.id, p.persondisplayname,
                                  p.standardmedievalname,
                                  p.moderngaelicname,
                                  p.persondescription)
            for a in p.assocfactoidperson_set.all():
                a.person = main_person
                txt += "==>added factoid [%d, %s]\n" % (
                    a.factoid.id, a.factoid)
                a.save()
            for a in p.assocfactoidwitness_set.all():
                a.person = main_person
                txt += "==>added witness [%d, %s]\n" % (
                    a.factoid.id, a.factoid)
                a.save()
            for a in p.assocfactoidproanima_set.all():
                a.person = main_person
                txt += "==>added proanima [%d, %s]\n" % (
                    a.factoid.id, a.factoid)
                a.save()
            p.persondisplayname = "%s :: MERGED INTO [%d] ..OK TO DELETE" % (
                p.persondisplayname, main_person.id)
            p.save()
    main_person.internal_notes = txt
    # put back the flag to false
    main_person.helper_merge = False
    main_person.save()
    return [main_person, person_list_string]


def create_helper_surnames(obj):
    """ updates all the helper_surnames fields; returns an updated
    (not saved yet) object """

    print("....updating Surname info for [%s]" % obj)
    sur = obj.surname

    def trimsurname(surname):
        x = surname.strip()
        for particle in ['of ', 'de ', 'le ',
                         'Le ', 'del ', 'de ', '? de ', 'd\'']:
            if x.find(particle) == 0:
                x = x.strip(particle)
                break
        return x

    def combine_surname_fields(person):
        """ 2010-10-29: new version """
        x = ""
        if person.surname:
            x += person.surname + " "
            if person.ofstring:
                if person.ofstring.strip() == "of":
                    x += person.ofstring + " "
                    if person.placeandinst:
                        x += person.placeandinst + " "
        else:
            if person.patronym:
                x += person.patronym + " "
            if person.ofstring:
                if person.ofstring.strip() == "of":
                    x += person.ofstring + " "
                    if person.placeandinst:
                        x += person.placeandinst + " "

        return x.strip()

    # def combine_surname_fields(person):
    # x = ""
    # if person.surname:
    # 	x += person.surname + " "
    # if person.patronym:
    # 	x += person.patronym + " "
    # if person.ofstring:
    # 	if person.ofstring.strip() == "of":
    # 		x += person.ofstring + " "
    # 		if person.placeandinst:
    # 			x += person.placeandinst + " "
    # return x.strip()

    # old searchsurname: applies to 'surname' field only
    obj.searchsurname = trimsurname(sur)
    #  new searchsurnames fr FB
    obj.helper_bigsurname = combine_surname_fields(obj)
    obj.helper_searchbigsur = trimsurname(obj.helper_bigsurname)
    print("....bigsurname = [%s]" % obj.helper_bigsurname)
    print("....searchbigsurname = [%s]" % obj.helper_searchbigsur)
    return obj


##################
#
#  helpers for the authority lists
#
##################


GRANTOR_CATEGORIES = {
    'Kings of Scots':
    {'hammondnumber': 1, 'hammondnumb2__gte': 1, 'hammondnumb2__lte': 9},
        'Queens of Scots':
    {'hammondnumber': 1, 'hammondnumb2__gte': 10, 'hammondnumb2__lte': 12},
        'Kings of the Isle of Man':
    {'hammondnumber': 1, 'hammondnumb2__gte': 13, 'hammondnumb2__lte': 19},
        'Kings of England':
    {'hammondnumber': 1, 'hammondnumb2__gte': 20, 'hammondnumb2__lte': 27},
        'Scottish bishops':
    {'hammondnumber': 2, 'hammondnumb2__gte': 1, 'hammondnumb2__lte': 13},
        'English bishops':
    {'hammondnumber': 2, 'hammondnumb2__gte': 14, 'hammondnumb2__lte': 30},
        'Other bishops':
    {'hammondnumber': 2, 'hammondnumb2__gte': 31, 'hammondnumb2__lte': 34},
        'Secular cathedral chapters':
    {'hammondnumber': 2, 'hammondnumb2__gte': 35, 'hammondnumb2__lte': 45},
        'Archdeacons and officials':
    {'hammondnumber': 2, 'hammondnumb2__gte': 46, 'hammondnumb2__lte': 50},
        'Deans and parish clergy':
    {'hammondnumber': 2, 'hammondnumb2__gte': 51, 'hammondnumb2__lte': 54},
        'Other clerics':
    {'hammondnumber': 2, 'hammondnumb2__gte': 55, 'hammondnumb2__lte': 60},
        'Celi De':
    {'hammondnumber': 2, 'hammondnumb2__gte': 61, 'hammondnumb2__lte': 63},
        'Scottish monks':
    {'hammondnumber': 2, 'hammondnumb2__gte': 64, 'hammondnumb2__lte': 82},
        'Non-Scottish monks':
    {'hammondnumber': 2, 'hammondnumb2__gte': 83, 'hammondnumb2__lte': 92},
        'Canons regular':
    {'hammondnumber': 2, 'hammondnumb2__gte': 93,
     'hammondnumb2__lte': 103},
        'Friars':
    {'hammondnumber': 2, 'hammondnumb2': 104},
        'Collegiate churches':
    {'hammondnumber': 2, 'hammondnumb2': 105},
        'Military orders':
    {'hammondnumber': 2, 'hammondnumb2__gte': 106,
     'hammondnumb2__lte': 109},
        'Papal documents':
    {'hammondnumber': 2, 'hammondnumb2__gte': 121,
     'hammondnumb2__lte': 160},
        'Papal legates':
    {'hammondnumber': 2, 'hammondnumb2__gte': 200,
     'hammondnumb2__lte': 205},
        'Members of the royal family':
    {'hammondnumber': 3, 'hammondnumb2__gte': 1, 'hammondnumb2__lte': 9},
        'Scottish earls and countesses':
    {'hammondnumber': 3, 'hammondnumb2__gte': 10, 'hammondnumb2__lte': 22},
    # 2010-07-01 new
        'Non-Scottish earls and countesses':
    {'hammondnumber': 3, 'hammondnumb2__gte': 23, 'hammondnumb2__lte': 27},
        'Major lordships':
    {'hammondnumber': 3, 'hammondnumb2__gte': 28, 'hammondnumb2__lte': 38},
        'Scottish families, ABC':
    {'hammondnumber': 3, 'hammondnumb2__gte': 40,
     'hammondnumb2__lte': 189},
        'Scottish families, DEF':
    {'hammondnumber': 3, 'hammondnumb2__gte': 190,
     'hammondnumb2__lte': 239},
        'Scottish families, GHI':
    {'hammondnumber': 3, 'hammondnumb2__gte': 240,
     'hammondnumb2__lte': 304},
        'Scottish families, JKL':
    {'hammondnumber': 3, 'hammondnumb2__gte': 305,
     'hammondnumb2__lte': 374},
        'Scottish families, MNO':
    {'hammondnumber': 3, 'hammondnumb2__gte': 375,
     'hammondnumb2__lte': 459},
        'Scottish families, PQR':
    {'hammondnumber': 3, 'hammondnumb2__gte': 450,
     'hammondnumb2__lte': 519},
        'Scottish families, STU':
    {'hammondnumber': 3, 'hammondnumb2__gte': 520,
     'hammondnumb2__lte': 584},
        'Scottish families, VWXYZ':
    {'hammondnumber': 3, 'hammondnumb2__gte': 585,
     'hammondnumb2__lte': 624},
        'Bishop\'s relatives':
    {'hammondnumber': 3, 'hammondnumb2': 625},
        'Burgesses':
    {'hammondnumber': 3, 'hammondnumb2__gte': 630,
     'hammondnumb2__lte': 648},
        'Agreements: kings and queens':
    {'hammondnumber': 4, 'hammondnumb2__gte': 1, 'hammondnumb2__lte': 2},
        'Agreements: between ecclesiastics':
    {'hammondnumber': 4, 'hammondnumb2__gte': 3, 'hammondnumb2__lte': 14},
        'Agreements: ecclesiastics and lay':
    {'hammondnumber': 4, 'hammondnumb2__gte': 15, 'hammondnumb2__lte': 25},
        'Agreements: between laypeople':
    {'hammondnumber': 4, 'hammondnumb2': 26},
        'Papal legates and auditors':
    {'hammondnumber': 4, 'hammondnumb2__gte': 30, 'hammondnumb2__lte': 31},
        'Papal judges delegate':
    {'hammondnumber': 4, 'hammondnumb2': 32},
        'Settlements: bishops and other religious':
    {'hammondnumber': 4, 'hammondnumb2__gte': 33, 'hammondnumb2__lte': 35},
        'Church court documents (misc)':
    {'hammondnumber': 4, 'hammondnumb2': 36},
        'Secular court documents (misc)':
    {'hammondnumber': 4, 'hammondnumb2': 37},
        'Inquests':
    {'hammondnumber': 4, 'hammondnumb2': 38},
        'Perambulations':
    {'hammondnumber': 4, 'hammondnumb2__gte': 39, 'hammondnumb2__lte': 40},
        'Royal ambassadors':
    {'hammondnumber': 4, 'hammondnumb2': 41},
        'National councils':
    {'hammondnumber': 4, 'hammondnumb2': 42},
        'ERA documents':
    {'hammondnumber': 5, },
        'Fealties and Homages (post-1286)':
    {'hammondnumber': 6, },
}


def createPersonSurface_name(obj):
    """ called from the admin model instance
    """
    # procedure for creating the surface name
    sur = getattr(obj, 'surname', None)
    if getattr(obj, 'persondisplayname', None) == "":
        composed_name = ""
        fore = getattr(obj, 'forename', None)
        sonof = getattr(obj, 'sonof', None)
        patr = getattr(obj, 'patronym', None)
        ofstr = getattr(obj, 'ofstring', None)
        place = getattr(obj, 'placeandinst', None)
        dates = getattr(obj, 'datestring', None)

        if sur:
            composed_name = fore + " " + sur
        else:
            composed_name = fore
        if patr:
            composed_name += ", " + sonof + " " + patr
        if place:
            composed_name += ", " + ofstr + " " + place
        composed_name += " " + dates
        obj.persondisplayname = composed_name.strip()
        print("*********Creating  surface name")

    # procedure for creating the medieval gaelic name
    field1 = getattr(obj, 'standardmedievalname', None)
    if field1 is None or field1.strip() == "" or field1.strip() == u"":
        print("*********Creating  standardmedievalname")
        composed_name = ""
        medievalfore = getattr(obj, 'medievalgaelicforename', "")
        medievalsur = getattr(obj, 'medievalgaelicsurname', "")
        if medievalfore:
            composed_name = "%s %s" % (medievalfore.name, medievalsur)
        else:
            composed_name = "%s %s" % ("", medievalsur)
        obj.standardmedievalname = composed_name.strip()

    # procedure for creating the modern gaelic name
    field2 = getattr(obj, 'moderngaelicname', None)
    if field2 is None or field2.strip() == "" or field2.strip() == u"":
        print("*********Creating moderngaelicname")
        composed_name = ""
        modernfore = getattr(obj, 'moderngaelicforename', "")
        modernsur = getattr(obj, 'moderngaelicsurname', "")
        if modernfore:
            composed_name = "%s %s" % (modernfore.name, modernsur)
        else:
            composed_name = "%s %s" % ("", modernsur)
        obj.moderngaelicname = composed_name.strip()

    return obj


def assign_grantorCategory(sourceInstance):
    """
    The method doesn't save the Source object, it just updates
    it and return it
    """
    for constraint in GRANTOR_CATEGORIES:
        flag = 0
        for innerConstraint in GRANTOR_CATEGORIES[constraint]:
            attrs = innerConstraint.split("__")
            value = GRANTOR_CATEGORIES[constraint][innerConstraint]
            if len(attrs) == 1:	 # eg: "hammondnumb2".split("__")[0]
                if getattr(sourceInstance, attrs[0], None):
                    if not (getattr(sourceInstance, attrs[0], None) == value):
                        flag = 1
                        break
            else:  # eg: "hammondnumb2__gte".split("__")
                if attrs[1] == 'gte':
                    if getattr(sourceInstance, attrs[0], None):
                        if not (getattr(sourceInstance,
                                        attrs[0], None) >= value):
                            flag = 1
                            break
                if attrs[1] == 'lte':
                    if getattr(sourceInstance, attrs[0], None):
                        if not (getattr(sourceInstance,
                                        attrs[0], None) <= value):
                            flag = 1
                            break
        if flag == 0:
            print("Assign_Grantorcategory:	 source[%d]	 h1[%s]\
                h2[%s] h3[%s] ===>	%s" % (sourceInstance.id,
                                          str(sourceInstance.hammondnumber),
                                          str(sourceInstance.hammondnumb2),
                                          str(sourceInstance.hammondnumb3),
                                          constraint))
            # we have a match: save the item and stop iterating through the
            # GRANTOR_CATEGORIES
            cat = GrantorCategory.objects.filter(name=constraint)
            if cat:
                category = cat[0]
            else:
                category = GrantorCategory(name=constraint)
                category.save()
            sourceInstance.grantor_category = category
            break
    if flag == 1:
        print("Assign_Grantorcategory: source[%d] h1[%s] h2[%s]\
        h3[%s] ===> FAILED (no adequate\
        mapping found)" % (sourceInstance.id,
                           str(sourceInstance.hammondnumber),
                           str(sourceInstance.hammondnumb2),
                           str(sourceInstance.hammondnumb3)))
    return sourceInstance


# 2011-04-20: transferred various methods from the 'fixtures' file
# (manually launched) to the editing workflow


def create_helperKeywordsearch(obj):
    """
    Creates the text field used as an index for searches..

    At the moment we do this just for Factoids, Charters and People


    >>> f1 = Factoid.objects.all()[50]
    >>> f1
    <Factoid: abbot of Melrose>
    >>> f1.__class__
    <class 'pomsapp.models.Factoid'>
    >>> f1.__class__.__name__
    'Factoid'
    >>> ft1 = FactTitle.objects.all()[50]
    >>> ft1.__class__.__name__
    'FactTitle'


    People: Searching on fields: full modern name, standard medieval
    name, modern gaelic name, ID number.
    Document: Searching on fields: H-number, trad.ID, description, ID number.
    Factoid: Searching on fields: short description, source for
    data entry, ID number.

    """
    #  now do the actions:
    if obj.__class__.__name__ == 'Person':
        print(
            "Creating helperKeywordsearch text for person id[%d] " % obj.id)
        string = ""
        try:
            string += obj.persondisplayname + " "
            string += obj.standardmedievalname + " "
            string += obj.moderngaelicname + " "
            string += str(obj.id) + " "
            # string += obj.persondescription + " "
            obj.helper_keywordsearch = string
            print("Saved!")
            print("HelperKeywordsearch	 = [%s]" % smart_text(string))
        except BaseException:
            print(
                "************\nProblem with person\
                id[%d]\n************" % (obj.id))
            pass
        return obj

    elif obj.__class__.__name__ in ('Source', 'Charter'):

        print(
            "Saving helperKeywordsearch text for source id[%d]" % obj.id)
        string = ""
        try:
            string += obj.helper_hnumber + " "  # if it's a charter
            string += obj.source_tradid + " "
            string += obj.description + " "
            string += str(obj.id) + " "
            string = string.replace("_", "")  # delete the italics
            obj.helper_keywordsearch = string
            print("Saved!")
            print("HelperKeywordsearch	 = [%s]" % smart_text(string))
        except BaseException:
            print(
                "************\nProblem with source\
                id[%d]\n************" % (obj.id))
            pass
        return obj

    elif obj.__class__.__name__ in ('FactTitle', 'FactPossession',
                                    'FactTransaction', 'FactRelationship',
                                    'FactReference'):
        print("Saving helperKeywordsearch text for %s id[%d]" % (
            obj.__class__.__name__, obj.id))
        string = ""
        try:
            string += obj.shortdesc + " "
            string += obj.sourcekey.sourcefordataentry + " "
            string += str(obj.id) + " "
            # string += x.standardmedievalname + " "
            string = string.replace("_", "")  # delete the italics
            obj.helper_keywordsearch = string
            print("Saved!")
            print("HelperKeywordsearch	 = [%s]" % smart_text(string))
        except BaseException:
            print(
                "************\nProblem with factoid\
                id[%d]\n************" % (obj.id))
            pass
        return obj

    elif obj.__class__.__name__ == 'Place':
        print(
            "Creating helperKeywordsearch text for place id[%d] " % obj.id)
        string = ""
        try:
            string += obj.name + " "
            try:
                string += obj.parent.name + " "
            except BaseException:
                pass
            string += str(obj.id) + " "
            obj.helper_keywordsearch = string
            print("Saved!")
            print("HelperKeywordsearch	 = [%s]" % smart_text(string))
        except BaseException:
            print(
                "************\nProblem with\
                place id[%d]\n************" % (obj.id))
            pass
        return obj

    else:
        raise TypeError(
            "create_helperKeywordsearch error: you didn't"
            "pass the right object! (I accept only Person, "
            "Source or Factoid-s- instances...)"
        )


def handle_tickboxes(obj_instance):
    """
    obj_instance =	either a Charter or Transaction instance

    Consolidates all tickboxes value in a new table, so to allow a\
    facet to be built out of it
    """
    if obj_instance._meta.verbose_name == 'Document':
        # it's a charter
        print(
            "Adding m2m reference to DocTickboxes table for\
            Charter [%d]" % obj_instance.id)
        # first clear existing rels
        obj_instance.helper_tickboxes.clear()
        if obj_instance.ischirograph:
            ischirograph, created = DocTickboxes.objects.get_or_create(
                name="Chirograph",)
            obj_instance.helper_tickboxes.add(ischirograph)
        if obj_instance.letterpatent:
            letterpatent, created = DocTickboxes.objects.get_or_create(
                name="Letter Patent",)
            obj_instance.helper_tickboxes.add(letterpatent)
        if obj_instance.origcontemp:
            origcontemp, created = DocTickboxes.objects.get_or_create(
                name="Original (contemporary)",)
            obj_instance.helper_tickboxes.add(origcontemp)
        if obj_instance.duporigcontemp:
            duporigcontemp, created = DocTickboxes.objects.get_or_create(
                name="Duplicate Original (contemporary)",)
            obj_instance.helper_tickboxes.add(duporigcontemp)
        if obj_instance.orignoncontemp:
            orignoncontemp, created = DocTickboxes.objects.get_or_create(
                name="Original (non-contemporary)",)
            obj_instance.helper_tickboxes.add(orignoncontemp)
        if obj_instance.duporignoncontemp:
            duporignoncontemp, created = DocTickboxes.objects.get_or_create(
                name="Duplicate Original (non-contemporary)",)
            obj_instance.helper_tickboxes.add(duporignoncontemp)
    elif obj_instance._meta.verbose_name == 'fact transaction':
        print(
            "Adding m2m reference to TransTickboxes table for\
            Transaction [%d]" % obj_instance.id)
        # first clear existing rels
        obj_instance.helper_tickboxes.clear()
        if obj_instance.isprimary:
            isprimary, created = TransTickboxes.objects.get_or_create(
                name="Primary Transaction",)
            obj_instance.helper_tickboxes.add(isprimary)
        if obj_instance.isdare:
            isdare, created = TransTickboxes.objects.get_or_create(
                name="Dare",)
            obj_instance.helper_tickboxes.add(isdare)
        if obj_instance.isexchange:
            isexchange, created = TransTickboxes.objects.get_or_create(
                name="Exchange",)
            obj_instance.helper_tickboxes.add(isexchange)
        if obj_instance.verbsnotspecified:
            verbsnotspecified, created = TransTickboxes.objects.get_or_create(
                name="Verbs not specified",)
            obj_instance.helper_tickboxes.add(verbsnotspecified)
        if obj_instance.conveth:
            conveth, created = TransTickboxes.objects.get_or_create(
                name="Conveth",)
            obj_instance.helper_tickboxes.add(conveth)
        if obj_instance.genericwitnesses:
            genericwitnesses, created = TransTickboxes.objects.get_or_create(
                name="Witnesses in original, but not copied into cartulary",)
            obj_instance.helper_tickboxes.add(genericwitnesses)
        if obj_instance.testemeipso:
            testemeipso, created = TransTickboxes.objects.get_or_create(
                name="Teste Me Ipso",)
            obj_instance.helper_tickboxes.add(testemeipso)
        if obj_instance.previouschartermention:
            previouschartermention, created =\
                TransTickboxes.objects.get_or_create(
                    name="Previous mention of charter",)
            obj_instance.helper_tickboxes.add(previouschartermention)
        if obj_instance.previouschirographmention:
            previouschirographmention, created =\
                TransTickboxes.objects.get_or_create(
                    name="Previous mention of chirograph",)
            obj_instance.helper_tickboxes.add(previouschirographmention)
        if obj_instance.perambulation:
            perambulation, created = TransTickboxes.objects.get_or_create(
                name="Perambulation",)
            obj_instance.helper_tickboxes.add(perambulation)
        if obj_instance.corroborationsealing:
            corroborationsealing, created =\
                TransTickboxes.objects.get_or_create(
                    name="Corroboration/Sealing",)
            obj_instance.helper_tickboxes.add(corroborationsealing)
        if obj_instance.ismalediction:
            ismalediction, created = TransTickboxes.objects.get_or_create(
                name="malediction",)
            obj_instance.helper_tickboxes.add(ismalediction)
        if obj_instance.bothaddressorsmentioned:
            bothaddressorsmentioned, created =\
                TransTickboxes.objects.get_or_create(
                    name="Both addressors mentioned",)
            obj_instance.helper_tickboxes.add(bothaddressorsmentioned)
        if obj_instance.warrandice:
            warrandice, created = TransTickboxes.objects.get_or_create(
                name="Warrandice",)
            obj_instance.helper_tickboxes.add(warrandice)
