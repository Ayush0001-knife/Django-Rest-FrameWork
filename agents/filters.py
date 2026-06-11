import django_filters
from .models import Agent


class AgentFilter(django_filters.FilterSet):
      designation=django_filters.CharFilter(field_name='designation',lookup_expr='iexact')
      agent_name=django_filters.CharFilter(field_name='agent_name',lookup_expr='icontains')
      # agent_id=django_filters.RangeFilter(field_name='agent_id')
      id_min=django_filters.CharFilter(method="filter_by_id_range",label="From Agent ID")
      id_max=django_filters.CharFilter(method="filter_by_id_range",label="To Agent ID")

      class Meta:
            model=Agent
            # fields=['designation','agent_name','agent_id']
            fields=['designation','agent_name','id_min','id_max']


      def filter_by_id_range(self,queryset,name,value):
            if (name=='id_min'):
                  return queryset.filter(agent_id__gte=value)
            elif (name=='id_max'):
                  return queryset.filter(agent_id__lte=value)
            return queryset      

