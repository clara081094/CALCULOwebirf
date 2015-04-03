from django.contrib import admin
from calculus.models import Question

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Pregunta',               {'fields': ['question_text']}),
        ('Informacion de fecha', {'fields': ['pub_date']}),
    ]

admin.site.register(Question, QuestionAdmin)

