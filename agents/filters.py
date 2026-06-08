import django_filters
from .models import Agent


class AgentFilter(django_filters.FilterSet):
      designation=django_filters.CharFilter(field_name='designation',lookup_expr='iexact')
      agent_name=django_filters.CharFilter(field_name='agent_name',lookup_expr='icontains')
      agent_id=django_filters.RangeFilter(field_name='agent_id')

      class Meta:
            model=Agent
            fields=['designation','agent_name','agent_id']
