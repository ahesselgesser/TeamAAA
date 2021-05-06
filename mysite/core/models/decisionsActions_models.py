"""
This file contains models most directly related to decisions and actions
Copied from previous project
"""
import os
from django.db import models

class DecisionsActions(models.Model):
    """
    Model of decisions/actions for a report
    """
    sloIR = models.OneToOneField('SLOInReport', on_delete=models.CASCADE)
    text = models.CharField(max_length=3000, blank=True, default="")

    """
    Model to hold supplements to the report as a whole
    Removed for this project
    """