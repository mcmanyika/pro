from django.conf.urls import include, url
from django.contrib import admin
from finance.views import *

urlpatterns = [
    # url(r'^$', currency, name='currency'),
    url(r"^add-currency/", ajax_currency, name="add-currency"),
    url(r"^add-incomehead/", ajax_incomehead, name="add-incomehead"),
    url(r"^add-commitment/", ajax_commitment, name="add-commitment"),
    url(r"^transaction/(?P<id>.*)$", transaction, name="transaction"),
    url(r"^all_receipts/(?P<id>.*)$", all_receipts, name="all_receipts"),
    url(r"^receipt/(?P<id>.*)$", receipt, name="receipt"),
    url(r"^single_rec/(?P<id>.*)$", single_rec, name="single_rec"),
    url(r"^filter-trans/", filter_trans, name="filter-trans"),
    url(r"^filter-by-incomehead/", filter_income_head, name="filter-by-incomehead"),
    # url(r'^transaction/(?P<id>.*)$', transaction, name='transaction'),
    url(r"^seed-payment/", seed_payments, name="seed-payment"),
    url(r"^all-seeds/", all_seeds, name="all-seeds"),
    url(r"^seed/(?P<id>.*)$", seed_receipt, name="seed"),
]
