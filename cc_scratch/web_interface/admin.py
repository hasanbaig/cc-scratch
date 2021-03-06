#-------------------------------------------------------------------------------
# Cloud-COPASI
# Copyright (c) 2013 Edward Kent.
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the GNU Public License v3.0
# which accompanies this distribution, and is available at
# http://www.gnu.org/licenses/gpl.html
#-------------------------------------------------------------------------------
from django.contrib import admin
from cc_scratch.web_interface.models import *

admin.site.register(AWSAccessKey)
admin.site.register(VPC)
admin.site.register(CondorPool)
admin.site.register(EC2Instance)
admin.site.register(EC2KeyPair)
admin.site.register(ElasticIP)
admin.site.register(Task)
admin.site.register(Subtask)
admin.site.register(CondorJob)
admin.site.register(SpotRequest)
admin.site.register(EC2Pool)
admin.site.register(BoscoPool)
admin.site.register(Profile)
