from import_export import resources
from libs.models import t_payment
from django.db.models import Count
from django.db import *

class DailyTransactions(resources.ModelResource):
	class Meta:
	    model = t_payment
	    fields = ('purpose', 'currency', 'amount', 'commitment', 'timestamp')