from itertools import chain
from typing import List

from django.db.models import Case, When, F
from users.models import User
from users import services
from news.models import Articles
# from resume.models import Respond, VacancyRespond, InternshipRespond



def added_annotate_favorite_field(obj: list, related_field: str, nested_field: str, user: User) -> list:
    filter_field = {
        f'{related_field}__content': user,
        f'{related_field}__{nested_field}_id': F('id')
    }
    result = obj.annotate(added=Case(When(**filter_field, then=True), default=False),
                          uuid_added=Case(When(**filter_field, then=f'{related_field}__pk')))
    return result