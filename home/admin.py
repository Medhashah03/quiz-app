from django.contrib import admin
from .models import *

# Register your models here.

# username : admin Password: admin


admin.site.register(Category)

# Stacked inline is used to show data of foreign keys
class AnswerAdmin(admin.StackedInline):
    model = Answer

# Displays AnswerAdmin inline with QuestionAdmin
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin]

# Class Over ride
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)