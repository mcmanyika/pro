from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.db import connection
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def fetch_members():
    members = connection.cursor()
    members.cursor.execute(
        """Select
            aa.root AS id, au.username, au.first_name AS fname, au.last_name AS lname, aa.gender, aa.phone
            FROM auth_User au 
            INNER JOIN joins_t_acct_attributes aa ON aa.root = au.id
            """
    )

    return dictfetchall(members)
