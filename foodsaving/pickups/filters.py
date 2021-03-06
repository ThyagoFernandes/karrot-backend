from django_filters import rest_framework as filters

from foodsaving.base.filters import ISODateTimeFromToRangeFilter
from foodsaving.pickups.models import PickupDate, PickupDateSeries, Feedback


class PickupDateSeriesFilter(filters.FilterSet):
    class Meta:
        model = PickupDateSeries
        fields = [
            'store',
        ]


class PickupDatesFilter(filters.FilterSet):
    store = filters.NumberFilter(field_name='store')
    group = filters.NumberFilter(field_name='store__group__id')
    date = ISODateTimeFromToRangeFilter(field_name='date')
    feedback_possible = filters.BooleanFilter(method='filter_feedback_possible')

    class Meta:
        model = PickupDate
        fields = ['store', 'group', 'date', 'series', 'feedback_possible']

    def filter_feedback_possible(self, qs, name, value):
        if value is True:
            return qs.only_feedback_possible(self.request.user)
        return qs.exclude_feedback_possible(self.request.user)


class FeedbackFilter(filters.FilterSet):
    group = filters.NumberFilter(field_name='about__store__group__id')
    store = filters.NumberFilter(field_name='about__store__id')
    about = filters.NumberFilter(field_name='about')
    given_by = filters.NumberFilter(field_name='given_by')
    created_at = ISODateTimeFromToRangeFilter(field_name='created_at')

    class Meta:
        model = Feedback
        fields = ['group', 'store', 'about', 'given_by', 'created_at']
